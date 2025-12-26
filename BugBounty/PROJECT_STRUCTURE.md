# Project Structure & Architecture

The Mozilla VPN Client is a cross-platform application built using **Qt (C++ & QML)**. It uses a split architecture with a privileged daemon/service and an unprivileged UI client.

## Key Directories

| Directory | Description |
|-----------|-------------|
| `src/` | **Core Application Logic**. Contains the C++ backend code. |
| `src/daemon/` | **Privileged Service**. This runs as root/system and handles network manipulation. **High Value Target**. |
| `src/ui/` | UI Logic (C++ models for QML). |
| `src/addons/` | Addon management (themes, languages). |
| `android/` | Android-specific build files and Java/Kotlin bridges. |
| `ios/` | iOS-specific code (Swift/Obj-C) and Packet Tunnel Provider. |
| `macos/` | macOS-specific code (Helper tool, XPC). |
| `windows/` | Windows-specific code. |
| `linux/` | Linux-specific code (Polkit policies, systemd units). |
| `3rdparty/` | External dependencies (WireGuard, c-ares, etc.). Check for known CVEs here. |
| `tests/` | Unit and integration tests. Good for understanding expected behavior. |

## Architecture Overview

1.  **Client (UI)**:
    *   Written in QML (Frontend) and C++ (Backend Logic).
    *   Runs with user privileges.
    *   Communicates with the Daemon via IPC (Inter-Process Communication).

2.  **Daemon (Service/Helper)**:
    *   Written in C++.
    *   Runs with **Root/System privileges**.
    *   Responsible for:
        *   Configuring the network interface (WireGuard).
        *   Setting firewall rules.
        *   Managing routing tables.
    *   **Security Critical**: Any vulnerability here can lead to Local Privilege Escalation (LPE).

3.  **WireGuard**:
    *   The underlying VPN protocol implementation.
    *   Found in `3rdparty/wireguard-go` (userspace) or kernel modules depending on OS.

## Attack Surface

*   **IPC Interface**: The communication channel between the unprivileged Client and privileged Daemon.
*   **Update Mechanism**: How the app updates itself (`src/update`).
*   **Addon System**: Loading of external resources (`addons/`).
*   **Network Parsing**: Handling of malicious network packets or DNS responses.
