# Network AI Agent for EVE-NG Lab

A powerful AI-driven network troubleshooting and automation agent that connects to your EVE-NG virtualized lab environment. This agent can discover devices, execute commands, analyze network issues, and provide intelligent troubleshooting guidance across multiple network vendors.

## Prerequisites

- Docker and Docker Compose installed on your system
- EVE-NG server with running network devices
- SSH access to your EVE-NG lab devices
- Valid pyATS testbed file configured for your lab environment

## Features

- 🔬 **EVE-NG Lab Integration** - Connects directly to your virtualized lab environment
- 🤖 **AI-Powered Analysis** - Uses ReAct (Reasoning + Acting) framework for intelligent troubleshooting
- 🌐 **Multi-Vendor Support** - Works with Cisco, Juniper, Arista, and other network devices
- 📊 **Structured Data Parsing** - Leverages pyATS for reliable command output parsing
- 💬 **Natural Language Interface** - Ask questions in plain English
- 🔧 **Configuration Management** - Can both diagnose issues and apply fixes
- 📋 **Device Discovery** - Automatically discovers and tests connectivity to lab devices

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/snowden-x/Network-ai-agent
cd Network-ai-agent
```

### 2. Configure Your EVE-NG Lab

Copy the lab configuration template and update it with your EVE-NG lab details:

```bash
cp react_ai_agent_cisco_ios_xe/lab_config_template.yaml react_ai_agent_cisco_ios_xe/testbed.yaml
```

Edit `testbed.yaml` and update:
- Device IP addresses (your EVE-NG management network IPs)
- Device credentials (usernames and passwords)
- Device types and platforms
- Add/remove devices based on your actual lab topology

### 3. Validate Your Lab Configuration

Test connectivity to your EVE-NG devices:

```bash
# Optional: Validate testbed file syntax
pyats validate testbed react_ai_agent_cisco_ios_xe/testbed.yaml
```

### 4. Start the Application

```bash
docker-compose up
```

Wait for both containers to start:
- Ollama container will download the AI model (first run takes a few minutes)
- Agent container will start the web interface

### 5. Access the Application

Open your browser and visit: **http://localhost:8501**

## Using the Agent

### Initial Setup Commands

When you first access the agent, try these commands to verify your lab setup:

```
"Discover all devices in the lab"
"Test connectivity to all lab devices"  
"Show me the interface status on cisco_router_main"
```

### Example Troubleshooting Scenarios

- **Connectivity Issues**: *"I can't reach 10.1.1.100 from the main router, can you help diagnose?"*
- **Interface Problems**: *"Check if all interfaces are up on cisco_switch_core"*
- **Routing Issues**: *"Show me the routing table and OSPF neighbors on all routers"*
- **Multi-device Analysis**: *"Compare the CDP neighbors on all Cisco devices"*

### Advanced Usage

- **Device-specific queries**: *"Check the spanning tree status on cisco_switch_access"*
- **Configuration analysis**: *"Show me the running config on juniper_router_branch"*
- **Cross-vendor comparison**: *"Compare interface utilization across all devices"*

## Lab Configuration Guide

### Supported Device Types

| Vendor | OS Type | Platform Examples | Notes |
|--------|---------|-------------------|--------|
| Cisco | `iosxe`, `ios` | CSR1000v, Cat9300, ISR4000 | Full pyATS support |
| Juniper | `junos` | vMX, vSRX, vQFX | Basic support via SSH |
| Arista | `eos` | vEOS, DCS-7050 | Basic support via SSH |
| MikrotikOS | `routeros` | CHR, RB series | Basic support via SSH |
| pfSense | `freebsd` | pfSense VM | Basic support via SSH |

### EVE-NG Network Setup

1. **Management Network**: Ensure all devices have management IPs accessible from your Docker host
2. **SSH Access**: Enable SSH on all devices with proper credentials
3. **Firewall Rules**: Allow SSH (port 22) from Docker container to lab devices
4. **DNS/Hosts**: Consider using IP addresses instead of hostnames for reliability

### Device Credentials

Update credentials in `testbed.yaml` for each device:

```yaml
credentials:
  default:
    username: "your_username"
    password: "your_password"
```

## Troubleshooting

### Common Issues

1. **Connection Timeout**
   - Verify device IPs are correct and reachable
   - Check SSH is enabled on devices
   - Verify credentials are correct

2. **Parser Errors**
   - Some commands may not have pyATS parsers
   - Check the supported commands list
   - Use basic show commands for best results

3. **Device Discovery Fails**
   - Ensure testbed.yaml syntax is correct
   - Verify all device IPs are in your EVE-NG management network
   - Check Docker container can reach EVE-NG network

### Testing Connectivity

Use these commands in the agent to test your setup:

```
"Test connectivity to all devices"
"Show me all available devices"
"Check device cisco_router_main status"
```

## Stopping the Application

```bash
docker-compose down
```

## Directory Structure

```
Network-ai-agent/
├── docker-compose.yml          # Docker services configuration
├── react_ai_agent_cisco_ios_xe/
│   ├── react_ai_agent_cisco_ios_xe.py  # Main agent application
│   ├── testbed.yaml            # Your EVE-NG lab configuration
│   ├── lab_config_template.yaml # Configuration template
│   └── commands.json           # Supported pyATS commands
├── docker/
│   └── Dockerfile              # Agent container build
├── ollama/
│   └── Dockerfile              # AI model container build
└── scripts/
    ├── init.sh                 # Ollama initialization
    └── startup.sh              # Agent startup script
```

## Contributing

This project is designed to be extensible for multiple network vendors and use cases. Contributions welcome for:

- Additional vendor support
- Enhanced troubleshooting workflows  
- Multi-device correlation analysis
- Network documentation integration

## Support

For issues specific to this EVE-NG integration, please open an issue in this repository.

For EVE-NG related questions, consult the [EVE-NG documentation](https://www.eve-ng.net/).

---

**Note**: This agent is designed for lab environments. Exercise caution when using with production networks.

