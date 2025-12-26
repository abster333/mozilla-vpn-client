# Mozilla Bug Bounty Program Information

## Program Overview
Mozilla participates in the [HackerOne](https://hackerone.com/mozilla) bug bounty program. The program encourages security research into Mozilla's products, including the Mozilla VPN Client.

**Program Page:** [https://hackerone.com/mozilla](https://hackerone.com/mozilla)

## Scope
While the specific asset list on HackerOne should be the source of truth, the Mozilla VPN Client is generally considered in-scope as a primary Mozilla product.

**Important Exclusions:**
- Issues found in the "Mozilla VPN Inspector" while in development mode are out of scope.
- Denial of Service (DoS) attacks are generally out of scope.
- Social Engineering / Phishing.
- Issues in third-party libraries *unless* they are incorporated into the shipped client code (which many are in `3rdparty/`).

## Severity & Rewards
Rewards are based on severity and impact.

| Severity | Description | Potential Reward Range |
|----------|-------------|------------------------|
| **Critical** | RCE, Auth Bypass, Secret Disclosure | $3,000 - $10,000+ |
| **High** | Account Takeover, Significant IDOR | Variable |
| **Medium** | Minor XSS, Internal Network Access | Variable |
| **Low** | Minor Leaks, Missing Best Practices | Swag / Hall of Fame |

*Note: Reward amounts are discretionary and subject to change by the Mozilla Bounty Panel.*

## Reporting
- **HackerOne:** [Submit Report](https://hackerone.com/mozilla?type=team)
- **Email:** security@mozilla.com (for non-bounty reports)

## Safe Harbor
Mozilla supports the **Gold Standard Safe Harbor** policy. If you conduct research in good faith and in accordance with the policy, Mozilla will not pursue legal action.
