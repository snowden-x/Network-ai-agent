#!/bin/bash

# Local Setup Script for Network AI Agent
# This script sets up the agent to run locally with your existing Ollama installation

echo "🚀 Network AI Agent - Local Setup"
echo "================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip and try again."
    exit 1
fi

echo "✅ Python 3 and pip are available"

# Check if Ollama is running locally
echo "🔍 Checking local Ollama installation..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "✅ Ollama is running on localhost:11434"
    
    # Check if mistral model is available
    if curl -s http://localhost:11434/api/tags | grep -q "mistral"; then
        echo "✅ mistral model is available"
    else
        echo "📥 Downloading mistral model..."
        ollama pull mistral
    fi
else
    echo "❌ Ollama is not running on localhost:11434"
    echo "Please start Ollama first: ollama serve"
    echo "Then install the model: ollama pull mistral"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📦 Installing Python packages..."
pip3 install -r requirements.txt

# Check if testbed.yaml exists
TESTBED_FILE="react_ai_agent_cisco_ios_xe/testbed.yaml"
TEMPLATE_FILE="react_ai_agent_cisco_ios_xe/lab_config_template.yaml"

if [ ! -f "$TESTBED_FILE" ]; then
    echo "📝 Creating testbed.yaml from template..."
    cp "$TEMPLATE_FILE" "$TESTBED_FILE"
    echo "✅ testbed.yaml created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit $TESTBED_FILE and update:"
    echo "   - Device IP addresses (your EVE-NG management network)"
    echo "   - Device credentials (usernames and passwords)"
    echo "   - Add/remove devices based on your lab topology"
    echo ""
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "🚀 To start the agent:"
echo "   source venv/bin/activate"
echo "   cd react_ai_agent_cisco_ios_xe"
echo "   streamlit run react_ai_agent_cisco_ios_xe.py"
echo ""
echo "🌐 Then open: http://localhost:8501"
echo ""
echo "💡 Or use the quick start script: ./scripts/start_local.sh" 