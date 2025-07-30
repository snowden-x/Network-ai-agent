import os
import json
import difflib
import streamlit as st
import requests
from pyats.topology import loader
from langchain_community.llms import Ollama
from langchain_core.tools import tool, render_text_description
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from genie.libs.parser.utils import get_parser

# Check Ollama connection at startup
def check_ollama_connection():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model.get('name', '') for model in models]
            if any('mistral' in name for name in model_names):
                return True, "Connected to Ollama with mistral model"
            else:
                return False, "Ollama is running but mistral model not found. Run: ollama pull mistral"
        else:
            return False, f"Ollama API returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Cannot connect to Ollama on localhost:11434. Please start Ollama: ollama serve"

# Display connection status in Streamlit
def display_connection_status():
    connected, message = check_ollama_connection()
    if connected:
        st.success(f"✅ {message}")
        return True
    else:
        st.error(f"❌ {message}")
        st.info("💡 Make sure Ollama is running: `ollama serve` and model is installed: `ollama pull mistral`")
        return False

# Function to run any supported show command using pyATS
def run_show_command(command: str, device_name: str = None):
    try:
        # Disallowed modifiers
        disallowed_modifiers = ['|', 'include', 'exclude', 'begin', 'redirect', '>', '<']

        # Check for disallowed modifiers
        for modifier in disallowed_modifiers:
            if modifier in command:
                return {"error": f"Command '{command}' contains disallowed modifier '{modifier}'. Modifiers are not allowed."}

        # Load the testbed
        print("Loading testbed...")
        testbed = loader.load('testbed.yaml')

        # If no device specified, use the first available Cisco device
        if device_name is None:
            cisco_devices = [name for name, dev in testbed.devices.items() 
                           if dev.os in ['iosxe', 'ios']]
            if not cisco_devices:
                return {"error": "No Cisco devices found in testbed"}
            device_name = cisco_devices[0]
            print(f"No device specified, using: {device_name}")

        # Access the device from the testbed
        if device_name not in testbed.devices:
            available_devices = list(testbed.devices.keys())
            return {"error": f"Device '{device_name}' not found. Available devices: {available_devices}"}
            
        device = testbed.devices[device_name]
        print(f"Selected device: {device_name} ({device.alias})")

        # Connect to the device
        print(f"Connecting to {device_name} at {device.connections.cli.ip}...")
        device.connect()

        # Check if a pyATS parser is available for the command
        print(f"Checking if a parser exists for the command: {command}")
        parser = get_parser(command, device)
        if parser is None:
            return {"error": f"No parser available for the command: {command}"}

        # Execute the command and parse the output using Genie
        print(f"Executing '{command}' on {device_name}...")
        parsed_output = device.parse(command)

        # Close the connection
        print(f"Disconnecting from {device_name}...")
        device.disconnect()

        # Return the parsed output (JSON) with device info
        return {
            "device": device_name,
            "device_alias": device.alias,
            "command": command,
            "output": parsed_output,
            "status": "success"
        }
    except Exception as e:
        # Handle exceptions and provide error information
        return {"error": str(e), "device": device_name if device_name else "unknown"}

# Function to load supported commands from a JSON file
def load_supported_commands():
    file_path = 'commands.json'  # Ensure the file is named correctly

    # Check if the file exists
    if not os.path.exists(file_path):
        return {"error": f"Supported commands file '{file_path}' not found."}

    try:
        # Load the JSON file with the list of commands
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Extract the command strings into a list
        command_list = [entry['command'] for entry in data]
        return command_list
    except Exception as e:
        return {"error": f"Error loading supported commands: {str(e)}"}

# Function to check if a command is supported with fuzzy matching
def check_command_support(command: str) -> dict:
    command_list = load_supported_commands()

    if "error" in command_list:
        return command_list

    # Find the closest matches to the input command using difflib
    close_matches = difflib.get_close_matches(command, command_list, n=1, cutoff=0.6)

    if close_matches:
        closest_command = close_matches[0]
        return {"status": "supported", "closest_command": closest_command}
    else:
        return {"status": "unsupported", "message": f"The command '{command}' is not supported. Please check the available commands."}

# Function to process agent response and chain tools
def process_agent_response(response):
    if response.get("status") == "supported" and "next_tool" in response.get("action", {}):
        next_tool = response["action"]["next_tool"]
        command_input = response["action"]["input"]
        device_name = response["action"].get("device") # Get device_name from action

        # Automatically invoke the next tool (run_show_command_tool)
        return agent_executor.invoke({
            "input": command_input,
            "chat_history": st.session_state.chat_history,
            "agent_scratchpad": "",
            "tool": next_tool,
            "device": device_name # Pass device_name to the tool
        })
    else:
        return response

