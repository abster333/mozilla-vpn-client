# Bug Hunting Tips & Strategy

## 1. Privilege Escalation (LPE)
The most critical attack surface is the **Daemon**.
*   **Goal**: Execute code as root/system from the unprivileged client user.
*   **Method**: Analyze the IPC (Inter-Process Communication) mechanism.
    *   Look at `src/daemon/rpc`.
    *   Can the client send a malformed message that crashes the daemon? (DoS)
    *   Can the client inject arguments into a command executed by the daemon? (Command Injection)
    *   Can the client trick the daemon into writing to an arbitrary file? (Arbitrary File Write)

## 2. Split Tunneling Bypasses
*   **Goal**: Leak traffic outside the VPN tunnel when it should be encrypted.
*   **Method**:
    *   Enable "Split Tunneling" or "App Exclusions".
    *   Use tools like Wireshark to monitor traffic.
    *   Check if DNS requests leak.
    *   Check if traffic from "excluded" apps accidentally goes through the tunnel, or vice versa.
    *   *Note*: Platform specific (Linux routing tables vs Windows WFP).

## 3. Addon & Resource Loading
*   **Goal**: Load malicious QML/JS or bypass signature verification.
*   **Method**:
    *   Examine `src/addons/`.
    *   How are signatures verified? (`src/signature.cpp`?)
    *   Is there a TOCTOU (Time-of-Check Time-of-Use) vulnerability when loading files?
    *   Can you modify an addon file after signature check but before load?

## 4. Dependency Vulnerabilities
*   **Goal**: Find known CVEs in bundled libraries.
*   **Method**:
    *   Check `3rdparty/` folder.
    *   Compare versions in `CMakeLists.txt` or `README` files against public CVE databases.
    *   Libraries to watch: `libcurl`, `openssl`, `qt`, `wireguard-go`.

## 5. Logic Bugs in State Management
*   **Goal**: Get the app into an inconsistent state (e.g., UI says "Connected" but traffic is unencrypted).
*   **Method**:
    *   Race conditions: Toggle VPN on/off rapidly.
    *   Network changes: Switch Wi-Fi networks, disconnect cable while connecting.
    *   Sleep/Wake cycles.

## Tools
*   **Frida**: For dynamic instrumentation and hooking functions.
*   **Wireshark**: For network traffic analysis.
*   **Qt Creator**: For reading code and debugging.
*   **Ghidra/IDA**: If analyzing the compiled binary (though source is available).
