# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T19:07:21.919439+00:00`
- Price records: `672`
- Market context records: `1348`
- Flow alert records: `5795`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8793`

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

- `market_context_high->crypto_major_24h` score `13.9608` n `128` status `ready` deltaP `34.2881` edge `1.048` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.8207` n `128` status `ready` deltaP `11.8056` edge `1.1564` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4008` n `128` status `ready` deltaP `28.3854` edge `0.7958` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.301` n `128` status `ready` deltaP `24.6528` edge `0.3027` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.0326` n `128` status `ready` deltaP `-8.5069` edge `0.4576` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.2256` n `157` status `ready` deltaP `11.7388` edge `0.1777` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.0928` n `128` status `ready` deltaP `17.5347` edge `0.3841` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4483` n `128` status `ready` deltaP `15.7119` edge `0.0624` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.6668` n `128` status `ready` deltaP `-5.0347` edge `0.3621` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.0399` n `160` status `ready` deltaP `2.601` edge `0.0287` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.0341` n `160` status `ready` deltaP `5.1722` edge `0.0153` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0086` n `157` status `ready` deltaP `4.8742` edge `0.0753` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-0.0093` n `157` status `ready` deltaP `13.068` edge `0.0552` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.1039` n `160` status `ready` deltaP `8.8361` edge `0.0014` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.373` n `160` status `ready` deltaP `2.5786` edge `-0.0027` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.6454` n `160` status `ready` deltaP `-0.2994` edge `0.0097` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-1.0531` n `160` status `ready` deltaP `-1.5157` edge `0.0094` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.2407` n `160` status `ready` deltaP `-4.0943` edge `-0.0258` maxDD `-6.1444`
- `market_context_high->unknown_4h` score `-1.3922` n `157` status `ready` deltaP `1.4292` edge `0.0391` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.4905` n `157` status `ready` deltaP `8.4676` edge `0.1513` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
