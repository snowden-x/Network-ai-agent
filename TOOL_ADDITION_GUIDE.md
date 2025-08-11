### Tool Addition Guide

This guide explains how to add new operational tools (CLI integrations, host discovery, diagnostics, etc.) to the agent in `react_ai_agent_cisco_ios_xe/react_ai_agent_cisco_ios_xe.py` so the model can select and execute them via the ReAct loop.

### Where tools live

- Tools are defined in `react_ai_agent_cisco_ios_xe/react_ai_agent_cisco_ios_xe.py` as Python functions decorated with `@tool` from LangChain.
- They are registered in the `tools` list and referenced by name in the agent prompt template.

### Conventions and design goals

- **Single-purpose**: Each tool should do one thing well (e.g., ping, traceroute, whois).
- **Input format**: Use a simple, human-friendly input string: positional tokens followed by optional `key=value` pairs. Example: `example.com top_ports=100 service=true`.
- **Parsing**: Reuse `_parse_kv_args(input_str)` to split positional and options cleanly.
- **Safety**: Use `_command_exists()` to verify the system binary is available, and `_run_subprocess()` to execute with `capture_output=True`, returning a structured result.
- **Return type**: Always return a `dict` with keys like `command`, `stdout`, `stderr`, `returncode`, and any task-specific fields (e.g., `reachable`, `connectivity`). On failure, return `{ "error": "..." }`.
- **Portability**: Prefer flags that work across macOS and Linux variants (e.g., `ping -c`, `nc -vz -w`). Avoid root-required modes by default (e.g., prefer `nmap -sT`).
- **No device side-effects**: Host tools should not alter device state. Device configuration is limited to `apply_configuration_tool`.

### Step-by-step: adding a new tool

1) Implement the function

- Place it near other host tools in the file. Use the `@tool` decorator and return a `dict`.

```python
@tool
def mtr_tool(input_text: str) -> dict:
    """Run mtr in report mode. Input: "<host> [count=<n>]". Example: "1.1.1.1 count=50"""
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing host. Usage: '<host> [count=<n>]'"}
    if not _command_exists("mtr"):
        return {"error": "System 'mtr' not found on PATH."}
    host = positional[0]
    count = options.get("count", "20")
    cmd = ["mtr", "--report", "--report-cycles", str(count), host]
    return _run_subprocess(cmd)
```

2) Register the tool

- Add the function to the `tools` list so the agent can call it by name.

```python
tools = [
    # existing tools ...
    mtr_tool,
]
```

3) Update the prompt tool catalog (optional but recommended)

- Extend the “TOOLS” section to include a one-line description and the input format so the model knows when to use it.

```python
- mtr_tool: Path quality analysis via mtr. Input: "<host> [count=<n>]".
```

4) Lint and test

- Ensure no new linter issues: run the project’s linter or rely on the IDE diagnostics.
- Launch the Streamlit app and try natural prompts like: “Run mtr to 1.1.1.1 count=30”.

### Input parsing helper

All new tools should reuse the shared helper to parse inputs:

```python
positional, options = _parse_kv_args(input_text)
```

- Positional tokens are free-form arguments (e.g., target host). Options are `key=value` pairs converted to a dictionary with lowercase keys.

### Subprocess safety helpers

Use these helpers to keep tools robust and consistent:

- `_command_exists(cmd)`: returns `True` if the binary is on PATH.
- `_run_subprocess(cmd_list)`: executes the command and returns `{ command, stdout, stderr, returncode }` or `{ error }`.

This ensures consistent error handling and structured outputs across tools.

### Examples of existing tools (patterns to follow)

- `ping_tool`: reachability test with `count` and `timeout` options.
- `traceroute_tool`: path discovery with optional `max_hops`.
- `dns_lookup_tool`: DNS via `dig` preferred, falls back to `nslookup`.
- `port_check_tool`: TCP port connectivity using `nc` with `-vz -w`.
- `arp_tool`: ARP table and lookups with optional `ip` and `interface`.
- `nmap_scan_tool`: port scanning and service detection with `ports`, `top_ports`, and `service` flags.
- `whois_lookup_tool`: ownership info for IPs/domains.

Use these as reference implementations for parsing, validation, subprocess usage, and return structure.

### System prerequisites

- Some tools require system binaries:
  - **ping**, **traceroute**, **arp**: typically preinstalled on macOS/Linux
  - **dig** (bind utilities) / **nslookup**: commonly available by default
  - **nc** (netcat): usually available; install via package manager if missing
  - **nmap**, **whois**, **mtr**: may require installation

macOS (Homebrew):

```bash
brew install nmap whois mtr
```

