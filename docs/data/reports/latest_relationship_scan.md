# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T12:07:18.502135+00:00`
- Price records: `672`
- Market context records: `1319`
- Flow alert records: `5708`
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

- `market_context_high->crypto_major_24h` score `16.1772` n `128` status `ready` deltaP `39.1493` edge `1.2003` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.4371` n `128` status `ready` deltaP `13.5417` edge `1.1962` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.702` n `128` status `ready` deltaP `28.3854` edge `0.8209` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.6499` n `128` status `ready` deltaP `29.5139` edge `0.3827` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.4236` n `128` status `ready` deltaP `22.3958` edge `0.5223` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4535` n `157` status `ready` deltaP `12.6534` edge `0.1906` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.9422` n `128` status `ready` deltaP `-0.8681` edge `0.4406` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.2133` n `128` status `ready` deltaP `-13.3681` edge `0.3384` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.9703` n `128` status `ready` deltaP `11.3716` edge `0.0515` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2248` n `157` status `ready` deltaP `3.6671` edge `0.037` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.129` n `157` status `ready` deltaP `5.3315` edge `0.0899` maxDD `-3.7119`
- `market_context_high->metal_4h` score `0.1035` n `157` status `ready` deltaP `13.068` edge `0.0646` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1007` n `157` status `ready` deltaP `5.9127` edge `0.0189` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0954` n `157` status `ready` deltaP `8.6426` edge `0.0034` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5373` n `157` status `ready` deltaP `0.6589` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5977` n `157` status `ready` deltaP `0.697` edge `0.0326` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8229` n `157` status `ready` deltaP `10.6018` edge `0.1927` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9031` n `157` status `ready` deltaP `-1.2167` edge `-0.0056` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.915` n `157` status `ready` deltaP `4.0207` edge `0.083` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9796` n `157` status `ready` deltaP `-2.153` edge `-0.0058` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
