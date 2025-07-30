#!/bin/bash

# Quick Start Script for Local Network AI Agent

echo "🚀 Starting Network AI Agent..."

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

# Start Streamlit
echo "🌐 Starting Streamlit on http://localhost:8501"
echo "📋 Available commands to try:"
echo '   "Discover all devices in the lab"'
echo '   "Test connectivity to all devices"'
echo '   "Show interface status on [device_name]"'
echo ""

streamlit run react_ai_agent_cisco_ios_xe.py 