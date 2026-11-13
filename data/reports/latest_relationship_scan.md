# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T19:52:26.861517+00:00`
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

- `market_context_high->unknown_24h` score `370.2788` n `75` status `ready` deltaP `2.8889` edge `30.8514` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.1492` n `53` status `ready` deltaP `33.4939` edge `2.6931` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.9155` n `75` status `ready` deltaP `28.0347` edge `2.1269` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.1392` n `75` status `ready` deltaP `47.9306` edge `1.3602` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4552` n `53` status `ready` deltaP `42.0434` edge `1.7695` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9514` n `53` status `ready` deltaP `34.7158` edge `0.7942` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.7787` n `53` status `ready` deltaP `37.6736` edge `0.2304` maxDD `0.0`
- `market_context_high->index_24h` score `4.9652` n `75` status `ready` deltaP `26.7778` edge `0.2444` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.8204` n `53` status `ready` deltaP `45.634` edge `0.1351` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.2842` n `53` status `ready` deltaP `24.7903` edge `0.2221` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0042` n `75` status `ready` deltaP `40.2917` edge `0.3339` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3791` n `53` status `ready` deltaP `17.4161` edge `0.2285` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2864` n `53` status `ready` deltaP `29.9126` edge `0.0998` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1355` n `53` status `ready` deltaP `19.3713` edge `0.2809` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2242` n `53` status `ready` deltaP `26.0394` edge `0.0372` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9908` n `53` status `ready` deltaP `19.9839` edge `0.0763` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.9346` n `53` status `ready` deltaP `14.7733` edge `0.6001` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7662` n `53` status `ready` deltaP `25.8887` edge `0.2177` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1723` n `53` status `ready` deltaP `15.9784` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5761` n `53` status `ready` deltaP `16.5461` edge `0.0615` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
