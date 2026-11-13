# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T16:52:32.148542+00:00`
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

- `market_context_high->unknown_24h` score `370.9945` n `75` status `ready` deltaP `3.9305` edge `30.9041` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.1998` n `53` status `ready` deltaP `31.9314` edge `2.6244` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.9661` n `75` status `ready` deltaP `26.4722` edge `2.0582` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.6885` n `75` status `ready` deltaP `49.6667` edge `1.3944` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.3179` n `53` status `ready` deltaP `42.0434` edge `1.7519` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5411` n `53` status `ready` deltaP `33.8012` edge `0.7661` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5769` n `53` status `ready` deltaP `36.1111` edge `0.224` maxDD `0.0`
- `market_context_high->index_24h` score `4.7845` n `75` status `ready` deltaP `25.3889` edge `0.2386` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6748` n `53` status `ready` deltaP `44.4145` edge `0.1311` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1035` n `53` status `ready` deltaP `23.4014` edge `0.2163` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8906` n `75` status `ready` deltaP `38.9028` edge `0.3286` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.487` n `53` status `ready` deltaP `17.7155` edge `0.2355` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0501` n `53` status `ready` deltaP `28.0833` edge `0.0923` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0127` n `53` status `ready` deltaP `19.0664` edge `0.2727` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.2917` n `53` status `ready` deltaP `16.5094` edge `0.6343` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1846` n `53` status `ready` deltaP `25.5903` edge `0.0369` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.957` n `53` status `ready` deltaP `19.8315` edge `0.0745` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7224` n `53` status `ready` deltaP `25.7363` edge `0.2131` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2334` n `53` status `ready` deltaP `16.5772` edge `0.0224` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.633` n `53` status `ready` deltaP `17.1449` edge `0.0648` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
