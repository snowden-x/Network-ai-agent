from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict, Any
import json
import asyncio
import logging
import requests
from datetime import datetime

# Import agent functionality
from react_ai_agent_cisco_ios_xe import (
    check_ollama_connection, 
    discover_lab_devices, 
    test_lab_connectivity,
    run_show_command,
    agent_executor
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Network AI Agent API",
    description="AI-powered network troubleshooting agent for EVE-NG labs",
    version="1.0.0"
)

# Pydantic models for API requests/responses
class QueryRequest(BaseModel):
    question: str
    device_name: Optional[str] = None
    chat_history: Optional[str] = ""

class CommandRequest(BaseModel):
    command: str
    device_name: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    device_used: Optional[str] = None
    timestamp: str
    status: str

class HealthResponse(BaseModel):
    status: str
    ollama_connected: bool
    message: str
    timestamp: str

# Global chat history storage (in production, use Redis or database)
chat_sessions = {}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve a simple web interface"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Network AI Agent</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .chat-container { border: 1px solid #ddd; height: 400px; overflow-y: auto; padding: 10px; margin: 10px 0; }
            .user-message { background: #e3f2fd; padding: 10px; margin: 5px 0; border-radius: 5px; }
            .agent-message { background: #f5f5f5; padding: 10px; margin: 5px 0; border-radius: 5px; }
            input[type="text"] { width: 70%; padding: 10px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            .status { padding: 10px; margin: 10px 0; border-radius: 5px; }
            .status.ok { background: #d4edda; color: #155724; }
            .status.error { background: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <h1>🔬 Network AI Agent for EVE-NG Lab</h1>
        <div id="status" class="status">Checking connection...</div>
        
        <div class="chat-container" id="chatContainer"></div>
        
        <div>
            <input type="text" id="questionInput" placeholder="Ask your network question..." onkeypress="handleKeyPress(event)">
            <button onclick="sendQuestion()">Send</button>
        </div>
        
        <div style="margin-top: 20px;">
            <h3>Quick Actions:</h3>
            <button onclick="discoverDevices()">Discover Devices</button>
            <button onclick="testConnectivity()">Test Connectivity</button>
        </div>
        
        <script>
            // Check health status
            fetch('/health')
                .then(response => response.json())
                .then(data => {
                    const statusDiv = document.getElementById('status');
                    if (data.ollama_connected) {
                        statusDiv.className = 'status ok';
                        statusDiv.textContent = '✅ ' + data.message;
                    } else {
                        statusDiv.className = 'status error';
                        statusDiv.textContent = '❌ ' + data.message;
                    }
                });
            
            function addMessage(content, isUser) {
                const chatContainer = document.getElementById('chatContainer');
                const messageDiv = document.createElement('div');
                messageDiv.className = isUser ? 'user-message' : 'agent-message';
                messageDiv.innerHTML = isUser ? '<strong>You:</strong> ' + content : '<strong>Agent:</strong> ' + content;
                chatContainer.appendChild(messageDiv);
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
            
            function sendQuestion() {
                const input = document.getElementById('questionInput');
                const question = input.value.trim();
                if (!question) return;
                
                addMessage(question, true);
                input.value = '';
                
                fetch('/query', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question: question})
                })
                .then(response => response.json())
                .then(data => {
                    addMessage(data.answer, false);
                })
                .catch(error => {
                    addMessage('Error: ' + error, false);
                });
            }
            
            function handleKeyPress(event) {
                if (event.key === 'Enter') {
                    sendQuestion();
                }
            }
            
            function discoverDevices() {
                addMessage('Discover all devices in the lab', true);
                sendQuestion();
            }
            
            function testConnectivity() {
                addMessage('Test connectivity to all devices', true);
                sendQuestion();
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check the health of the service and Ollama connection"""
    connected, message = check_ollama_connection()
    
    return HealthResponse(
        status="healthy" if connected else "degraded",
        ollama_connected=connected,
        message=message,
        timestamp=datetime.now().isoformat()
    )

@app.get("/devices")
async def get_devices():
    """Discover available devices in the lab"""
    try:
        result = discover_lab_devices()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/connectivity")
async def test_connectivity():
    """Test connectivity to all lab devices"""
    try:
        result = test_lab_connectivity()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/command")
async def execute_command(request: CommandRequest):
    """Execute a specific command on a device"""
    try:
        result = run_show_command(request.command, request.device_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query", response_model=QueryResponse)
async def query_agent(request: QueryRequest):
    """Send a natural language query to the AI agent"""
    try:
        # Get or create session
        session_id = "default"  # In production, use proper session management
        if session_id not in chat_sessions:
            chat_sessions[session_id] = ""
        
        # Build chat history
        chat_history = chat_sessions[session_id]
        if request.chat_history:
            chat_history = request.chat_history
        
        # Query the agent
        response = agent_executor.invoke({
            "input": request.question,
            "chat_history": chat_history,
            "agent_scratchpad": ""
        })
        
        # Update chat history
        chat_sessions[session_id] += f"\nUser: {request.question}\nAssistant: {response.get('output', 'No response')}"
        
        return QueryResponse(
            answer=response.get('output', 'No response available'),
            device_used=request.device_name,
            timestamp=datetime.now().isoformat(),
            status="success"
        )
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/chat/history/{session_id}")
async def get_chat_history(session_id: str):
    """Get chat history for a session"""
    return {"history": chat_sessions.get(session_id, "")}

@app.delete("/chat/history/{session_id}")
async def clear_chat_history(session_id: str):
    """Clear chat history for a session"""
    chat_sessions[session_id] = ""
    return {"message": "Chat history cleared"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 