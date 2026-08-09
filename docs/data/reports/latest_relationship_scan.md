# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T19:37:25.492787+00:00`
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

- `market_context_high->equity_24h` score `1.7491` n `113` status `ready` deltaP `2.6472` edge `0.4341` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.6334` n `113` status `ready` deltaP `7.6819` edge `0.1425` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2288` n `143` status `ready` deltaP `15.5094` edge `0.0663` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8518` n `145` status `ready` deltaP `11.5022` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5917` n `113` status `ready` deltaP `20.208` edge `0.0278` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.1428` n `113` status `ready` deltaP `5.6031` edge `0.1341` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.4521` n `145` status `ready` deltaP `-2.0452` edge `-0.0054` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5165` n `145` status `ready` deltaP `1.6064` edge `-0.0042` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6645` n `145` status `ready` deltaP `-4.3816` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7416` n `143` status `ready` deltaP `2.7791` edge `-0.005` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.9598` n `143` status `ready` deltaP `-1.5254` edge `-0.0093` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0248` n `143` status `ready` deltaP `-1.9657` edge `-0.0174` maxDD `-2.7373`
- `market_context_high->equity_1h` score `-1.0706` n `145` status `ready` deltaP `-1.7944` edge `0.0056` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-2.018` n `145` status `ready` deltaP `-10.7381` edge `-0.0324` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.607` n `143` status `ready` deltaP `-2.0286` edge `-0.07` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2759` n `145` status `ready` deltaP `-11.7644` edge `-0.0621` maxDD `-7.2638`
- `market_context_high->crypto_alt_4h` score `-4.1172` n `143` status `ready` deltaP `-9.0387` edge `-0.1172` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3769` n `113` status `ready` deltaP `0.8819` edge `-0.1212` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.1042` n `113` status `ready` deltaP `-17.5163` edge `-0.2476` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.9342` n `145` status `ready` deltaP `-7.0008` edge `-0.5698` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