Ubuntu/Debian:

```bash
sudo apt-get update && sudo apt-get install -y nmap whois mtr-tiny dnsutils netcat-traditional
```

### Testing in the UI

- Start the app and use natural instructions; the model will pick the right tool based on the prompt catalog:
  - “Ping 8.8.8.8 count=3”
  - “Traceroute to cloudflare.com max_hops=20”
  - “DNS lookup example.com type=MX”
  - “Scan example.com top_ports=100 service=true”
  - “Whois example.org”

### Review checklist

- [ ] Has presence check for required binary
- [ ] Uses `_parse_kv_args` for inputs
- [ ] Uses `_run_subprocess` for execution
- [ ] Returns structured dict with `command`, `stdout`, `stderr`, `returncode` or `error`
- [ ] Added to `tools` list
- [ ] Prompt catalog updated with description and input
- [ ] Lint clean; manual tests pass

### Troubleshooting

- If the tool isn’t being called, verify it is in the `tools` list and appears in the rendered tool names.
- If subprocess fails silently, log the returned `stderr` and `returncode` to diagnose missing flags or permissions.
- If the model makes poor tool choices, clarify the tool’s description and input examples in the prompt catalog.

## Examples

### Connectivity & Discovery Tools

**ping_tool**
```python
@tool
def ping_tool(input_text: str) -> dict:
    """Ping a host to test reachability. Input: "<host> [count=<int>] [timeout=<seconds>]".
    Examples: "8.8.8.8 count=5", "core switch timeout=5"
    """
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing host. Usage: '<host> [count=<int>] [timeout=<seconds>]'"}
    
    host, resolved = _maybe_resolve_host(positional[0])
    count = int(options.get("count", "4"))
    timeout = int(options.get("timeout", "10"))
    
    if not _command_exists("ping"):
        return {"error": "System 'ping' not found on PATH."}
    
    # Platform-specific ping command
    if os.name == "nt":  # Windows
        cmd = ["ping", "-n", str(count), "-w", str(timeout * 1000), host]
    else:  # Unix/Linux/macOS
        cmd = ["ping", "-c", str(count), "-W", str(timeout), host]
    
    result = _run_subprocess(cmd)
    result["reachable"] = result["returncode"] == 0
    
    if resolved:
        result["resolved"] = resolved
    result["host"] = host
    
    return result
```

**traceroute_tool**
```python
@tool
def traceroute_tool(input_text: str) -> dict:
    """Trace the path to a host. Input: "<host> [max_hops=<int>]".
    Examples: "8.8.8.8 max_hops=15", "core switch"
    """
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing host. Usage: '<host> [max_hops=<int>]'"}
    
    host, resolved = _maybe_resolve_host(positional[0])
    max_hops = int(options.get("max_hops", "30"))
    
    if not _command_exists("traceroute"):
        return {"error": "System 'traceroute' not found on PATH."}
    
    cmd = ["traceroute", "-m", str(max_hops), host]
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["host"] = host
    
    return result
```

### Information Gathering Tools

**nmap_scan_tool**
```python
@tool
def nmap_scan_tool(input_text: str) -> dict:
    """Port scanning and service detection using nmap. Input: "<target> [ports=80,443|1-1024] [top_ports=<n>] [service=true]".
    Examples: "example.com ports=443,8443 service=true" or "10.0.0.0/24 top_ports=100"
    """
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing target. Usage: '<target> [ports=...] [top_ports=<n>] [service=true]'"}
    
    if not _command_exists("nmap"):
        return {"error": "System 'nmap' not found on PATH."}
    
    target = positional[0]
    cmd = ["nmap"]
    
    if "ports" in options:
        cmd.extend(["-p", options["ports"]])
    elif "top_ports" in options:
        cmd.extend(["--top-ports", options["top_ports"]])
    
    if options.get("service") == "true":
        cmd.append("-sV")
    
    cmd.append(target)
    result = _run_subprocess(cmd)
    result["target"] = target
    
    return result
```

### SNMP Tools

**snmp_read_tool**
```python
@tool
def snmp_read_tool(input_text: str) -> dict:
    """Read SNMP values from a network device. Input: "<device> <oid> [community=public] [version=2c]".
    Examples: "core switch 1.3.6.1.2.1.1.1.0", "192.168.1.60 1.3.6.1.2.1.1.1.0 community=public version=2c"
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 2:
        return {"error": "Usage: '<device> <oid> [community=public] [version=2c]'"}
    
    device, oid = positional[0], positional[1]
    community = options.get("community", "public")
    version = options.get("version", "2c")
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("snmpget"):
        return {"error": "System 'snmpget' not found. Install net-snmp tools."}
    
    cmd = ["snmpget", "-v", version, "-c", community, host, oid]
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["oid"] = oid
    
    return result
```

