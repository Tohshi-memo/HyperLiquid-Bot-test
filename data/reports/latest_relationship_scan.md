# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T16:22:29.147356+00:00`
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

- `market_context_high->unknown_24h` score `371.1327` n `75` status `ready` deltaP `4.2777` edge `30.9133` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.0191` n `53` status `ready` deltaP `31.7578` edge `2.6105` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.7854` n `75` status `ready` deltaP `26.2986` edge `2.0443` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.805` n `75` status `ready` deltaP `50.0139` edge `1.4018` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.293` n `53` status `ready` deltaP `42.0434` edge `1.7487` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.4197` n `53` status `ready` deltaP `33.6487` edge `0.757` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5685` n `53` status `ready` deltaP `36.1111` edge `0.2233` maxDD `0.0`
- `market_context_high->index_24h` score `4.7574` n `75` status `ready` deltaP `25.2153` edge `0.2375` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6652` n `53` status `ready` deltaP `44.4145` edge `0.1303` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0764` n `53` status `ready` deltaP `23.2278` edge `0.2152` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8754` n `75` status `ready` deltaP `38.7292` edge `0.3278` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.4738` n `53` status `ready` deltaP `17.5658` edge `0.2354` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9969` n `53` status `ready` deltaP `27.7784` edge `0.0899` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.9645` n `53` status `ready` deltaP `18.914` edge `0.2697` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.3674` n `53` status `ready` deltaP `16.8566` edge `0.6417` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1703` n `53` status `ready` deltaP `25.4406` edge `0.0367` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9364` n `53` status `ready` deltaP `19.679` edge `0.0738` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7097` n `53` status `ready` deltaP `25.5838` edge `0.2125` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2322` n `53` status `ready` deltaP `16.5772` edge `0.0223` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6284` n `53` status `ready` deltaP `16.9952` edge `0.0652` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
