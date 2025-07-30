#!/bin/bash

# EVE-NG Lab Setup Script
# This script helps you configure the Network AI Agent for your EVE-NG lab

echo "🔬 Network AI Agent - EVE-NG Lab Setup"
echo "======================================"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command_exists docker; then
    echo "❌ Docker is not installed. Please install Docker and try again."
    exit 1
fi

if ! command_exists docker-compose; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Navigate to project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

echo "📁 Working in: $PROJECT_DIR"

# Check if testbed.yaml exists
TESTBED_FILE="react_ai_agent_cisco_ios_xe/testbed.yaml"
TEMPLATE_FILE="react_ai_agent_cisco_ios_xe/lab_config_template.yaml"

if [ ! -f "$TESTBED_FILE" ]; then
    echo "📝 Creating testbed.yaml from template..."
    if [ -f "$TEMPLATE_FILE" ]; then
        cp "$TEMPLATE_FILE" "$TESTBED_FILE"
        echo "✅ testbed.yaml created from template"
        echo ""
        echo "⚠️  IMPORTANT: Please edit $TESTBED_FILE and update:"
        echo "   - Device IP addresses (your EVE-NG management network)"
        echo "   - Device credentials (usernames and passwords)"
        echo "   - Add/remove devices based on your lab topology"
        echo ""
        read -p "Press Enter when you have configured your testbed.yaml..."
    else
        echo "❌ Template file not found: $TEMPLATE_FILE"
        exit 1
    fi
else
    echo "✅ testbed.yaml already exists"
fi

# Optional: Validate testbed file if pyATS is available
if command_exists pyats; then
    echo "🔍 Validating testbed.yaml..."
    if pyats validate testbed "$TESTBED_FILE"; then
        echo "✅ testbed.yaml validation passed"
    else
        echo "⚠️  testbed.yaml validation failed - please check your configuration"
        echo "You can still proceed, but connectivity might not work properly"
    fi
else
    echo "ℹ️  pyATS not available - skipping testbed validation"
fi

# Test EVE-NG connectivity (if specified)
echo ""
read -p "🌐 Do you want to test basic connectivity to your EVE-NG devices? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🔌 Testing basic connectivity..."
    
    # Extract device IPs from testbed.yaml (basic parsing)
    if command_exists grep && command_exists awk; then
        echo "Found device IPs:"
        grep -A 10 "ip:" "$TESTBED_FILE" | grep "ip:" | awk '{print $2}' | while read ip; do
            # Remove quotes and test ping
            clean_ip=$(echo $ip | tr -d '"' | tr -d "'")
            if ping -c 1 -W 3 "$clean_ip" >/dev/null 2>&1; then
                echo "  ✅ $clean_ip - reachable"
            else
                echo "  ❌ $clean_ip - not reachable"
            fi
        done
    fi
fi

echo ""
echo "🚀 Starting the Network AI Agent..."
echo "This may take a few minutes on first run (downloading AI model)..."
echo ""

# Start the application
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Check if services are running
if docker-compose ps | grep -q "Up"; then
    echo ""
    echo "🎉 SUCCESS! The Network AI Agent is running!"
    echo ""
    echo "🌐 Open your browser and go to: http://localhost:8501"
    echo ""
    echo "💡 Try these commands to test your setup:"
    echo '   "Discover all devices in the lab"'
    echo '   "Test connectivity to all devices"'
    echo '   "Show me interface status on [device_name]"'
    echo ""
    echo "📋 Available devices in your testbed:"
    if command_exists grep && command_exists awk; then
        grep -B 1 "alias:" "$TESTBED_FILE" | grep -v "alias:" | grep -v "^--$" | awk -F: '{print "   - " $1}'
    fi
    echo ""
    echo "🛑 To stop the agent: docker-compose down"
else
    echo "❌ Failed to start services. Check the logs:"
    echo "   docker-compose logs"
fi 