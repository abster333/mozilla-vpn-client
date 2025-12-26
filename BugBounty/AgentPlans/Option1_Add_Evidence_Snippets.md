# Plan: Add Evidence Snippets to Report (Option 1)

## Goal
Add concrete, reproducible evidence output to the report to back the impact claim (routes/DNS/WireGuard state) after running the PoC.

## Scope
- Report: `BugBounty/Reports/Linux_DBus_Injection.md`
- Evidence sources: `wg show`, `ip route`, `resolvectl status` (or `/etc/resolv.conf` if systemd-resolved is not used)

## Checklist
- [ ] Run PoC on target system and capture timestamps
- [ ] Capture `wg show` output after PoC (confirm peer/endpoint)
- [ ] Capture `ip route` (and `ip -6 route` if applicable) after PoC
- [ ] Capture DNS state (`resolvectl status` or `/etc/resolv.conf`)
- [ ] Redact any sensitive identifiers (real server IPs, keys, hostnames) if needed
- [ ] Insert a new **Evidence** section into the report with short excerpts
- [ ] Note command context (user, host, date/time) in one short line
- [ ] Re-read the report for consistency (Impact + PoC + Evidence alignment)

## Detailed Steps
1. Run the PoC:
   - `python3 tests/security/poc_linux_dbus_injection.py`
2. Immediately capture evidence:
   - `wg show`
   - `ip route` and `ip -6 route`
   - `resolvectl status` (or `cat /etc/resolv.conf`)
3. Save outputs to a scratch file for editing/redaction.
4. Add a new **Evidence** subsection under **Proof of Concept** or **Impact**.
5. Insert short, relevant excerpts (not full dumps).
6. Verify the evidence matches the attack path and configuration values in the PoC.

## Deliverable
Updated report with a concise **Evidence** section showing routes and DNS changes consistent with the injected config.

## Status
- Owner: Codex
- State: Ready to execute once evidence outputs are provided