**snmp_write_tool**
```python
@tool
def snmp_write_tool(input_text: str) -> dict:
    """Write SNMP values to a network device. Input: "<device> <oid> <type> <value> [community=private] [version=2c]".
    Examples: "core switch 1.3.6.1.2.1.1.6.0 s 'New Location'", "192.168.1.60 1.3.6.1.2.1.1.6.0 s 'New Location' community=private"
    Types: s=string, i=integer, u=unsigned, x=hex, d=decimal, n=null, o=object_id, t=timeticks, a=ipaddress
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 4:
        return {"error": "Usage: '<device> <oid> <type> <value> [community=private] [version=2c]'"}
    
    device, oid, snmp_type, value = positional[0], positional[1], positional[2], positional[3]
    community = options.get("community", "private")
    version = options.get("version", "2c")
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("snmpset"):
        return {"error": "System 'snmpset' not found. Install net-snmp tools."}
    
    cmd = ["snmpset", "-v", version, "-c", community, host, oid, snmp_type, value]
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["oid"] = oid
    result["type"] = snmp_type
    result["value"] = value
    
    return result
```

## Prerequisites for External Commands

Some tools require external system commands to be installed:

- **ping**: Built-in on most systems
- **traceroute**: Built-in on most systems  
- **dig/nslookup**: Built-in on most systems
- **nc (netcat)**: Built-in on most systems
- **arp**: Built-in on most systems
- **nmap**: Install via package manager (`apt install nmap`, `brew install nmap`, etc.)
- **whois**: Install via package manager (`apt install whois`, `brew install whois`, etc.)
- **SNMP tools**: Install net-snmp (`apt install snmp`, `brew install net-snmp`, etc.)
- **SSH tools**: Install Paramiko (`pip install paramiko`) - **Now using Paramiko instead of system SSH!**

## SSH Tools (Paramiko Implementation)

**ssh_connect_tool**
```python
@tool
def ssh_connect_tool(input_text: str) -> dict:
    """Connect to a device via SSH and run a command using Paramiko. Input: "<device> <command> [username=admin] [timeout=30]".
    Examples: "core switch show version", "192.168.1.60 show ip interface brief username=admin"
    Note: Uses credentials from testbed.yaml if available, otherwise prompts for password.
    """
    try:
        import paramiko
    except ImportError:
        return {"error": "Paramiko not installed. Run: pip install paramiko"}
    
    # Parse input and resolve device
    positional, options = _parse_kv_args(input_text)
    device, command = positional[0], positional[1]
    username = options.get("username", "admin")
    timeout = int(options.get("timeout", "30"))
    
    # Resolve device name to IP and get credentials
    host, resolved = _maybe_resolve_host(device)
    password = _get_device_credentials(resolved, username)
    
    try:
        # Create SSH client and connect
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, timeout=timeout)
        
        # Execute command and get output
        stdin, stdout, stderr = ssh.exec_command(command, timeout=timeout)
        exit_status = stdout.channel.recv_exit_status()
        output = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()
        
        ssh.close()
        
        return {
            "status": "success" if exit_status == 0 else "error",
            "exit_code": exit_status,
            "output": output,
            "error": error,
            "device": device,
            "command": command
        }
        
    except paramiko.AuthenticationException:
        return {"error": f"Authentication failed for {username}@{host}"}
    except Exception as e:
        return {"error": f"SSH error: {str(e)}"}
```

**ssh_execute_script_tool**
```python
@tool
def ssh_execute_script_tool(input_text: str) -> dict:
    """Execute multiple commands on a device via SSH using Paramiko. Input: "<device> <commands> [username=admin] [timeout=60]".
    Examples: "core switch 'show version; show ip interface brief; show running-config'"
    Commands should be separated by semicolons.
    """
    try:
        import paramiko
    except ImportError:
        return {"error": "Paramiko not installed. Run: pip install paramiko"}
    
    # Parse input and resolve device
    positional, options = _parse_kv_args(input_text)
    device, commands = positional[0], positional[1]
    username = options.get("username", "admin")
    timeout = int(options.get("timeout", "60"))
    
    # Resolve device name to IP and get credentials
    host, resolved = _maybe_resolve_host(device)
    password = _get_device_credentials(resolved, username)
    
    try:
        # Create SSH client and connect
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, timeout=timeout)
        
        # Execute multiple commands
        stdin, stdout, stderr = ssh.exec_command(commands, timeout=timeout)
        exit_status = stdout.channel.recv_exit_status()
        output = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()
        
        ssh.close()
        
        return {
            "status": "success" if exit_status == 0 else "error",
            "exit_code": exit_status,
            "output": output,
            "error": error,
            "device": device,
            "commands": commands
        }
        
    except Exception as e:
        return {"error": f"SSH error: {str(e)}"}
```

