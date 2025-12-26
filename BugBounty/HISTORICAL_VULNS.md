# Historical Vulnerabilities & Fixes

Analyzing past security fixes can provide insight into recurring bug classes and fragile code paths.

## Notable Git History

*   **VPN-1467: Fix github security vulnerability issues**
    *   Commit: `878373f13`
    *   *Context*: General cleanup of reported vulnerabilities.

*   **VPN-7070: Daemon should link to the Security framework**
    *   Commit: `b67d7f577`
    *   *Context*: macOS specific hardening.

*   **VPN-5992: Allow extensions to request Access to the Proxy Network**
    *   Commit: `c34e159f7`
    *   *Context*: Permission model changes for extensions.

*   **VPN-1137: Fix inverted WPA/RSN security flag checks for Linux**
    *   Commit: `f23bd72b7`
    *   *Context*: Logic error in security checks.

*   **VPN-7399: Fix crash when toggling addons signature debug**
    *   Commit: `549ff1ded`
    *   *Context*: Potential memory safety or logic issue in addon handling.

*   **VPN-7122: Fix view logs when macOS daemon not running**
    *   Commit: `4a6c16f0e`
    *   *Context*: Error handling and state management.

## Recurring Themes

1.  **Logic Errors**: Inverted flags, incorrect state handling (e.g., VPN-1137).
2.  **Permission/Access Control**: Managing what extensions or components can access (e.g., VPN-5992).
3.  **Platform Specifics**: Many fixes are specific to how Android, Linux, or macOS handle permissions and networking.
4.  **Crash Fixes**: Often indicative of underlying memory safety issues (C++) or unhandled exceptions.

## Search Strategy
To find more, run:
```bash
git log --grep="CVE" --grep="security" --grep="vulnerability" --grep="fix" -i
```
Look for commits that touch `src/daemon` or `src/auth`.
