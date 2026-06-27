# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T09:07:29.540956+00:00`
- Price records: `672`
- Market context records: `4918`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9384`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_1h` score `16.4772` n `104` status `ready` deltaP `10.5539` edge `1.3445` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.9114` n `104` status `ready` deltaP `27.7204` edge `0.7759` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `6.9875` n `104` status `ready` deltaP `22.8776` edge `0.565` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.5691` n `104` status `ready` deltaP `17.9761` edge `0.55` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.7579` n `86` status `ready` deltaP `24.6568` edge `0.3497` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2438` n `104` status `ready` deltaP `8.9822` edge `0.11` maxDD `-1.9651`
- `market_context_high->equity_4h` score `1.0275` n `104` status `ready` deltaP `13.7664` edge `0.1781` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6791` n `104` status `ready` deltaP `9.3223` edge `0.0407` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4501` n `104` status `ready` deltaP `5.6022` edge `0.1242` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3409` n `104` status `ready` deltaP `5.4065` edge `0.065` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.2854` n `104` status `ready` deltaP `6.3047` edge `0.0968` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.1642` n `104` status `ready` deltaP `1.7561` edge `0.0326` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.1664` n `104` status `ready` deltaP `4.1916` edge `0.0167` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.4208` n `104` status `ready` deltaP `8.6422` edge `0.0071` maxDD `-4.4933`
- `market_context_high->index_1h` score `-0.559` n `104` status `ready` deltaP `-1.0479` edge `0.0108` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.8959` n `104` status `ready` deltaP `-2.7322` edge `0.0004` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4777` n `104` status `ready` deltaP `-8.9072` edge `-0.0025` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.9252` n `86` status `ready` deltaP `-6.8557` edge `-0.0137` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9323` n `86` status `ready` deltaP `-9.9281` edge `-0.1576` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.956` n `86` status `ready` deltaP `13.9616` edge `0.0048` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
