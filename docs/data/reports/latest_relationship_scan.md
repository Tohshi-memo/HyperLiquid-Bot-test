# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T22:52:28.855941+00:00`
- Price records: `672`
- Market context records: `2808`
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

- `market_context_high->unknown_24h` score `2.636` n `142` status `ready` deltaP `3.4697` edge `0.243` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `1.074` n `142` status `ready` deltaP `7.1002` edge `0.1475` maxDD `-3.7602`
- `market_context_high->crypto_alt_24h` score `0.8041` n `142` status `ready` deltaP `0.7923` edge `0.4534` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.6415` n `142` status `ready` deltaP `11.2114` edge `0.2881` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3371` n `142` status `ready` deltaP `13.3009` edge `0.0387` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0154` n `142` status `ready` deltaP `4.4805` edge `0.0445` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0548` n `142` status `ready` deltaP `4.4974` edge `0.0124` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5371` n `142` status `ready` deltaP `-0.5376` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5866` n `142` status `ready` deltaP `1.031` edge `0.0025` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6615` n `142` status `ready` deltaP `-0.5819` edge `-0.0056` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.8184` n `142` status `ready` deltaP `4.6471` edge `0.0401` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8679` n `142` status `ready` deltaP `-2.45` edge `0.0273` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-1.0043` n `142` status `ready` deltaP `3.4769` edge `0.035` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0398` n `142` status `ready` deltaP `2.2673` edge `0.0362` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1703` n `142` status `ready` deltaP `-4.0579` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.594` n `142` status `ready` deltaP `0.0086` edge `-0.0124` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.72` n `142` status `ready` deltaP `-4.8366` edge `-0.0239` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7639` n `142` status `ready` deltaP `13.4232` edge `0.1976` maxDD `-28.7261`
- `market_context_high->index_24h` score `-1.9552` n `142` status `ready` deltaP `-0.6993` edge `-0.0602` maxDD `-2.5127`
- `market_context_high->metal_4h` score `-2.0825` n `142` status `ready` deltaP `0.1439` edge `-0.0129` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
