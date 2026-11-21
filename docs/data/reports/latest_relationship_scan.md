# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T17:07:25.940247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2652`

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

- `market_context_high->unknown_1h` score `9998.763` n `126` status `ready` deltaP `0.8649` edge `833.2443` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6070.1223` n `126` status `ready` deltaP `-0.7719` edge `505.8792` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2599` n `126` status `ready` deltaP `3.0534` edge `0.0128` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3933` n `126` status `ready` deltaP `1.2118` edge `0.0027` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.7885` n `126` status `ready` deltaP `7.9849` edge `0.0263` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4274` n `126` status `ready` deltaP `-9.2553` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8622` n `126` status `ready` deltaP `-5.812` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1104` n `126` status `ready` deltaP `3.8922` edge `0.0041` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3458` n `126` status `ready` deltaP `-8.9702` edge `-0.0225` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.796` n `126` status `ready` deltaP `-7.605` edge `-0.019` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.1744` n `126` status `ready` deltaP `0.4633` edge `-0.0358` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8611` n `126` status `ready` deltaP `-6.1401` edge `-0.0531` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.024` n `126` status `ready` deltaP `-5.0717` edge `-0.0456` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4721` n `126` status `ready` deltaP `-13.1697` edge `-0.0056` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.0901` n `126` status `ready` deltaP `-20.9494` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.6956` n `126` status `ready` deltaP `8.0853` edge `0.1144` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.9959` n `126` status `ready` deltaP `-6.1387` edge `-0.1108` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.2789` n `126` status `ready` deltaP `15.749` edge `0.3808` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8703` n `126` status `ready` deltaP `-26.8353` edge `-0.1165` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.5559` n `126` status `ready` deltaP `5.0347` edge `0.0903` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
