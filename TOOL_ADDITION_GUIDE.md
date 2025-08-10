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