**ssh_file_transfer_tool**
```python
@tool
def ssh_file_transfer_tool(input_text: str) -> dict:
    """Transfer files to/from a device via SFTP using Paramiko. Input: "<device> <direction> <local_path> <remote_path> [username=admin]".
    Examples: "core switch upload config.txt /tmp/config.txt", "192.168.1.60 download /tmp/log.txt log.txt"
    Direction: upload (local to remote) or download (remote to local)
    """
    try:
        import paramiko
    except ImportError:
        return {"error": "Paramiko not installed. Run: pip install paramiko"}
    
    # Parse input and resolve device
    positional, options = _parse_kv_args(input_text)
    device, direction, local_path, remote_path = positional[0], positional[1], positional[2], positional[3]
    username = options.get("username", "admin")
    
    # Resolve device name to IP and get credentials
    host, resolved = _maybe_resolve_host(device)
    password = _get_device_credentials(resolved, username)
    
    try:
        # Create SSH client and connect
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, timeout=30)
        
        # Create SFTP session
        sftp = ssh.open_sftp()
        
        try:
            if direction.lower() == "upload":
                sftp.put(local_path, remote_path)
                message = f"File uploaded: {local_path} -> {remote_path}"
            else:
                sftp.get(remote_path, local_path)
                message = f"File downloaded: {remote_path} -> {local_path}"
                
            return {"status": "success", "message": message}
            
        finally:
            sftp.close()
            ssh.close()
            
    except Exception as e:
        return {"error": f"File transfer failed: {str(e)}"}
```

## Benefits of Paramiko Implementation

**Advantages over subprocess SSH:**
- **Pure Python**: No external SSH client required
- **Better error handling**: Specific exception types (AuthenticationException, SSHException, etc.)
- **Programmatic control**: Full control over SSH sessions
- **Credential management**: Can handle passwords programmatically
- **SFTP support**: Better file transfer than SCP
- **Session persistence**: Keep connections alive for multiple commands
- **Timeout control**: Better timeout handling
- **Cross-platform**: Works consistently across different operating systems

**Key Features:**
- **Auto-add host keys**: `ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())`
- **Credential extraction**: Automatically gets passwords from testbed.yaml
- **Proper cleanup**: Always closes connections in finally blocks
- **Error categorization**: Different error types for different failure modes
- **Output parsing**: Clean stdout/stderr handling with exit codes

## SSH Workflow Examples

### 1. **Device Configuration Backup Workflow**
```
"Backup the running configuration from all core network devices"
```
The agent would:
- Use `ssh_connect_tool` to run `show running-config` on each device
- Use `ssh_file_transfer_tool` to download configs to local storage
- Create timestamped backup files
- Verify all configs were retrieved successfully

### 2. **Multi-Device Command Execution Workflow**
```
"Update the SNMP community string on all switches"
```
The agent would:
- Use `ssh_execute_script_tool` to run multiple commands:
  - `configure terminal`
  - `snmp-server community newcommunity RO`
  - `write memory`
- Execute on each device in sequence
- Verify changes were applied

### 3. **Emergency Configuration Workflow**
```
"Quickly disable all non-essential interfaces during an incident"
```
The agent would:
- Use `ssh_execute_script_tool` to run:
  - `show ip interface brief` (to see current status)
  - `configure terminal`
  - `interface range GigabitEthernet 2/0/1-24`
  - `shutdown`
  - `write memory`
- Execute on affected devices
- Provide status report

### 4. **Network Documentation Workflow**
```
"Gather comprehensive device information for documentation"
```
The agent would:
- Use `ssh_execute_script_tool` on each device to run:
  - `show version`
  - `show ip interface brief`
  - `show ip route`
  - `show vlan`
  - `show running-config | include hostname|domain-name|ntp|snmp`
- Compile information into structured report
- Identify any configuration inconsistencies

### 5. **Troubleshooting Workflow**
```
"Investigate connectivity issues between departments"
```
The agent would:
- Use `ssh_connect_tool` to check interface status on relevant switches
- Use `ssh_execute_script_tool` to run diagnostic commands:
  - `show interface status`
  - `show spanning-tree`
  - `show mac address-table`
  - `show ip arp`
- Analyze outputs for configuration issues
- Provide troubleshooting recommendations


