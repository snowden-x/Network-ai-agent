import os
import json
import difflib
import subprocess
import shutil
import sys
import streamlit as st
from pyats.topology import loader
from langchain_community.llms import Ollama
from langchain_core.tools import tool, render_text_description
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from genie.libs.parser.utils import get_parser
import yaml

# Function to run any supported show command using pyATS
def run_show_command(command: str):
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

        # Access the selected device from the testbed
        selected_name = st.session_state.get("selected_device")
        if not selected_name or selected_name not in testbed.devices:
            selected_name = next(iter(testbed.devices.keys()))
        device = testbed.devices[selected_name]

        # Connect to the device
        print("Connecting to device...")
        device.connect()

        # Check if a pyATS parser is available for the command
        print(f"Checking if a parser exists for the command: {command}")
        parser = get_parser(command, device)
        if parser is None:
            return {"error": f"No parser available for the command: {command}"}

        # Execute the command and parse the output using Genie
        print(f"Executing '{command}'...")
        parsed_output = device.parse(command)

        # Close the connection
        print("Disconnecting from device...")
        device.disconnect()

        # Return the parsed output (JSON)
        return parsed_output
    except Exception as e:
        # Handle exceptions and provide error information
        return {"error": str(e)}

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

        # Automatically invoke the next tool (run_show_command_tool)
        return agent_executor.invoke({
            "input": command_input,
            "chat_history": st.session_state.chat_history,
            "agent_scratchpad": "",
            "tool": next_tool
        })
    else:
        return response

# Function to apply configuration using pyATS
def apply_device_configuration(config_commands: str):
    try:
        # Load the testbed
        print("Loading testbed...")
        testbed = loader.load('testbed.yaml')

        # Access the selected device from the testbed
        selected_name = st.session_state.get("selected_device")
        if not selected_name or selected_name not in testbed.devices:
            selected_name = next(iter(testbed.devices.keys()))
        device = testbed.devices[selected_name]

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

        # Access the selected device from the testbed
        selected_name = st.session_state.get("selected_device")
        if not selected_name or selected_name not in testbed.devices:
            selected_name = next(iter(testbed.devices.keys()))
        device = testbed.devices[selected_name]

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

        # Access the selected device from the testbed
        selected_name = st.session_state.get("selected_device")
        if not selected_name or selected_name not in testbed.devices:
            selected_name = next(iter(testbed.devices.keys()))
        device = testbed.devices[selected_name]

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

# ============================================================
# Host Connectivity & Discovery helpers
# ============================================================

def _command_exists(command_name: str) -> bool:
    return shutil.which(command_name) is not None

def _parse_kv_args(input_str: str):
    """Parse a simple input format like:
    - "host.example.com count=5 timeout=2"
    - "8.8.8.8"
    - "core switch 1.3.6.1.2.1.1.1.0" (multi-word device names)
    Returns: (positional_args: list[str], options: dict[str, str])
    """
    if not isinstance(input_str, str):
        return [], {}
    
    # Handle quoted strings properly - split on spaces but preserve quoted content
    import shlex
    try:
        tokens = shlex.split(input_str.strip())
    except ValueError:
        # Fallback to simple split if shlex fails
        tokens = input_str.strip().split()
    
    if not tokens:
        return [], {}
    
    # Special handling for multi-word device names in SNMP and other tools
    # Try to find a device name that spans multiple tokens
    device_name = None
    remaining_tokens = []
    
    # Check if first token(s) might be a device name
    for i in range(len(tokens), 0, -1):
        potential_device = " ".join(tokens[:i])
        # Try to resolve this as a device name
        res = _resolve_device(potential_device)
        if res.get("status") == "ok":
            device_name = potential_device
            remaining_tokens = tokens[i:]
            break
    
    # If no device name found, use first token as host/device
    if device_name is None:
        device_name = tokens[0]
        remaining_tokens = tokens[1:]
    
    positional = [device_name]
    options = {}
    
    # Parse remaining tokens for options
    for token in remaining_tokens:
        if "=" in token:
            key, _, value = token.partition("=")
            options[key.strip().lower()] = value.strip()
        else:
            positional.append(token)
    
    return positional, options

