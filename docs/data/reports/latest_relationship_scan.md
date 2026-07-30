# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T19:52:45.820356+00:00`
- Price records: `672`
- Market context records: `8442`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5785`

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

- `news_risk_high->unknown_24h` score `6258.4325` n `52` status `ready` deltaP `44.0438` edge `521.2845` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.1475` n `52` status `ready` deltaP `23.0183` edge `0.3352` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.5623` n `55` status `ready` deltaP `19.7551` edge `0.1127` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1125` n `52` status `ready` deltaP `18.75` edge `0.0701` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5556` n `55` status `ready` deltaP `12.3952` edge `0.0904` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.3989` n `55` status `ready` deltaP `10.6206` edge `0.0855` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1201` n `52` status `ready` deltaP `3.8813` edge `0.1871` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9681` n `52` status `ready` deltaP `13.2153` edge `0.1752` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.3259` n `55` status `ready` deltaP `9.5073` edge `0.0065` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.1775` n `55` status `ready` deltaP `4.1181` edge `0.0162` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.011` n `52` status `ready` deltaP `1.841` edge `0.0336` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.2562` n `55` status `ready` deltaP `2.0223` edge `0.0055` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3028` n `52` status `ready` deltaP `6.4845` edge `0.0137` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9173` n `55` status `ready` deltaP `-6.2575` edge `-0.0395` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6665` n `52` status `ready` deltaP `-27.7244` edge `-0.0552` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.5052` n `52` status `ready` deltaP `-27.1224` edge `-0.1972` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.8132` n `52` status `ready` deltaP `-34.7088` edge `-0.226` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7426` n `52` status `ready` deltaP `-12.7804` edge `-0.3827` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.0743` n `52` status `ready` deltaP `-29.6341` edge `-0.3417` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-38.3794` n `52` status `ready` deltaP `-27.7244` edge `-1.2259` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
