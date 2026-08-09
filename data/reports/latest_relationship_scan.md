# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T20:37:33.530019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->metal_24h` score `1.4548` n `116` status `ready` deltaP `7.3995` edge `0.1295` maxDD `-2.2743`
- `market_context_high->equity_24h` score `1.3842` n `116` status `ready` deltaP `2.8856` edge `0.4021` maxDD `-21.1456`
- `market_context_high->commodity_4h` score `1.1656` n `143` status `ready` deltaP `14.8996` edge `0.0651` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7287` n `149` status `ready` deltaP `10.0983` edge `0.0277` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.597` n `116` status `ready` deltaP `20.534` edge `0.0263` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.087` n `116` status `ready` deltaP `5.5496` edge `0.1273` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5124` n `149` status `ready` deltaP `-3.1899` edge `-0.0055` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5207` n `149` status `ready` deltaP `1.5231` edge `-0.004` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.5951` n `149` status `ready` deltaP `-3.1226` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7416` n `143` status `ready` deltaP `2.7791` edge `-0.005` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.9586` n `143` status `ready` deltaP `-1.5254` edge `-0.0092` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9949` n `149` status `ready` deltaP `-0.7576` edge `0.005` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0225` n `143` status `ready` deltaP `-1.9657` edge `-0.0171` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.856` n `149` status `ready` deltaP `-9.3126` edge `-0.0284` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.589` n `143` status `ready` deltaP `-2.0286` edge `-0.0685` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2572` n `149` status `ready` deltaP `-11.755` edge `-0.0606` maxDD `-7.2638`
- `market_context_high->crypto_alt_4h` score `-4.1292` n `143` status `ready` deltaP `-9.0387` edge `-0.1182` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3028` n `116` status `ready` deltaP `1.5685` edge `-0.1196` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.7861` n `116` status `ready` deltaP `-16.6009` edge `-0.2272` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8731` n `149` status `ready` deltaP `-7.047` edge `-0.5644` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
