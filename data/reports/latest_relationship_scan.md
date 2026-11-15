# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T05:37:37.933350+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9730`

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

- `market_context_high->unknown_24h` score `549.5853` n `66` status `ready` deltaP `2.4263` edge `45.7826` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.724` n `53` status `ready` deltaP `47.1045` edge `3.2336` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.9703` n `66` status `ready` deltaP `42.1302` edge `3.0375` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.9488` n `66` status `ready` deltaP `57.8121` edge `2.218` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.2184` n `53` status `ready` deltaP `43.1052` edge `2.6295` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.7176` n `53` status `ready` deltaP `38.9075` edge `0.8301` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.4605` n `66` status `ready` deltaP `44.244` edge `0.3359` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2216` n `53` status `ready` deltaP `49.74` edge `0.2702` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.6255` n `53` status `ready` deltaP `14.473` edge `1.2035` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.1025` n `53` status `ready` deltaP `40.499` edge `0.2689` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.8553` n `66` status `ready` deltaP `55.3858` edge `0.4706` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.2613` n `53` status `ready` deltaP `21.869` edge `0.4414` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `5.0141` n `53` status `ready` deltaP `46.001` edge `0.1488` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7506` n `53` status `ready` deltaP `20.2604` edge `0.2405` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3417` n `53` status `ready` deltaP `30.9038` edge `0.0978` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.848` n `53` status `ready` deltaP `26.0991` edge `0.355` maxDD `-10.1088`
- `market_context_high->crypto_major_24h` score `2.6441` n `66` status `ready` deltaP `12.6306` edge `1.1687` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.4268` n `53` status `ready` deltaP `24.939` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2254` n `53` status `ready` deltaP `25.5903` edge `0.0403` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3771` n `53` status `ready` deltaP `18.3736` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
