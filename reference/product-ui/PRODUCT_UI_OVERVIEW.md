# Product UI overview

Public-safe orientation for sales materials. This is not an engineering specification,
security audit or guarantee that every capability is enabled for every customer.

## Main surfaces

| Surface | What it helps a customer do | Claim boundary |
|---|---|---|
| Insights | See portfolio-level signals and areas needing attention. | Describe only metrics verified for the customer's account. |
| Indexability | Review and govern business information across locations and supported destinations. | Coverage varies by destination, country and connection status. |
| Discoverability | Review search, content and visibility signals. | Never promise a ranking position or permanent recommendation. |
| Reputation | Monitor reviews, themes, response activity and reputation signals. | Never expose reviewer or staff identities in a sales deliverable. |
| Posts and campaigns | Coordinate approved content and campaign activity across locations. | Availability and publishing cadence depend on account configuration and connected channels. |
| Reports | Prepare scheduled or on-demand reporting for permitted users. | Confirm the account's enabled report types before promising them. |
| Tasks and automation | Coordinate recurring operational work and exception handling. | Describe an action as automated only when the customer's account is configured for it. |
| Account administration | Organize permitted users, roles, locations and groups. | Do not disclose another customer's account structure or access model. |
| AI assistant access | Query permitted portfolio information through compatible governed workflows. | Access depends on authentication, permissions, connected data and approval controls. |

## White-label

Agencies and resellers can run the dashboard under their own brand. Masked screens from a live
agency instance, with their approval status, are in
[the white-label screen index](../../assets/white-label/README.md).

| What the agency's customers see | Claim boundary |
|---|---|
| The agency's own subdomain, logo, favicon and browser-tab name | Set up per agency at go-live. The agency must be able to manage DNS for its domain. |
| The agency's brand color | In the captured instance it shows on the logo and the active navigation. Product-wide styling, such as gradient headings and score bars, stays the same. Check the live instance before promising a specific recolored element. |
| The same product, functions and data | White-label changes presentation, not capability. |

Obenan stays visible in three places. Say so before the agency asks:

- **Google connection.** Google's own consent screen names Obenan, because the connection runs
  through Obenan's registered Google app. Google requires this; it cannot be rebranded.
- **Terms and Privacy Policy.** The dashboard shows Obenan's own Terms and Privacy Policy, not
  the agency's. This follows Google's user-data policy and Obenan's legal review.
- **Email.** As of October 2026, password resets and notifications are sent by Obenan, not the
  agency. Branded email is not available; do not promise a date.

Never tell an agency its customers will never know Obenan is behind the dashboard. Say the
dashboard carries the agency's brand, then name the three exceptions.

## How to use this file

- Use this overview to explain the product in plain language.
- Verify live availability through approved product sources before making a commitment.
- Keep route maps, implementation details, authentication behavior, vulnerabilities and
  customer-specific counts in restricted engineering or customer workspaces.
- If a requested answer requires internal implementation detail, stop and route it to the
  responsible Obenan owner.
