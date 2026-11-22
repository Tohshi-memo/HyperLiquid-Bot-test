# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T01:22:37.865373+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4574`

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

- `market_context_high->unknown_1h` score `9793.539` n `126` status `ready` deltaP `0.8649` edge `816.1423` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5864.3453` n `126` status `ready` deltaP `-0.6194` edge `488.7301` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2965` n `126` status `ready` deltaP `2.6043` edge `0.0111` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4766` n `126` status `ready` deltaP `-0.2852` edge `0.002` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9208` n `126` status `ready` deltaP `6.4605` edge `0.0195` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4154` n `126` status `ready` deltaP `-9.1056` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8701` n `126` status `ready` deltaP `-5.9645` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.3261` n `126` status `ready` deltaP `1.9461` edge `-0.0009` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3565` n `126` status `ready` deltaP `-9.1199` edge `-0.0224` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.9431` n `126` status `ready` deltaP `-9.1294` edge `-0.0211` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.5629` n `126` status `ready` deltaP `-1.0337` edge `-0.0582` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.1825` n `126` status `ready` deltaP `-7.4874` edge `-0.0709` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.08` n `126` status `ready` deltaP `-9.003` edge `-0.0007` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.5108` n `126` status `ready` deltaP `-6.1387` edge `-0.1009` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.0222` n `126` status `ready` deltaP `-20.3397` edge `-0.0803` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.0032` n `126` status `ready` deltaP `4.9603` edge `0.1096` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.4833` n `126` status `ready` deltaP `-6.2912` edge `-0.1504` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.7363` n `126` status `ready` deltaP `13.4921` edge `0.3372` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8411` n `126` status `ready` deltaP `-26.1409` edge `-0.1187` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.5865` n `126` status `ready` deltaP `3.4722` edge `0.0968` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
