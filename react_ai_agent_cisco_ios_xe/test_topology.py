#!/usr/bin/env python3
"""
Test script for topology resolution logic
"""

import difflib

def resolve_target_device_from_query(query: str, testbed_devices=None) -> tuple[str, str]:
    """
    Intelligently resolve the target device from a user query.
    
    Args:
        query: User's query text
        testbed_devices: dict of device info (optional, will use mock data if not provided)
    
    Returns:
        tuple: (device_name, resolution_method)
    """
    if testbed_devices is None:
        # Mock testbed data for testing
        testbed_devices = {
            'CoreSwitch': {'alias': 'Core Switch (Cisco vIOS)', 'type': 'Switch'},
            'ServersSwitch': {'alias': 'Servers Switch (Cisco vIOS)', 'type': 'Switch'},
            'MarketingSwitch': {'alias': 'Marketing Switch (Cisco vIOS)', 'type': 'Switch'},
            'EngineeringSwitch': {'alias': 'Engineering Switch (Cisco vIOS)', 'type': 'Switch'},
            'AccessPoint': {'alias': 'Access Point (Cisco vIOS L3)', 'type': 'Switch'},
        }
    
    # Normalize query for matching
    query_lower = query.lower().strip()
    
    # Direct device name matches (exact or close)
    device_names = list(testbed_devices.keys())
    for device_name in device_names:
        if device_name.lower() in query_lower:
            return device_name, "exact_name"
    
    # Alias matches
    for device_name, device in testbed_devices.items():
        alias = device.get('alias', '')
        if alias and alias.lower() in query_lower:
            return device_name, "alias"
    
    # Type-based matches
    for device_name, device in testbed_devices.items():
        device_type = device.get('type', '').lower()
        if device_type in query_lower:
            return device_name, "type"
    
    # Location/function-based inference
    if any(word in query_lower for word in ['core', 'main', 'central']):
        for device_name in device_names:
            if 'core' in device_name.lower():
                return device_name, "inference_core"
    
    if any(word in query_lower for word in ['server', 'servers']):
        for device_name in device_names:
            if 'server' in device_name.lower():
                return device_name, "inference_servers"
    
    if any(word in query_lower for word in ['marketing', 'sales']):
        for device_name in device_names:
            if 'marketing' in device_name.lower():
                return device_name, "inference_marketing"
    
    if any(word in query_lower for word in ['engineering', 'dev', 'development']):
        for device_name in device_names:
            if 'engineering' in device_name.lower():
                return device_name, "inference_engineering"
    
    if any(word in query_lower for word in ['access', 'ap', 'wireless']):
        for device_name in device_names:
            if 'access' in device_name.lower():
                return device_name, "inference_access"
    
    # Fuzzy matching for device names
    for device_name in device_names:
        if difflib.SequenceMatcher(None, query_lower, device_name.lower()).ratio() > 0.6:
            return device_name, "fuzzy_match"
    
    # Default to first device if no match found
    if device_names:
        return device_names[0], "default"
    
    return None, "no_devices"

def test_topology_resolution():
    """Test various query patterns"""
    
    test_queries = [
        # Direct device names
        ("show interfaces on CoreSwitch", "CoreSwitch", "exact_name"),
        ("check MarketingSwitch", "MarketingSwitch", "exact_name"),
        
        # Aliases
        ("show ip route on the core switch", "CoreSwitch", "alias"),
        ("configure the marketing switch", "MarketingSwitch", "alias"),
        ("check the servers switch", "ServersSwitch", "alias"),
        
        # Function-based
        ("show interfaces on the core device", "CoreSwitch", "inference_core"),
        ("configure the marketing switch", "MarketingSwitch", "inference_marketing"),
        ("check the engineering switch", "EngineeringSwitch", "inference_engineering"),
        ("show config on the access point", "AccessPoint", "inference_access"),
        
        # Generic queries (should use default)
        ("show interfaces", "CoreSwitch", "default"),
        ("ping 192.168.1.1", "CoreSwitch", "default"),
        
        # Edge cases
        ("", "CoreSwitch", "default"),
        ("just some random text", "CoreSwitch", "default"),
    ]
    
    print("Testing topology resolution logic:")
    print("=" * 50)
    
    for query, expected_device, expected_method in test_queries:
        device, method = resolve_target_device_from_query(query)
        status = "✅" if device == expected_device else "❌"
        print(f"{status} Query: '{query}'")
        print(f"   Expected: {expected_device} ({expected_method})")
        print(f"   Got:      {device} ({method})")
        print()

if __name__ == "__main__":
    test_topology_resolution()
