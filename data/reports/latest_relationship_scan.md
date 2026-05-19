# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T12:07:19.573208+00:00`
- Price records: `672`
- Market context records: `1218`
- Flow alert records: `5412`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8777`

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

- `market_context_high->crypto_major_24h` score `18.8859` n `128` status `ready` deltaP `44.3576` edge `1.3913` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.6861` n `128` status `ready` deltaP `2.9345` edge `0.7426` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.1836` n `128` status `ready` deltaP `22.1354` edge `0.6527` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.7365` n `128` status `ready` deltaP `-3.2986` edge `0.6482` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.7257` n `128` status `ready` deltaP `-2.9514` edge `0.5802` maxDD `-6.3373`
- `market_context_high->equity_4h` score `3.0837` n `128` status `ready` deltaP `15.7202` edge `0.2185` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.4317` n `128` status `ready` deltaP `19.2708` edge `0.1828` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.1586` n `128` status `ready` deltaP `19.4444` edge `0.3798` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.1249` n `128` status `ready` deltaP `11.4519` edge `0.0857` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.9478` n `128` status `ready` deltaP `9.6355` edge `0.0612` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.6241` n `128` status `ready` deltaP `9.5996` edge `0.0197` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5427` n `128` status `ready` deltaP `4.8605` edge `0.0497` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `-0.0401` n `128` status `ready` deltaP `-0.5208` edge `0.2731` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.0477` n `128` status `ready` deltaP `9.6697` edge `-0.0074` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1037` n `128` status `ready` deltaP `5.4501` edge `0.0006` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1665` n `128` status `ready` deltaP `5.545` edge `0.1338` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3243` n `128` status `ready` deltaP `0.7953` edge `0.0374` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3903` n `128` status `ready` deltaP `2.8256` edge `0.0077` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.805` n `128` status `ready` deltaP `-2.6104` edge `0.0118` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9074` n `128` status `ready` deltaP `12.2523` edge `-0.0142` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