# Function to apply configuration using pyATS
def apply_device_configuration(config_commands: str):
    try:
        # Load the testbed
        print("Loading testbed...")
        testbed = loader.load('testbed.yaml')

        # Access the device from the testbed
        device = testbed.devices['Cat8000V']

        # Connect to the device
        print("Connecting to device...")
        device.connect()

        # Apply the configuration
        print(f"Applying configuration:\n{config_commands}")
        device.configure(config_commands)

        # Close the connection
        print("Disconnecting from device...")
        device.disconnect()

        # Return a success message
        return {"status": "success", "message": "Configuration applied successfully."}
    except Exception as e:
        # Handle exceptions and provide error information
        return {"error": str(e)}

# Function to learn the configuration using pyATS
def execute_show_run():
    try:
        # Load the testbed
        print("Loading testbed...")
        testbed = loader.load('testbed.yaml')

        # Access the device from the testbed
        device = testbed.devices['Cat8000V']

        # Connect to the device
        print("Connecting to device...")
        device.connect()

        # Use the pyATS learn function to gather the configuration
        print("Learning configuration...")
        learned_config = device.execute('show run brief')

        # Close the connection
        print("Disconnecting from device...")
        device.disconnect()

        # Return the learned configuration as JSON
        return learned_config
    except Exception as e:
        # Handle exceptions and provide error information
        return {"error": str(e)}

# Function to learn the configuration using pyATS
def execute_show_logging():
    try:
        # Load the testbed
        print("Loading testbed...")
        testbed = loader.load('testbed.yaml')

        # Access the device from the testbed
        device = testbed.devices['Cat8000V']

        # Connect to the device
        print("Connecting to device...")
        device.connect()

        # Use the pyATS learn function to gather the configuration
        print("Learning configuration...")
        learned_logs = device.execute('show logging last 250')

        # Close the connection
        print("Disconnecting from device...")
        device.disconnect()

        # Return the learned configuration as JSON
        return learned_logs
    except Exception as e:
        # Handle exceptions and provide error information
        return {"error": str(e)}

# Function to discover available devices in the lab
def discover_lab_devices():
    try:
        # Load the testbed
        testbed = loader.load('testbed.yaml')
        
        devices_info = {}
        for device_name, device in testbed.devices.items():
            devices_info[device_name] = {
                "alias": device.alias,
                "type": device.type,
                "os": device.os,
                "platform": getattr(device, 'platform', 'unknown'),
                "ip": device.connections.cli.ip,
                "port": device.connections.cli.port
            }
        
        return {
            "status": "success",
            "total_devices": len(devices_info),
            "devices": devices_info
        }
    except Exception as e:
        return {"error": f"Failed to discover devices: {str(e)}"}

# Function to test connectivity to lab devices (simple ping test)
def test_lab_connectivity():
    try:
        import subprocess
        import socket
        
        # First, try to load testbed to get device IPs
        try:
            testbed = loader.load('testbed.yaml')
            devices_to_test = {}
            
            for device_name, device in testbed.devices.items():
                devices_to_test[device_name] = {
                    "ip": device.connections.cli.ip,
                    "alias": device.alias,
                    "port": device.connections.cli.port
                }
        except Exception as e:
            return {"error": f"Could not load testbed: {str(e)}"}
        
        connectivity_results = {}
        
        for device_name, device_info in devices_to_test.items():
            try:
                ip = device_info["ip"]
                port = device_info.get("port", 22)
                
                # Test 1: Ping test
                ping_result = subprocess.run(
                    ['ping', '-c', '1', '-W', '3', ip], 
                    capture_output=True, 
                    text=True, 
                    timeout=5
                )
                ping_success = ping_result.returncode == 0
                
                # Test 2: Port connectivity (SSH)
                port_success = False
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(3)
                    result = sock.connect_ex((ip, port))
                    port_success = result == 0
                    sock.close()
                except:
                    port_success = False
                
                # Determine overall status
                if ping_success and port_success:
                    status = "reachable"
                    message = f"✅ Ping and SSH port {port} both accessible"
                elif ping_success:
                    status = "ping_only"
                    message = f"⚠️ Ping works but SSH port {port} not accessible"
                else:
                    status = "unreachable"
                    message = f"❌ No ping response from {ip}"
                
                connectivity_results[device_name] = {
                    "status": status,
                    "ip": ip,
                    "alias": device_info["alias"],
                    "ping_success": ping_success,
                    "ssh_port_open": port_success,
                    "message": message
                }
                
            except Exception as e:
                connectivity_results[device_name] = {
                    "status": "error", 
                    "error": str(e),
                    "ip": device_info.get("ip", "unknown"),
                    "alias": device_info.get("alias", "unknown"),
                    "message": f"❌ Error testing {device_name}: {str(e)}"
                }
        
        # Summary
        total_devices = len(connectivity_results)
        reachable_count = len([r for r in connectivity_results.values() if r["status"] == "reachable"])
        
        return {
            "status": "completed",
            "summary": f"{reachable_count}/{total_devices} devices fully reachable",
            "results": connectivity_results
        }
        
    except Exception as e:
        return {"error": f"Failed to test connectivity: {str(e)}"}

