# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T20:37:27.369945+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `309.2468` n `84` status `ready` deltaP `6.4732` edge `25.7415` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.8814` n `94` status `ready` deltaP `8.1053` edge `6.3142` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.816` n `53` status `ready` deltaP `23.4244` edge `2.3158` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.7986` n `84` status `ready` deltaP `21.1557` edge `1.6628` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.5356` n `53` status `ready` deltaP `37.1823` edge `1.4276` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.1359` n `53` status `ready` deltaP `31.9719` edge `0.6612` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.3688` n `84` status `ready` deltaP `41.2203` edge `1.2077` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.4147` n `53` status `ready` deltaP `43.2292` edge `0.3297` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2272` n `84` status `ready` deltaP `38.6905` edge `0.3023` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6006` n `53` status `ready` deltaP `43.6523` edge `0.13` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.08` n `84` status `ready` deltaP `23.1151` edge `0.1954` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.6717` n `53` status `ready` deltaP `21.3181` edge `0.1942` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1534` n `53` status `ready` deltaP `17.5658` edge `0.2087` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9703` n `53` status `ready` deltaP `26.7114` edge `0.0948` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.832` n `53` status `ready` deltaP `20.4384` edge `0.2485` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2433` n `53` status `ready` deltaP `26.3388` edge `0.0368` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6095` n `53` status `ready` deltaP `17.3924` edge `0.0618` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4997` n `53` status `ready` deltaP `25.2789` edge `0.1876` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2214` n `53` status `ready` deltaP `16.8766` edge `0.0194` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.9312` n `53` status `ready` deltaP `11.3011` edge `0.4946` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
