# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T14:37:26.200121+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10494`

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

- `market_context_high->unknown_24h` score `371.9174` n `75` status `ready` deltaP `5.1458` edge `30.9729` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.5039` n `53` status `ready` deltaP `31.0633` edge `2.5722` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.2703` n `75` status `ready` deltaP `25.6041` edge `2.006` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.2004` n `75` status `ready` deltaP `51.0556` edge `1.4278` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2033` n `53` status `ready` deltaP `42.0434` edge `1.7372` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.0835` n `53` status `ready` deltaP `33.4963` edge `0.73` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6105` n `53` status `ready` deltaP `36.1111` edge `0.2268` maxDD `0.0`
- `market_context_high->index_24h` score `4.6913` n `75` status `ready` deltaP `24.8681` edge `0.2343` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.5828` n `53` status `ready` deltaP `43.8047` edge `0.1275` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0103` n `53` status `ready` deltaP `22.8806` edge `0.212` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8213` n `75` status `ready` deltaP `38.0348` edge `0.3255` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.2915` n `53` status `ready` deltaP `17.4161` edge `0.2212` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9387` n `53` status `ready` deltaP `27.3211` edge `0.0881` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8257` n `53` status `ready` deltaP `18.3042` edge `0.2622` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.6244` n `53` status `ready` deltaP `17.8983` edge `0.6677` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1008` n `53` status `ready` deltaP `24.8418` edge `0.0349` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.893` n `53` status `ready` deltaP `19.5266` edge `0.0712` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.723` n `53` status `ready` deltaP `25.5838` edge `0.2142` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1759` n `53` status `ready` deltaP `16.1281` edge `0.0206` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5504` n `53` status `ready` deltaP `16.5461` edge `0.0582` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
