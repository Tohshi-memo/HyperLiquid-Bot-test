# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T13:22:34.028890+00:00`
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

- `market_context_high->unknown_24h` score `372.2595` n `75` status `ready` deltaP `5.493` edge `30.9991` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.6627` n `53` status `ready` deltaP `31.7578` edge `2.5808` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.429` n `75` status `ready` deltaP `26.2986` edge `2.0146` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.5734` n `75` status `ready` deltaP `51.9236` edge `1.4531` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.251` n `53` status `ready` deltaP `42.3906` edge `1.741` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.2306` n `53` status `ready` deltaP `34.106` edge `0.7382` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.7272` n `53` status `ready` deltaP `36.8056` edge `0.2319` maxDD `0.0`
- `market_context_high->index_24h` score `4.731` n `75` status `ready` deltaP `25.2153` edge `0.2353` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.5682` n `53` status `ready` deltaP `43.6523` edge `0.1273` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.05` n `53` status `ready` deltaP `23.2278` edge `0.213` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.7719` n `75` status `ready` deltaP `37.3403` edge `0.3238` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3226` n `53` status `ready` deltaP `17.7155` edge `0.2218` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0163` n `53` status `ready` deltaP `27.9309` edge `0.0905` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.9437` n `53` status `ready` deltaP `18.6091` edge `0.27` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.8669` n `53` status `ready` deltaP `18.7663` edge `0.693` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1044` n `53` status `ready` deltaP `24.8418` edge `0.0352` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9076` n `53` status `ready` deltaP `19.679` edge `0.0714` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8091` n `53` status `ready` deltaP `25.8887` edge `0.2232` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.1281` edge `0.0204` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5886` n `53` status `ready` deltaP `16.6958` edge `0.0621` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
