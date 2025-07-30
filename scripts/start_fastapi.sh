#!/bin/bash

# FastAPI Start Script for Network AI Agent

echo "🚀 Starting Network AI Agent (FastAPI)..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./scripts/setup_local.sh first"
    exit 1
fi

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "❌ Ollama is not running. Please start it first:"
    echo "   ollama serve"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Navigate to the agent directory
cd react_ai_agent_cisco_ios_xe

# Start FastAPI with uvicorn
echo "🌐 Starting FastAPI server on http://localhost:8000"
echo "📋 Available endpoints:"
echo "   GET  /           - Web interface"
echo "   GET  /docs       - API documentation"
echo "   GET  /health     - Health check"
echo "   GET  /devices    - Discover devices"
echo "   POST /query      - Ask questions"
echo ""

uvicorn fastapi_agent:app --host 0.0.0.0 --port 8000 --reload 