def _run_subprocess(cmd: list[str]):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return {
            "command": " ".join(cmd),
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except Exception as exc:
        return {"error": str(exc), "command": " ".join(cmd)}

# ============================================================
# Topology loading and device resolution
# ============================================================

_TOPOLOGY_CACHE = None
_DEVICE_INDEX_CACHE = None

def _normalize_name(name: str) -> str:
    return "".join(ch for ch in name.lower() if ch.isalnum())

def _load_topology() -> dict:
    global _TOPOLOGY_CACHE
    if _TOPOLOGY_CACHE is not None:
        return _TOPOLOGY_CACHE
    candidate_paths = [
        os.environ.get("TOPOLOGY_YAML_PATH"),
        os.path.join(os.getcwd(), "topology.yaml"),
        "/Users/xsnowdev/Documents/Projects/sndvt/sndvt-back/data/topology.yaml",
    ]
    for path in candidate_paths:
        if path and os.path.exists(path):
            try:
                with open(path, "r") as f:
                    _TOPOLOGY_CACHE = yaml.safe_load(f) or {}
                return _TOPOLOGY_CACHE
            except Exception:
                continue
    _TOPOLOGY_CACHE = {}
    return _TOPOLOGY_CACHE

def _build_device_index() -> dict:
    global _DEVICE_INDEX_CACHE
    if _DEVICE_INDEX_CACHE is not None:
        return _DEVICE_INDEX_CACHE
    topo = _load_topology()
    try:
        tb = loader.load('testbed.yaml')
        testbed_devices = tb.devices if tb else {}
    except Exception:
        testbed_devices = {}

    index: dict[str, dict] = {}

    # Collect names from testbed
    for tb_name, dev in testbed_devices.items():
        norm_tb = _normalize_name(tb_name)
        index.setdefault(norm_tb, {}).update({"testbed_name": tb_name})
        alias = getattr(dev, "alias", None)
        if alias:
            norm_alias = _normalize_name(str(alias))
            index.setdefault(norm_alias, {}).update({"testbed_name": tb_name})
            # Also add individual words from alias
            for word in str(alias).lower().split():
                norm_word = _normalize_name(word)
                if norm_word and len(norm_word) > 2:  # Skip very short words
                    index.setdefault(norm_word, {}).update({"testbed_name": tb_name})

    # Collect names and IPs from topology
    devices = (topo or {}).get("devices", {})
    for topo_name, meta in devices.items():
        norm_topo = _normalize_name(topo_name)
        entry = index.setdefault(norm_topo, {})
        entry.update({
            "topology_name": topo_name,
            "ip": meta.get("ip_address"),
            "meta": meta,
        })
        
        # Add individual words from topology name
        for word in topo_name.lower().split():
            norm_word = _normalize_name(word)
            if norm_word and len(norm_word) > 2:  # Skip very short words
                index.setdefault(norm_word, {}).update({
                    "topology_name": topo_name,
                    "ip": meta.get("ip_address"),
                    "meta": meta,
                })
        
        # Try to link to a testbed name by similarity
        if "testbed_name" not in entry:
            # direct exact variants
            for candidate in list(index.keys()):
                # If candidate equals norm_topo and already has a testbed_name
                if candidate == norm_topo and "testbed_name" in index[candidate]:
                    entry["testbed_name"] = index[candidate]["testbed_name"]
                    break
            else:
                # fuzzy match
                try:
                    import difflib as _difflib
                    candidates = [k for k, v in index.items() if "testbed_name" in v]
                    if candidates:
                        best = _difflib.get_close_matches(norm_topo, candidates, n=1, cutoff=0.6)
                        if best:
                            entry["testbed_name"] = index[best[0]]["testbed_name"]
                except Exception:
                    pass

        # Add type/location aliases if present
        for key in ("type", "location"):
            val = meta.get(key)
            if isinstance(val, str):
                norm_val = _normalize_name(val)
                index.setdefault(norm_val, {}).update({
                    "topology_name": topo_name,
                    "ip": meta.get("ip_address"),
                    "meta": meta,
                    **({"testbed_name": entry.get("testbed_name")} if entry.get("testbed_name") else {}),
                })
                # Also add individual words from type/location
                for word in val.lower().split():
                    norm_word = _normalize_name(word)
                    if norm_word and len(norm_word) > 2:
                        index.setdefault(norm_word, {}).update({
                            "topology_name": topo_name,
                            "ip": meta.get("ip_address"),
                            "meta": meta,
                            **({"testbed_name": entry.get("testbed_name")} if entry.get("testbed_name") else {}),
                        })

    _DEVICE_INDEX_CACHE = index
    return _DEVICE_INDEX_CACHE

def _resolve_device(name_or_alias: str) -> dict:
    if not name_or_alias:
        return {"error": "Empty device name"}
    index = _build_device_index()
    
    # Try exact match first
    key = _normalize_name(name_or_alias)
    if key in index:
        return {"status": "ok", **index[key]}
    
    # Try partial matches for multi-word names
    search_terms = name_or_alias.lower().split()
    for term in search_terms:
        norm_term = _normalize_name(term)
        if norm_term in index:
            return {"status": "ok", **index[norm_term], "note": f"Partial match on '{term}'"}
    
    # fuzzy match on full name
    try:
        import difflib as _difflib
        best = _difflib.get_close_matches(key, list(index.keys()), n=1, cutoff=0.6)
        if best:
            match = index[best[0]]
            return {"status": "ok", **match, "note": f"Resolved by similarity from '{name_or_alias}'"}
    except Exception:
        pass
    
    return {"status": "not_found", "query": name_or_alias}

def _maybe_resolve_host(token: str) -> tuple[str, dict | None]:
    # If token is an IP or FQDN, leave as-is; else try topology
    # Check if it's a pure IP address first
    import ipaddress
    try:
        ipaddress.ip_address(token)
        return token, None  # It's a valid IP, no resolution needed
    except ValueError:
        # Not a pure IP, try to resolve as device name
        res = _resolve_device(token)
        if res.get("status") == "ok" and res.get("ip"):
            return res["ip"], res
        # If resolution fails, return original token
        return token, None

# ------------------------------------------------------------
# Tools: ping, traceroute, DNS lookup (dig/nslookup), port check (nc), arp
# ------------------------------------------------------------

@tool
def ping_tool(input_text: str) -> dict:
    """Ping a host to test reachability. Input format: "<host> [count=<int>] [timeout=<seconds>]".
    Example: "8.8.8.8 count=4 timeout=2""" 
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing host. Usage: '<host> [count=<int>] [timeout=<seconds>]'"}
    host, resolved = _maybe_resolve_host(positional[0])
    count = options.get("count", "4")
    # Timeout flags differ across OS; keep it simple and portable
    cmd = ["ping", "-c", str(count), host]
    if not _command_exists("ping"):
        return {"error": "System 'ping' not found on PATH."}
    result = _run_subprocess(cmd)
    result["reachable"] = result.get("returncode", 1) == 0
    if resolved:
        result["resolved"] = resolved
    return result

@tool
def traceroute_tool(input_text: str) -> dict:
    """Trace the route to a host. Input format: "<host> [max_hops=<int>]".
    Example: "cloudflare.com max_hops=25"""
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing host. Usage: '<host> [max_hops=<int>]'"}
    host, resolved = _maybe_resolve_host(positional[0])
    max_hops = options.get("max_hops")
    if not _command_exists("traceroute"):
        return {"error": "System 'traceroute' not found on PATH."}
    cmd = ["traceroute"]
    if max_hops:
        cmd += ["-m", str(max_hops)]
    cmd.append(host)
    res = _run_subprocess(cmd)
    if resolved:
        res["resolved"] = resolved
    return res

@tool
def dns_lookup_tool(input_text: str) -> dict:
    """DNS lookup using dig (preferred) or nslookup. Input: "<name> [type=A|AAAA|CNAME|MX|TXT|PTR|NS]".
    Example: "example.com type=MX"""
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing name. Usage: '<name> [type=A|AAAA|CNAME|MX|TXT|PTR|NS]'"}
    name = positional[0]
    rtype = options.get("type", "A").upper()
    if _command_exists("dig"):
        cmd = ["dig", "+short", name, rtype]
        res = _run_subprocess(cmd)
        return res
    elif _command_exists("nslookup"):
        cmd = ["nslookup", "-querytype=" + rtype, name]
        return _run_subprocess(cmd)
    else:
        return {"error": "Neither 'dig' nor 'nslookup' found on PATH."}

@tool
def port_check_tool(input_text: str) -> dict:
    """Check TCP port connectivity using netcat (nc). Input: "<host> <port> [timeout=<seconds>]".
    Example: "example.com 443 timeout=3"""
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 2:
        return {"error": "Usage: '<host> <port> [timeout=<seconds>]'"}
    host, port = positional[0], positional[1]
    host, resolved = _maybe_resolve_host(host)
    timeout = options.get("timeout", "3")
    if not _command_exists("nc"):
        return {"error": "System 'nc' (netcat) not found on PATH."}
    # BSD netcat (macOS) supports -w for timeout; -z for scan, -v verbose
    cmd = ["nc", "-vz", "-w", str(timeout), host, str(port)]
    result = _run_subprocess(cmd)
    result["connectivity"] = result.get("returncode", 1) == 0
    if resolved:
        result["resolved"] = resolved
    return result

@tool
def arp_tool(input_text: str) -> dict:
    """Show ARP table or lookup a specific IP. Input: "[ip=<ip>] [interface=<iface>]".
    Examples: "" (table), "ip=192.168.1.10", "interface=en0"""
    _, options = _parse_kv_args(input_text)
    if not _command_exists("arp"):
        return {"error": "System 'arp' not found on PATH."}
    ip = options.get("ip")
    interface = options.get("interface")
    if ip:
        cmd = ["arp", "-n", ip]
    else:
        cmd = ["arp", "-a"]
        if interface:
            cmd += ["-i", interface]
    return _run_subprocess(cmd)

@tool
def resolve_device_tool(name: str) -> dict:
    """Resolve a device by human-friendly name/alias (e.g., "core switch"). Returns topology info, IP, and pyATS testbed name if available."""
    return _resolve_device(name)

@tool
def select_device_tool(name: str) -> dict:
    """Resolve a device name and set it as the active target for device commands. Use before running show/config tools.
    Input: "<device name or alias>
    """
    res = _resolve_device(name)
    if res.get("status") == "ok" and res.get("testbed_name"):
        st.session_state.selected_device = res["testbed_name"]
        return {"status": "selected", **res}
    return res

@tool
def list_devices_tool(dummy: str = "") -> dict:
    """List known devices from topology and testbed, including friendly names, IPs, and testbed mapping."""
    index = _build_device_index()
    devices = {}
    for k, v in index.items():
        # prefer canonical topology name as key when available
        name = v.get("topology_name") or v.get("testbed_name") or k
        if name not in devices:
            devices[name] = {
                "ip": v.get("ip"),
                "testbed_name": v.get("testbed_name"),
                "meta": v.get("meta"),
            }
    return {"devices": devices}

# ============================================================
# SNMP tools for network device management
# ============================================================

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

@tool
def snmp_walk_tool(input_text: str) -> dict:
    """Walk SNMP tree from a network device. Input: "<device> <oid> [community=public] [version=2c]".
    Examples: "core switch 1.3.6.1.2.1.2", "192.168.1.60 1.3.6.1.2.1.2 community=public version=2c"
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 2:
        return {"error": "Usage: '<device> <oid> [community=public] [version=2c]'"}
    
    device, oid = positional[0], positional[1]
    community = options.get("community", "public")
    version = options.get("version", "2c")
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("snmpwalk"):
        return {"error": "System 'snmpwalk' not found. Install net-snmp tools."}
    
    cmd = ["snmpwalk", "-v", version, "-c", community, host, oid]
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["oid"] = oid
    
    return result

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

@tool
def snmp_table_tool(input_text: str) -> dict:
    """Get SNMP table from a network device. Input: "<device> <oid> [community=public] [version=2c]".
    Examples: "core switch 1.3.6.1.2.1.2.2", "192.168.1.60 1.3.6.1.2.1.2.2 community=public version=2c"
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 2:
        return {"error": "Usage: '<device> <oid> [community=public] [version=2c]'"}
    
    device, oid = positional[0], positional[1]
    community = options.get("community", "public")
    version = options.get("version", "2c")
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("snmptable"):
        return {"error": "System 'snmptable' not found. Install net-snmp tools."}
    
    cmd = ["snmptable", "-v", version, "-c", community, host, oid]
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["oid"] = oid
    
    return result

@tool
def nmap_scan_tool(input_text: str) -> dict:
    """Port scanning and service detection using nmap. Input: "<target> [ports=80,443|1-1024] [top_ports=<n>] [service=true]".
    Examples: "example.com ports=443,8443 service=true" or "10.0.0.0/24 top_ports=100"""
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing target. Usage: '<target> [ports=...] [top_ports=<n>] [service=true]'"}
    if not _command_exists("nmap"):
        return {"error": "System 'nmap' not found on PATH."}
    target = positional[0]
    ports = options.get("ports")
    top_ports = options.get("top_ports")
    service_flag = options.get("service", "false").lower() in {"true", "1", "yes"}
    # Use TCP connect scan (-sT) to avoid requiring root, skip host discovery (-Pn), no DNS (-n)
    cmd = ["nmap", "-sT", "-Pn", "-n", target]
    if ports:
        cmd += ["-p", ports]
    elif top_ports:
        cmd += ["--top-ports", str(top_ports)]
    if service_flag:
        cmd += ["-sV"]
    return _run_subprocess(cmd)

@tool
def whois_lookup_tool(input_text: str) -> dict:
    """WHOIS lookup for IP or domain ownership info. Input: "<domain_or_ip>".
    Example: "whois example.com" or "whois 8.8.8.8"""
    positional, _ = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Missing target. Usage: '<domain_or_ip>'"}
    if not _command_exists("whois"):
        return {"error": "System 'whois' not found on PATH."}
    target = positional[0]
    cmd = ["whois", target]
    return _run_subprocess(cmd)

# ============================================================
# SSH tools for direct device access
# ============================================================

@tool
def ssh_connect_tool(input_text: str) -> dict:
    """Connect to a device via SSH and run a command. Input: "<device> <command> [username=admin] [timeout=30]".
    Examples: "core switch show version", "192.168.1.60 show ip interface brief username=admin"
    Note: Uses default credentials from testbed.yaml if available.
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 2:
        return {"error": "Usage: '<device> <command> [username=admin] [timeout=30]'"}
    
    device, command = positional[0], positional[1]
    username = options.get("username", "admin")
    timeout = int(options.get("timeout", "30"))
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    # Try to get credentials from testbed if available
    credentials = None
    if resolved and resolved.get("testbed_name"):
        try:
            tb = loader.load('testbed.yaml')
            if tb and resolved["testbed_name"] in tb.devices:
                dev = tb.devices[resolved["testbed_name"]]
                if hasattr(dev, 'credentials') and dev.credentials:
                    credentials = dev.credentials
        except Exception:
            pass
    
    if not _command_exists("ssh"):
        return {"error": "System 'ssh' not found. Install OpenSSH client."}
    
    # Build SSH command
    cmd = ["ssh", "-o", "ConnectTimeout=" + str(timeout), "-o", "StrictHostKeyChecking=no"]
    
    if credentials and hasattr(credentials, 'default') and credentials.default:
        # Use testbed credentials if available
        cmd.extend(["-l", username, host, command])
    else:
        # Fallback to basic SSH (will prompt for password)
        cmd.extend(["-l", username, host, command])
    
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["command"] = command
    result["username"] = username
    
    return result

@tool
def ssh_interactive_tool(input_text: str) -> dict:
    """Start an interactive SSH session to a device. Input: "<device> [username=admin] [timeout=30]".
    Examples: "core switch username=admin", "192.168.1.60"
    This opens an interactive terminal session.
    """
    positional, options = _parse_kv_args(input_text)
    if not positional:
        return {"error": "Usage: '<device> [username=admin] [timeout=30]'"}
    
    device = positional[0]
    username = options.get("username", "admin")
    timeout = int(options.get("timeout", "30"))
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("ssh"):
        return {"error": "System 'ssh' not found. Install OpenSSH client."}
    
    # For interactive sessions, we'll provide instructions rather than executing
    result = {
        "status": "interactive_session",
        "message": f"To connect interactively to {device} ({host}):",
        "command": f"ssh -l {username} {host}",
        "device": device,
        "host": host,
        "username": username
    }
    
    if resolved:
        result["resolved"] = resolved
    
    return result

@tool
def ssh_execute_script_tool(input_text: str) -> dict:
    """Execute multiple commands on a device via SSH. Input: "<device> <commands> [username=admin] [timeout=60]".
    Examples: "core switch 'show version; show ip interface brief; show running-config'", 
              "192.168.1.60 'show version' username=admin"
    Commands should be separated by semicolons.
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 2:
        return {"error": "Usage: '<device> <commands> [username=admin] [timeout=60]'"}
    
    device, commands = positional[0], positional[1]
    username = options.get("username", "admin")
    timeout = int(options.get("timeout", "60"))
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("ssh"):
        return {"error": "System 'ssh' not found. Install OpenSSH client."}
    
    # Build SSH command with multiple commands
    cmd = ["ssh", "-o", "ConnectTimeout=" + str(timeout), "-o", "StrictHostKeyChecking=no", 
           "-l", username, host, commands]
    
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["commands"] = commands
    result["username"] = username
    
    return result

@tool
def ssh_file_transfer_tool(input_text: str) -> dict:
    """Transfer files to/from a device via SCP. Input: "<device> <direction> <local_path> <remote_path> [username=admin]".
    Examples: "core switch upload config.txt /tmp/config.txt", "192.168.1.60 download /tmp/log.txt log.txt username=admin"
    Direction: upload (local to remote) or download (remote to local)
    """
    positional, options = _parse_kv_args(input_text)
    if len(positional) < 4:
        return {"error": "Usage: '<device> <direction> <local_path> <remote_path> [username=admin]'"}
    
    device, direction, local_path, remote_path = positional[0], positional[1], positional[2], positional[3]
    username = options.get("username", "admin")
    
    # Resolve device name to IP if needed
    host, resolved = _maybe_resolve_host(device)
    
    if not _command_exists("scp"):
        return {"error": "System 'scp' not found. Install OpenSSH client."}
    
    if direction.lower() not in ["upload", "download"]:
        return {"error": "Direction must be 'upload' or 'download'"}
    
    # Build SCP command
    if direction.lower() == "upload":
        cmd = ["scp", "-o", "StrictHostKeyChecking=no", local_path, f"{username}@{host}:{remote_path}"]
    else:  # download
        cmd = ["scp", "-o", "StrictHostKeyChecking=no", f"{username}@{host}:{remote_path}", local_path]
    
    result = _run_subprocess(cmd)
    
    if resolved:
        result["resolved"] = resolved
    result["device"] = device
    result["direction"] = direction
    result["local_path"] = local_path
    result["remote_path"] = remote_path
    result["username"] = username
    
    return result

# Define the custom tool using the langchain `tool` decorator
@tool
def run_show_command_tool(command: str) -> dict:
    """Execute a 'show' command on the router using pyATS and return the parsed JSON output."""
    return run_show_command(command)

# New tool for checking if a command is supported and chaining to run_show_command_tool
@tool
def check_supported_command_tool(command: str) -> dict:
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
                "input": closest_command
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

# ============================================================
# Define the agent with a custom prompt template
# ============================================================

# Initialize the LLM (you can replace 'gpt-3.5-turbo' with your desired model)
llm = Ollama(model="mistral", temperature=0.4, base_url="http://localhost:11434")

# Create a list of tools
tools = [
    # Device tools
    run_show_command_tool,
    check_supported_command_tool,
    apply_configuration_tool,
    learn_config_tool,
    learn_logging_tool,
    # Host connectivity & discovery tools
    ping_tool,
    traceroute_tool,
    dns_lookup_tool,
    port_check_tool,
    arp_tool,
    # Basic information gathering
    nmap_scan_tool,
    whois_lookup_tool,
    # Topology & device selection
    resolve_device_tool,
    select_device_tool,
    list_devices_tool,
    # SNMP tools
    snmp_read_tool,
    snmp_walk_tool,
    snmp_write_tool,
    snmp_table_tool,
    # SSH tools
    ssh_connect_tool,
    ssh_interactive_tool,
    ssh_execute_script_tool,
    ssh_file_transfer_tool,
]

# Render text descriptions for the tools for inclusion in the prompt
tool_descriptions = render_text_description(tools)

template = '''
Assistant is a large language model trained by OpenAI.

Assistant is designed to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on various topics. As a language model, Assistant can generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide coherent and relevant responses.

Assistant is constantly learning and improving. It can process and understand large amounts of text and use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant can generate its text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on various topics.

NETWORK INSTRUCTIONS:

Assistant is a network assistant with the capability to run tools to gather information, configure the network, and provide accurate answers. You MUST use the provided tools for checking interface statuses, retrieving the running configuration, configuring settings, connectivity discovery (ping, traceroute, DNS), port reachability, ARP table lookups, device resolution via topology, or finding which commands are supported.

**Important Guidelines:**

1. **If you are certain of the command for retrieving information, use the 'run_show_command_tool' to execute it.**
2. **If you need access to the full running configuration, use the 'learn_config_tool' to retrieve it.**
3. **If you are unsure of the command or if there is ambiguity, use the 'check_supported_command_tool' to verify the command or get a list of available commands.**
4. **If the 'check_supported_command_tool' finds a valid command, automatically use 'run_show_command_tool' to run that command.**
5. **For configuration changes, use the 'apply_configuration_tool' with the necessary configuration string (single or multi-line).**
6. **Do NOT use any command modifiers such as pipes (`|`), `include`, `exclude`, `begin`, `redirect`, or any other modifiers.**
7. **If the command is not recognized, always use the 'check_supported_command_tool' to clarify the command before proceeding.**
 8. **For connectivity testing, use 'ping_tool' (basic reachability), 'traceroute_tool' (path and latency), 'dns_lookup_tool' (DNS resolution), 'port_check_tool' (TCP port connectivity), and 'arp_tool' (Layer 2 address resolution).**
 9. **To target a device by human-friendly name (e.g., "core switch"), use 'resolve_device_tool' and 'select_device_tool' to set the active device before running show or config commands.**
 10. **For SNMP operations, use 'snmp_read_tool' (single OID read), 'snmp_walk_tool' (tree walk), 'snmp_write_tool' (write values), and 'snmp_table_tool' (table retrieval). Use 'public' community for reads and 'private' community for writes.**
 11. **For direct device access, use 'ssh_connect_tool' (run single command), 'ssh_execute_script_tool' (run multiple commands), 'ssh_file_transfer_tool' (file transfer), or 'ssh_interactive_tool' (interactive session). These provide direct SSH access to devices.**

**Using the Tools:**

- If you are confident about the command to retrieve data, use the 'run_show_command_tool'.
- If you need access to the full running configuration, use 'learn_config_tool'.
- If there is any doubt or ambiguity, always check the command first with the 'check_supported_command_tool'.
- If you need to apply a configuration change, use 'apply_configuration_tool' with the appropriate configuration commands.

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

If the first tool provides a valid command, you MUST immediately run the 'run_show_command_tool' without waiting for another input. Follow the flow like this:

Example:

Thought: Do I need to use a tool? Yes  
Action: check_supported_command_tool  
Action Input: "show ip access-lists"  
Observation: "The closest supported command is 'show ip access-list'."

Thought: Do I need to use a tool? Yes  
Action: run_show_command_tool  
Action Input: "show ip access-list"  
Observation: [parsed output here]

If you need access to the full running configuration:

Example:

Thought: Do I need to use a tool? Yes  
Action: learn_config_tool  
Action Input: (No input required)  
Observation: [configuration here]

If you need to apply a configuration:

Example:

Thought: Do I need to use a tool? Yes  
Action: apply_configuration_tool  
Action Input: """  
interface loopback 100  
description AI Created  
ip address 10.10.100.100 255.255.255.0  
no shutdown  
"""  
Observation: "Configuration applied successfully."

If you need to read SNMP values:

Example:

Thought: Do I need to use a tool? Yes  
Action: snmp_read_tool  
Action Input: "core switch 1.3.6.1.2.1.1.1.0"  
Observation: [SNMP output here]

If you need to write SNMP values:

Example:

Thought: Do I need to use a tool? Yes  
Action: snmp_write_tool  
Action Input: "core switch 1.3.6.1.2.1.1.6.0 s 'New Location' community=private"  
Observation: [SNMP write result here]

If you need to run commands via SSH:

Example:

Thought: Do I need to use a tool? Yes  
Action: ssh_connect_tool  
Action Input: "core switch show version"  
Observation: [SSH command output here]

If you need to execute multiple commands via SSH:

Example:

Thought: Do I need to use a tool? Yes  
Action: ssh_execute_script_tool  
Action Input: "core switch 'show version; show ip interface brief; show running-config'"  
Observation: [Multiple command outputs here]

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

Thought: Do I need to use a tool? No  
Final Answer: [your response here]

Correct Formatting is Essential: Ensure that every response follows the format strictly to avoid errors.

TOOLS:

Assistant has access to the following tools:

- check_supported_command_tool: Finds and returns the closest supported commands.
- run_show_command_tool: Executes a supported 'show' command on the network device and returns the parsed output.
- apply_configuration_tool: Applies the provided configuration commands on the network device.
- learn_config_tool: Learns the running configuration from the network device and returns it as JSON.
- learn_logging_tool: Retrieves recent logging output from the device.
- ping_tool: Ping a host to test reachability from the agent host. Input: "<host> [count=<int>] [timeout=<seconds>]".
- traceroute_tool: Trace the path to a host from the agent host. Input: "<host> [max_hops=<int>]".
- dns_lookup_tool: DNS resolution via dig or nslookup. Input: "<name> [type=A|AAAA|CNAME|MX|TXT|PTR|NS]".
- port_check_tool: Check TCP port connectivity using netcat. Input: "<host> <port> [timeout=<seconds>]".
- arp_tool: Show ARP table or lookup an IP. Input: "[ip=<ip>] [interface=<iface>]".
 - nmap_scan_tool: Port scanning and service detection using nmap. Input: "<target> [ports=80,443|1-1024] [top_ports=<n>] [service=true]".
 - whois_lookup_tool: WHOIS lookup for IP or domain ownership info. Input: "<domain_or_ip>".
 - resolve_device_tool: Resolve device by friendly name/alias to topology info and pyATS testbed name.
 - select_device_tool: Set the active device (in session) by friendly name before running device commands.
 - list_devices_tool: List known devices from topology and testbed with IPs and mappings.
 - snmp_read_tool: Read SNMP values from a network device. Input: "<device> <oid> [community=public] [version=2c]".
 - snmp_walk_tool: Walk SNMP tree from a network device. Input: "<device> <oid> [community=public] [version=2c]".
 - snmp_write_tool: Write SNMP values to a network device. Input: "<device> <oid> <type> <value> [community=private] [version=2c]".
 - snmp_table_tool: Get SNMP table from a network device. Input: "<device> <oid> [community=public] [version=2c]".
 - ssh_connect_tool: Connect to a device via SSH and run a command. Input: "<device> <command> [username=admin] [timeout=30]".
 - ssh_interactive_tool: Start an interactive SSH session to a device. Input: "<device> [username=admin] [timeout=30]".
 - ssh_execute_script_tool: Execute multiple commands on a device via SSH. Input: "<device> <commands> [username=admin] [timeout=60]".
 - ssh_file_transfer_tool: Transfer files to/from a device via SCP. Input: "<device> <direction> <local_path> <remote_path> [username=admin]".

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
st.title("ReAct AI Agent with pyATS and LangChain")
st.write("Ask your network questions and get insights using AI!")

# Load testbed once to populate device selector
try:
    tb_for_ui = loader.load('testbed.yaml')
    device_names = list(tb_for_ui.devices.keys())
except Exception:
    tb_for_ui = None
    device_names = []

if "selected_device" not in st.session_state and device_names:
    st.session_state.selected_device = device_names[0]

selected_device = st.selectbox(
    "Target device (from testbed.yaml)",
    options=device_names,
    index=device_names.index(st.session_state.selected_device) if device_names and st.session_state.get("selected_device") in device_names else 0,
)
st.session_state.selected_device = selected_device

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
