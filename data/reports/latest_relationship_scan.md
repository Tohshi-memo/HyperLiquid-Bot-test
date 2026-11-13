# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T18:07:28.018583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `370.5207` n `75` status `ready` deltaP `3.0625` edge `30.8704` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.5659` n `53` status `ready` deltaP `32.2786` edge `2.6526` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.3323` n `75` status `ready` deltaP `26.8194` edge `2.0864` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.4464` n `75` status `ready` deltaP `49.1459` edge `1.3777` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.3694` n `53` status `ready` deltaP `42.0434` edge `1.7585` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8224` n `53` status `ready` deltaP `34.2585` edge `0.7865` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6239` n `53` status `ready` deltaP `36.4583` edge `0.2256` maxDD `0.0`
- `market_context_high->index_24h` score `4.826` n `75` status `ready` deltaP `25.5625` edge `0.2409` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.733` n `53` status `ready` deltaP `44.8718` edge `0.1329` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.145` n `53` status `ready` deltaP `23.575` edge `0.2186` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9408` n `75` status `ready` deltaP `39.5973` edge `0.3304` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3515` n `53` status `ready` deltaP `17.2664` edge `0.2272` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1519` n `53` status `ready` deltaP `28.8455` edge `0.0957` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1077` n `53` status `ready` deltaP `19.2189` edge `0.2796` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1798` n `53` status `ready` deltaP `25.5903` edge `0.0365` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.1343` n `53` status `ready` deltaP `15.9886` edge `0.6176` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.9872` n `53` status `ready` deltaP `19.9839` edge `0.076` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7708` n `53` status `ready` deltaP `25.8887` edge `0.2183` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1843` n `53` status `ready` deltaP `16.1281` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6159` n `53` status `ready` deltaP `16.9952` edge `0.0636` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
