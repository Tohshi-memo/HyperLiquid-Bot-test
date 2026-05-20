# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T17:37:26.691484+00:00`
- Price records: `672`
- Market context records: `1342`
- Flow alert records: `5776`
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

- `market_context_high->crypto_major_24h` score `14.4233` n `128` status `ready` deltaP `35.3298` edge `1.0796` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.9845` n `128` status `ready` deltaP `11.9792` edge `1.1689` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4704` n `128` status `ready` deltaP `28.3854` edge `0.8016` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.5523` n `128` status `ready` deltaP `25.6944` edge `0.3167` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `2.5569` n `128` status `ready` deltaP `-9.5486` edge `0.4249` maxDD `-6.8535`
- `market_context_high->equity_24h` score `2.3139` n `128` status `ready` deltaP `18.5764` edge `0.4055` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.246` n `157` status `ready` deltaP `11.7388` edge `0.1794` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.3362` n `128` status `ready` deltaP `14.6702` edge `0.06` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.8218` n `128` status `ready` deltaP `-4.6875` edge `0.3727` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.1217` n `157` status `ready` deltaP `3.218` edge `0.0314` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.0559` n `157` status `ready` deltaP `13.3729` edge `0.0586` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0212` n `157` status `ready` deltaP `5.0145` edge `0.0147` maxDD `-1.6329`
- `market_context_high->index_4h` score `0.0007` n `157` status `ready` deltaP `4.8742` edge `0.0765` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.0607` n `157` status `ready` deltaP `9.2414` edge `0.0023` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4619` n `157` status `ready` deltaP `1.5571` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.753` n `157` status `ready` deltaP `-1.1051` edge `0.0061` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8843` n `157` status `ready` deltaP `-0.5006` edge `0.0167` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.0854` n `157` status `ready` deltaP `-2.8634` edge `-0.018` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.3531` n `157` status `ready` deltaP `1.5817` edge `0.0431` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.5253` n `157` status `ready` deltaP `8.4676` edge `0.1484` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
