# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T16:37:27.862532+00:00`
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

- `market_context_high->unknown_1h` score `9998.8086` n `126` status `ready` deltaP `0.8649` edge `833.2481` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6070.0467` n `126` status `ready` deltaP `-0.7719` edge `505.8729` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2514` n `126` status `ready` deltaP `3.2031` edge `0.0129` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.377` n `126` status `ready` deltaP `1.5112` edge `0.0028` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.7782` n `126` status `ready` deltaP `8.1373` edge `0.0266` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8622` n `126` status `ready` deltaP `-5.812` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.0733` n `126` status `ready` deltaP `4.1916` edge `0.0052` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3194` n `126` status `ready` deltaP `-8.6708` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.768` n `126` status `ready` deltaP `-7.3001` edge `-0.0187` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.1048` n `126` status `ready` deltaP `0.7627` edge `-0.032` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8215` n `126` status `ready` deltaP `-6.1401` edge `-0.0498` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.9426` n `126` status `ready` deltaP `-4.7668` edge `-0.0372` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4769` n `126` status `ready` deltaP `-13.1697` edge `-0.006` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.0889` n `126` status `ready` deltaP `-20.9494` edge `-0.0818` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.6558` n `126` status `ready` deltaP `8.4326` edge `0.1154` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.8588` n `126` status `ready` deltaP `-5.8339` edge `-0.1014` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.182` n `126` status `ready` deltaP `16.0962` edge `0.3909` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8993` n `126` status `ready` deltaP `-27.1825` edge `-0.1166` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.4458` n `126` status `ready` deltaP `5.3819` edge `0.1021` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