# Function to test a single device connectivity (even simpler)
def test_single_device_connectivity(device_ip: str, device_port: int = 22):
    """Test connectivity to a single device by IP"""
    try:
        import subprocess
        import socket
        
        # Ping test
        ping_result = subprocess.run(
            ['ping', '-c', '1', '-W', '3', device_ip], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        ping_success = ping_result.returncode == 0
        
        # Port test
        port_success = False
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((device_ip, device_port))
            port_success = result == 0
            sock.close()
        except:
            port_success = False
        
        if ping_success and port_success:
            return {
                "status": "reachable",
                "message": f"✅ {device_ip} is reachable on port {device_port}",
                "ping_success": True,
                "port_open": True
            }
        elif ping_success:
            return {
                "status": "ping_only", 
                "message": f"⚠️ {device_ip} responds to ping but port {device_port} is closed",
                "ping_success": True,
                "port_open": False
            }
        else:
            return {
                "status": "unreachable",
                "message": f"❌ {device_ip} is not reachable",
                "ping_success": False,
                "port_open": False
            }
            
    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Error testing {device_ip}: {str(e)}",
            "error": str(e)
        }

# Define the custom tool using the langchain `tool` decorator
@tool
def run_show_command_tool(command: str, device_name: str = None) -> dict:
    """Execute a 'show' command on a specific device in the lab using pyATS and return the parsed JSON output.
    If no device_name is specified, uses the first available Cisco device."""
    return run_show_command(command, device_name)

# New tool for device discovery
@tool
def discover_devices_tool(dummy_input: str = "") -> dict:
    """Discover all available devices in the EVE-NG lab and return their information."""
    return discover_lab_devices()

# New tool for connectivity testing
@tool
def test_connectivity_tool(dummy_input: str = "") -> dict:
    """Test basic network connectivity (ping + SSH port) to all devices in the EVE-NG lab."""
    return test_lab_connectivity()

# New tool for single device connectivity testing
@tool
def test_device_connectivity_tool(input_string: str) -> dict:
    """Test connectivity to a specific device by IP address using ping and port check.
    Usage: test_device_connectivity_tool("192.168.1.1") or test_device_connectivity_tool("192.168.1.1:2222")"""
    
    try:
        # Parse the input to extract IP and optional port
        import re
        
        # Handle various input formats
        input_clean = input_string.strip().strip('"').strip("'")
        
        # Extract IP from formats like 'device_ip="192.168.1.1"' or just '192.168.1.1'
        ip_match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', input_clean)
        if not ip_match:
            return {
                "status": "error",
                "message": f"❌ Could not extract valid IP address from: {input_string}",
                "error": "Invalid IP format"
            }
        
        device_ip = ip_match.group(1)
        
        # Check for port specification (IP:PORT format)
        port = 22  # default
        port_match = re.search(r':(\d+)', input_clean)
        if port_match:
            port = int(port_match.group(1))
        
        return test_single_device_connectivity(device_ip, port)
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Error parsing input '{input_string}': {str(e)}",
            "error": str(e)
        }

# New tool for checking if a command is supported and chaining to run_show_command_tool
@tool
def check_supported_command_tool(command: str, device_name: str = None) -> dict:
    """Check if a command is supported by pyATS based on the command list and return the details."""
    result = check_command_support(command)

    if result.get('status') == 'supported':
        # Automatically run the show command if the command is valid
        closest_command = result['closest_command']
        return {
            "status": "supported",
            "message": f"The closest supported command is '{closest_command}'",
            "action": {
                "next_tool": "run_show_command_tool",
                "input": closest_command,
                "device": device_name
            }
        }
    return result

