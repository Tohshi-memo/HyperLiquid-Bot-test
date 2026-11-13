# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T18:22:30.741224+00:00`
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

- `market_context_high->unknown_24h` score `370.4516` n `75` status `ready` deltaP `2.8889` edge `30.8658` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.6674` n `53` status `ready` deltaP `32.4522` edge `2.6599` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.4338` n `75` status `ready` deltaP `26.993` edge `2.0937` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.4061` n `75` status `ready` deltaP `48.9723` edge `1.3755` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.3881` n `53` status `ready` deltaP `42.0434` edge `1.7609` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9006` n `53` status `ready` deltaP `34.4109` edge `0.792` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.645` n `53` status `ready` deltaP `36.6319` edge `0.2262` maxDD `0.0`
- `market_context_high->index_24h` score `4.8483` n `75` status `ready` deltaP `25.7361` edge `0.2416` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.7488` n `53` status `ready` deltaP `45.0242` edge `0.1332` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1673` n `53` status `ready` deltaP `23.7486` edge `0.2193` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9545` n `75` status `ready` deltaP `39.7709` edge `0.331` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3563` n `53` status `ready` deltaP `17.2664` edge `0.2276` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1713` n `53` status `ready` deltaP `28.998` edge `0.0963` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1403` n `53` status `ready` deltaP `19.3713` edge `0.2813` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.181` n `53` status `ready` deltaP `25.5903` edge `0.0366` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.1081` n `53` status `ready` deltaP `15.815` edge `0.6154` maxDD `-29.0448`
- `news_risk_high->index_4h` score `2.0054` n `53` status `ready` deltaP `20.1363` edge `0.0765` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7928` n `53` status `ready` deltaP `26.0411` edge `0.2201` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1855` n `53` status `ready` deltaP `16.1281` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6143` n `53` status `ready` deltaP `16.9952` edge `0.0634` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
