# Tested Attack Vectors

## Investigation Log

### Daemon_Command_Injection_Linux_Firewall
- **Hypothesis**: Command injection via `deviceIpv6Address` in `LinuxFirewall::up` -> `NetfilterIsolateIpv6`.
- **Files Inspected**: `src/platforms/linux/daemon/linuxfirewall.cpp`, `linux/netfilter/netfilter.go`
- **Attack Surface**: JSON config passed to `activate` method of daemon.
- **Test Status**: Pass (Safe)
- **Conclusion**: The daemon uses `github.com/google/nftables` Go library which communicates directly with kernel via netlink. It does not use shell commands, so injection is impossible.
- **Date**: 2025-12-23

### Daemon_Path_Traversal_Cgroups
- **Hypothesis**: Path traversal in `WireguardUtilsLinux::excludeCgroup` via malicious cgroup path.
- **Files Inspected**: `src/platforms/linux/daemon/wireguardutilslinux.cpp`, `src/platforms/linux/daemon/apptracker.cpp`
- **Attack Surface**: `vpnDisabledApps` config or running malicious apps.
- **Test Status**: Pass (Safe)
- **Conclusion**: Cgroup paths are constructed from systemd properties and validated mount points. Path traversal is not feasible.
- **Date**: 2025-12-23

### Deep_Link_CSRF_Auth
- **Hypothesis**: Login CSRF via `mozillavpn://login/success?code=...` deep link.
- **Files Inspected**: `src/tasks/authenticate/taskauthenticate.cpp`
- **Attack Surface**: Deep link handler.
- **Test Status**: Pass (Mitigated)
- **Conclusion**: While the `state` parameter is not checked, the use of PKCE (`code_verifier`) prevents an attacker from injecting a code that the client can successfully exchange for a token. The server will reject the code/verifier mismatch.
- **Date**: 2025-12-23

### Linux_Session_Locking_DoS
- **Hypothesis**: A user can lock the VPN session, preventing other users on the same machine from using the VPN even after the first user logs out.
- **Files Inspected**: `src/platforms/linux/daemon/dbusservice.cpp`
- **Attack Surface**: DBus `activate` method and `UserRemoved` signal handling.
- **Test Status**: Fail (Vulnerable)
- **Conclusion**: `DBusService` does not reset `m_sessionUid` or deactivate the VPN when the session owner logs out (via `UserRemoved` signal). This prevents subsequent users from activating or deactivating the VPN, effectively causing a DoS and forcing them to use the previous user's tunnel.
- **Date**: 2025-12-23

### Windows_IPC_Authorization
- **Hypothesis**: Unauthorized connection to Windows daemon named pipe.
- **Files Inspected**: `src/platforms/linux/daemon/windowsdaemonserver.cpp`
- **Attack Surface**: Named pipe connection.
- **Test Status**: Pass (Safe)
- **Conclusion**: The daemon verifies that the connecting client process is the exact same executable file (on disk) as the daemon itself. This prevents unauthorized clients from connecting.
- **Date**: 2025-12-23

