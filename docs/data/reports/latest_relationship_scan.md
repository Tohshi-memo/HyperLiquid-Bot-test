# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T18:07:24.625006+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2658`

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

- `market_context_high->unknown_1h` score `9992.3046` n `126` status `ready` deltaP `0.8649` edge `832.7061` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6060.3773` n `126` status `ready` deltaP `-0.6194` edge `505.0661` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2677` n `126` status `ready` deltaP `2.9037` edge `0.0128` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3847` n `126` status `ready` deltaP `1.3615` edge `0.0028` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8074` n `126` status `ready` deltaP `7.68` edge `0.0259` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4394` n `126` status `ready` deltaP `-9.405` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.878` n `126` status `ready` deltaP `-6.1169` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1224` n `126` status `ready` deltaP `3.7425` edge `0.0041` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3841` n `126` status `ready` deltaP `-9.4193` edge `-0.0227` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7704` n `126` status `ready` deltaP `-7.3001` edge `-0.0189` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2331` n `126` status `ready` deltaP `0.1639` edge `-0.0387` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8995` n `126` status `ready` deltaP `-6.4395` edge `-0.0543` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.1077` n `126` status `ready` deltaP `-5.3765` edge `-0.0543` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4625` n `126` status `ready` deltaP `-13.1697` edge `-0.0048` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1023` n `126` status `ready` deltaP `-21.1019` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.7799` n `126` status `ready` deltaP `7.3909` edge `0.112` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.1751` n `126` status `ready` deltaP `-6.4436` edge `-0.1237` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.464` n `126` status `ready` deltaP `15.0546` edge `0.3617` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8504` n `126` status `ready` deltaP `-26.6617` edge `-0.116` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.7332` n `126` status `ready` deltaP `4.3402` edge `0.0722` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
