# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T22:37:28.895130+00:00`
- Price records: `672`
- Market context records: `2807`
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

- `market_context_high->unknown_24h` score `2.6738` n `142` status `ready` deltaP `3.6433` edge `0.245` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `1.0692` n `142` status `ready` deltaP `7.1002` edge `0.1471` maxDD `-3.7602`
- `market_context_high->crypto_alt_24h` score `0.9224` n `142` status `ready` deltaP `0.9659` edge `0.4621` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.6331` n `142` status `ready` deltaP `11.2114` edge `0.2874` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.334` n `142` status `ready` deltaP `13.3009` edge `0.0383` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0074` n `142` status `ready` deltaP `4.4805` edge `0.0426` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.054` n `142` status `ready` deltaP `4.4974` edge `0.0125` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5383` n `142` status `ready` deltaP `-0.5376` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5858` n `142` status `ready` deltaP `1.031` edge `0.0026` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6771` n `142` status `ready` deltaP `-0.7316` edge `-0.0066` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.8246` n `142` status `ready` deltaP `4.6471` edge `0.0393` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8679` n `142` status `ready` deltaP `-2.45` edge `0.0273` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-1.0067` n `142` status `ready` deltaP `3.4769` edge `0.0347` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0614` n `142` status `ready` deltaP `2.2673` edge `0.0344` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1703` n `142` status `ready` deltaP `-4.0579` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.6097` n `142` status `ready` deltaP `-0.1439` edge `-0.0134` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.7049` n `142` status `ready` deltaP `-4.663` edge `-0.0238` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7603` n `142` status `ready` deltaP `13.4232` edge `0.1979` maxDD `-28.7261`
- `market_context_high->index_24h` score `-2.0039` n `142` status `ready` deltaP `-0.8729` edge `-0.0631` maxDD `-2.5127`
- `market_context_high->metal_4h` score `-2.0716` n `142` status `ready` deltaP `0.1439` edge `-0.0115` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
