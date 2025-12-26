# Plan: Add Scope Note (System vs Per-User Service) (Option 2)

## Goal
Clarify the vulnerability scope based on how the daemon is deployed (system service vs per-user), to avoid ambiguity in impact.

## Scope
- Report: `BugBounty/Reports/Linux_DBus_Injection.md`
- Inputs: packaging details or environment observations (systemd unit, dbus service file, install path)

## Checklist
- [ ] Determine deployment model on target (system service vs user service)
- [ ] Confirm service identity (`User=` in dbus service file or systemd unit)
- [ ] Validate dbus policy install location (`/usr/share/dbus-1/system.d/`)
- [ ] Draft a one-paragraph **Scope** note
- [ ] Add conditional language if distribution/packaging may vary
- [ ] Ensure Impact section aligns with the scope note

## Detailed Steps
1. Collect service details:
   - Check `src/platforms/linux/daemon/org.mozilla.vpn.dbus.service.in` (source of truth)
   - Optionally confirm installed unit on target system
2. If system service:
   - State that any local user can trigger a system-wide network reconfiguration.
3. If user service or sandboxed build:
   - State that impact is limited to the user session.
4. Insert a short **Scope** subsection near Impact or Technical Root Cause.

## Deliverable
Report updated with a short **Scope** note explaining system-wide vs user-scoped impact.

## Status
- Owner: Codex
- State: Awaiting environment confirmation or packaging details
