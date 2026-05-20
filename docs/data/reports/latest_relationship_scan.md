# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T14:37:24.588798+00:00`
- Price records: `672`
- Market context records: `1329`
- Flow alert records: `5739`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `15.4324` n `128` status `ready` deltaP `37.4131` edge `1.1498` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.3909` n `128` status `ready` deltaP `13.3681` edge `1.1935` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6924` n `128` status `ready` deltaP `28.3854` edge `0.8201` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.181` n `128` status `ready` deltaP `27.7778` edge `0.3552` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8942` n `128` status `ready` deltaP `20.6597` edge `0.466` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3641` n `157` status `ready` deltaP `12.1961` edge `0.1862` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.6882` n `128` status `ready` deltaP `-11.6319` edge `0.3664` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `1.4445` n `128` status `ready` deltaP `-2.6042` edge `0.4107` maxDD `-10.1706`
- `market_context_high->fx_24h` score `1.1584` n `128` status `ready` deltaP `13.1077` edge `0.0556` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2003` n `157` status `ready` deltaP `13.6778` edge `0.0686` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1876` n `157` status `ready` deltaP `3.3677` edge `0.0359` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0819` n `157` status `ready` deltaP `4.8742` edge `0.0869` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0399` n `157` status `ready` deltaP `5.1642` edge `0.0161` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0379` n `157` status `ready` deltaP `9.2414` edge `0.0042` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5134` n `157` status `ready` deltaP `0.9583` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6612` n `157` status `ready` deltaP `0.3976` edge `0.0293` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9101` n `157` status `ready` deltaP `-1.8536` edge `-0.002` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-0.9701` n `157` status `ready` deltaP `-1.9652` edge `-0.0092` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-1.0737` n `157` status `ready` deltaP `9.6871` edge `0.1779` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.0927` n `157` status `ready` deltaP `3.2585` edge `0.0653` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
