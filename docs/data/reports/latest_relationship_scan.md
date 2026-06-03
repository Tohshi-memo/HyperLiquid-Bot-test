# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T22:22:26.241083+00:00`
- Price records: `672`
- Market context records: `2806`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.7237` n `142` status `ready` deltaP `3.817` edge `0.248` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `1.074` n `142` status `ready` deltaP `7.1002` edge `0.1475` maxDD `-3.7602`
- `market_context_high->crypto_alt_24h` score `1.0143` n `142` status `ready` deltaP `1.1395` edge `0.4686` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.6271` n `142` status `ready` deltaP `11.2114` edge `0.2869` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3309` n `142` status `ready` deltaP `13.3009` edge `0.0379` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0082` n `142` status `ready` deltaP `4.6302` edge `0.0429` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0446` n `142` status `ready` deltaP `4.6471` edge `0.0127` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5251` n `142` status `ready` deltaP `-0.3879` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.585` n `142` status `ready` deltaP `1.031` edge `0.0027` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6904` n `142` status `ready` deltaP `-0.8813` edge `-0.0073` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.8184` n `142` status `ready` deltaP `4.6471` edge `0.0401` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8499` n `142` status `ready` deltaP `-2.3003` edge `0.0278` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9981` n `142` status `ready` deltaP `3.4769` edge `0.0358` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.083` n `142` status `ready` deltaP `2.2673` edge `0.0326` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1581` n `142` status `ready` deltaP `-3.9054` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.6223` n `142` status `ready` deltaP `-0.2963` edge `-0.014` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6898` n `142` status `ready` deltaP `-4.4894` edge `-0.0237` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7313` n `142` status `ready` deltaP `13.5756` edge `0.1993` maxDD `-28.7261`
- `market_context_high->index_24h` score `-2.0514` n `142` status `ready` deltaP `-1.0465` edge `-0.0659` maxDD `-2.5127`
- `market_context_high->metal_4h` score `-2.0622` n `142` status `ready` deltaP `0.1439` edge `-0.0103` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
