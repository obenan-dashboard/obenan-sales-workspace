# White-label screens

Six screens from a live agency white-label instance: Findri, on its own subdomain
`agent.findri.nl`. They show what an agency's customer sees: the agency's logo, color and web
address on the Obenan dashboard. Use them to explain white-label to agencies and resellers.

**Status: approved.** Seven approved showing Findri's logo and domain in these six screens on
14 October 2026; scope and review date are in the
[public proof register](../../knowledge/proof/PUBLIC_PROOF_REGISTER.md). If the entry no longer
reads `APPROVED`, these files are internal reference only and stay out of customer-facing material.

| File | Screen | SHA-256 |
|---|---|---|
| [findri-01-login.png](findri-01-login.png) | Sign-in page on the agency subdomain | `600c801a619e6670999048f9c38f12c6a8175ddbcf9b0bd836ac7e36aa9f4c2f` |
| [findri-02-get-started.png](findri-02-get-started.png) | Onboarding: connect a Google Business Profile | `b3c17e190198b7e609b0ddd620e8e9ad3c809a7300a723146ec30155fcafa03f` |
| [findri-03-insights.png](findri-03-insights.png) | Insights, "Your month at a glance" | `20f1f5adee1cf45e547ecda2f9087e7e61bcff2cdbe8977d9220899ec1f62385` |
| [findri-04-indexability.png](findri-04-indexability.png) | Indexability overview | `63480f637701c907d64aa6a8e7560f7f389ec1076f15469fe14e235c83b860f8` |
| [findri-05-discoverability.png](findri-05-discoverability.png) | Discoverability overview | `e4d04815cf114690c35aba79d31b4005c74bb921583f19da0d7169b9621788fd` |
| [findri-06-reputation.png](findri-06-reputation.png) | Reputation overview | `4840f1c88eb1f1319b42bfa80fe604648325a2b3821468739cb6924146be7142` |

## Source and masking

Captured by Ceren on 14 October 2026 on the live instance, at Don's request for agency
presentations. Before publication, the following were masked:

- the underlying customer location: its name, address, imagery, metrics and score values
- a competitor business name shown in the comparison
- the signed-in operator's name
- browser extensions, profile picture, update prompts and the bookmarks bar

Score bar lengths remain visible but are not attributable to any business. Everything else is
unchanged, including the product's own gradient headings and cookie notice. Capture metadata
was stripped.

## Use in sales material

- Show the screens whole, as examples of the agency's brand on the dashboard. Pair them with
  the limits in [the White-label section of the product UI overview](../../reference/product-ui/PRODUCT_UI_OVERVIEW.md#white-label).
- Do not unmask, recreate or overlay figures, and do not cite any value from these screens.
  They illustrate the interface, not results.
- Naming Findri as a white-label example is approved for these screens only. Do not infer
  Findri's customers, location count or commercial terms from them.
- Withdrawals update this index, the register and `tests/test_white_label.py` together.
