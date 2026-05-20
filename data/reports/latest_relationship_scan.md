# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T07:52:17.677832+00:00`
- Price records: `672`
- Market context records: `1301`
- Flow alert records: `5656`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8780`

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

- `market_context_high->crypto_major_24h` score `17.1726` n `128` status `ready` deltaP `41.4062` edge `1.2682` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.7625` n `128` status `ready` deltaP `10.7639` edge `1.1585` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5892` n `128` status `ready` deltaP `28.3854` edge `0.8115` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.0542` n `128` status `ready` deltaP `31.5972` edge `0.4025` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0645` n `128` status `ready` deltaP `25.3472` edge `0.5848` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5353` n `155` status `ready` deltaP `12.8806` edge `0.1959` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.2628` n `128` status `ready` deltaP `0.6944` edge `0.4569` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.759` n `128` status `ready` deltaP `-15.9722` edge `0.3179` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.625` n `128` status `ready` deltaP `8.4202` edge `0.0424` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.19` n `157` status `ready` deltaP `3.5174` edge `0.0351` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1579` n `155` status `ready` deltaP `5.5714` edge `0.092` maxDD `-3.7119`
- `market_context_high->metal_4h` score `0.1323` n `155` status `ready` deltaP `13.0979` edge `0.0668` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.103` n `157` status `ready` deltaP `6.0624` edge `0.0182` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0199` n `157` status `ready` deltaP `9.3911` edge `0.0047` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4595` n `157` status `ready` deltaP `1.5571` edge `-0.0031` maxDD `-0.3124`
- `market_context_high->unknown_4h` score `-0.5786` n `155` status `ready` deltaP `3.6517` edge `0.1286` maxDD `-11.1695`
- `market_context_high->crypto_alt_1h` score `-0.5857` n `157` status `ready` deltaP `0.8467` edge `0.0326` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.84` n `157` status `ready` deltaP `-0.4682` edge `-0.0025` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.884` n `155` status `ready` deltaP `10.3187` edge `0.1895` maxDD `-19.5565`
- `market_context_high->commodity_1h` score `-1.0336` n `157` status `ready` deltaP `-2.4524` edge `-0.0083` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