# Define the custom tool for configuration changes
@tool
def apply_configuration_tool(config_commands: str) -> dict:
    """Apply configuration commands on the router using pyATS."""
    return apply_device_configuration(config_commands)

# Define the custom tool for learning the configuration
@tool
def learn_config_tool(dummy_input: str = "") -> dict:
    """Excute show run brief on the router using pyATS to return the running-configuration."""
    return execute_show_run()

# Define the custom tool for learning the configuration
@tool
def learn_logging_tool(dummy_input: str = "") -> dict:
    """Execute show logging on the router using pyATS and return it as raw text."""
    return execute_show_logging()

# Simple ping tool
@tool
def ping_device_tool(ip_address: str) -> dict:
    """Test if a device responds to ping. Input should be just the IP address like '192.168.1.1'"""
    
    try:
        import subprocess
        import re
        
        # Clean the input and extract IP address
        clean_ip = ip_address.strip().strip('"').strip("'")
        
        # Extract IP using regex to handle any formatting issues
        ip_match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', clean_ip)
        if not ip_match:
            return {
                "status": "error",
                "message": f"❌ Invalid IP address format: {ip_address}",
                "suggestion": "Please provide a valid IP address like '192.168.1.1'"
            }
        
        target_ip = ip_match.group(1)
        
        # Perform ping test
        ping_result = subprocess.run(
            ['ping', '-c', '1', '-W', '3', target_ip], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        
        if ping_result.returncode == 0:
            return {
                "status": "reachable",
                "message": f"✅ {target_ip} is reachable",
                "ip_tested": target_ip,
                "ping_success": True
            }
        else:
            return {
                "status": "unreachable", 
                "message": f"❌ {target_ip} is not responding to ping",
                "ip_tested": target_ip,
                "ping_success": False,
                "ping_output": ping_result.stderr
            }
            
    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "message": f"⏰ Ping to {target_ip} timed out",
            "ip_tested": target_ip,
            "ping_success": False
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Error pinging {clean_ip}: {str(e)}",
            "error": str(e)
        }

# ============================================================
# Define the agent with a custom prompt template
# ============================================================

# Initialize the LLM (using local Ollama installation)
llm = Ollama(model="mistral", temperature=0.7, base_url="http://localhost:11434")

# Create a list of tools
tools = [run_show_command_tool, discover_devices_tool, test_connectivity_tool, test_device_connectivity_tool, ping_device_tool, check_supported_command_tool, apply_configuration_tool, learn_config_tool, learn_logging_tool]

# Render text descriptions for the tools for inclusion in the prompt
tool_descriptions = render_text_description(tools)

template = '''
Assistant is a large language model trained by OpenAI.

Assistant is designed to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on various topics. As a language model, Assistant can generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide coherent and relevant responses.

Assistant is constantly learning and improving. It can process and understand large amounts of text and use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant can generate its text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on various topics.

NETWORK LAB INSTRUCTIONS:

Assistant is a network assistant with the capability to run tools to gather information, configure the network, and provide accurate answers. You are connected to an EVE-NG lab environment with multiple network devices including routers and switches from various vendors.

**Important Guidelines:**

1. **Start by discovering available devices** - Use 'discover_devices_tool' to see what devices are available in the lab.
2. **Test connectivity** - Use 'test_connectivity_tool' to verify which devices are reachable.
3. **For executing commands** - Use 'run_show_command_tool' and specify the device name when working with specific devices.
4. **If unsure about device selection** - Ask the user which device they want to troubleshoot or use the first available device.
5. **Multi-device troubleshooting** - When diagnosing network issues, consider checking multiple devices to understand the full picture.
6. **If you need access to the full running configuration, use the 'learn_config_tool' to retrieve it.**
7. **If you are unsure of the command or if there is ambiguity, use the 'check_supported_command_tool' to verify the command or get a list of available commands.**
8. **For configuration changes, use the 'apply_configuration_tool' with the necessary configuration string (single or multi-line).**
9. **Do NOT use any command modifiers such as pipes (`|`), `include`, `exclude`, `begin`, `redirect`, or any other modifiers.**

**Lab Environment Context:**
- You are working with an EVE-NG virtualized lab
- Devices may include Cisco routers/switches, Juniper devices, and other vendors
- Each device has its own IP address and may require different credentials
- Always identify which device you're working with when providing responses

**Using the Tools:**

- Use 'discover_devices_tool' to see available lab devices
- Use 'test_connectivity_tool' to verify device accessibility  
- Use 'run_show_command_tool' with device_name parameter for specific devices
- Use 'check_supported_command_tool' to verify commands before execution
- If you need to apply a configuration change, use 'apply_configuration_tool'

**TOOLS:**  
{tools}

**Available Tool Names (use exactly as written):**  
{tool_names}

To use a tool, follow this format:

**FORMAT:**
Thought: Do I need to use a tool? Yes  
Action: the action to take, should be one of [{tool_names}]  
Action Input: the input to the action  
Observation: the result of the action
Final Answer: [Answer to the User]  

**Examples:**

To discover lab devices:
Thought: Do I need to use a tool? Yes  
Action: discover_devices_tool  
Action Input: ""  
Observation: [list of available devices]

To execute a command on a specific device:
Thought: Do I need to use a tool? Yes  
Action: run_show_command_tool  
Action Input: command="show ip interface brief", device_name="cisco_router_1"  
Observation: [parsed output here]

To test lab connectivity:
Thought: Do I need to use a tool? Yes  
Action: test_connectivity_tool  
Action Input: ""  
Observation: [connectivity status for all devices]

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

Thought: Do I need to use a tool? No  
Final Answer: [your response here]

Correct Formatting is Essential: Ensure that every response follows the format strictly to avoid errors.

TOOLS:

Assistant has access to the following tools:

- discover_devices_tool: Discover all available devices in the EVE-NG lab
- test_connectivity_tool: Test connectivity to all lab devices
- test_device_connectivity_tool: Test connectivity to a specific device (ping + SSH port)
- ping_device_tool: Simple ping test to check if an IP address is reachable
- run_show_command_tool: Execute show commands on specific devices
- check_supported_command_tool: Finds and returns the closest supported commands
- apply_configuration_tool: Applies configuration commands on network devices
- learn_config_tool: Learns the running configuration from network devices
- learn_logging_tool: Execute show logging on network devices

Begin!

Previous conversation history:

{chat_history}

New input: {input}

{agent_scratchpad}
'''

# Define the input variables separately
input_variables = ["input", "agent_scratchpad", "chat_history"]

# Create the PromptTemplate using the complete template and input variables
prompt_template = PromptTemplate(
    template=template,
    input_variables=input_variables,
    partial_variables={
        "tools": tool_descriptions,
        "tool_names": ", ".join([t.name for t in tools])
    }
)

# Create the ReAct agent using the Ollama LLM, tools, and custom prompt template
agent = create_react_agent(llm, tools, prompt_template)

# ============================================================
# Streamlit App
# ============================================================

# Initialize the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True, verbose=True, max_iterations=50)

# Initialize Streamlit
st.title("Network AI Agent for EVE-NG Lab")
st.write("Ask your network questions and get insights using AI! 🔬 Connected to your EVE-NG lab environment.")

# Display Ollama connection status
display_connection_status()

# Input for user questions
user_input = st.text_input("Enter your question:")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ""

if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Button to submit the question
if st.button("Send"):
    if user_input:
        # Add the user input to the conversation history
        st.session_state.conversation.append({"role": "user", "content": user_input})

        # Invoke the agent with the user input and current chat history
        response = agent_executor.invoke({
            "input": user_input,
            "chat_history": st.session_state.chat_history,
            "agent_scratchpad": ""  # Initialize agent scratchpad as an empty string
        })

        # Check if chaining is needed (i.e., next tool)
        final_response = process_agent_response(response)

        # Extract the final answer
        final_answer = final_response.get('output', 'No answer provided.')

        # Display the question and answer
        st.write(f"**Question:** {user_input}")
        st.write(f"**Answer:** {final_answer}")

        # Add the response to the conversation history
        st.session_state.conversation.append({"role": "assistant", "content": final_answer})

        # Update chat history with the new conversation
        st.session_state.chat_history = "\n".join(
            [f"{entry['role'].capitalize()}: {entry['content']}" for entry in st.session_state.conversation]
        )

# Display the entire conversation history
if st.session_state.conversation:
    st.write("## Conversation History")
    for entry in st.session_state.conversation:
        st.write(f"**{entry['role'].capitalize()}:** {entry['content']}")
