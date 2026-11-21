# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T16:07:33.797928+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2644`

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

- `market_context_high->unknown_1h` score `9998.781` n `126` status `ready` deltaP `0.8649` edge `833.2458` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6075.6099` n `126` status `ready` deltaP `-0.7719` edge `506.3365` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.249` n `126` status `ready` deltaP `3.2031` edge `0.0132` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3598` n `126` status `ready` deltaP `1.8106` edge `0.003` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.7577` n `126` status `ready` deltaP `8.4422` edge `0.0272` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4645` n `126` status `ready` deltaP `-9.7044` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8701` n `126` status `ready` deltaP `-5.9645` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.0361` n `126` status `ready` deltaP `4.491` edge `0.0063` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3074` n `126` status `ready` deltaP `-8.5211` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.74` n `126` status `ready` deltaP `-6.9952` edge `-0.0184` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.0688` n `126` status `ready` deltaP `0.9124` edge `-0.03` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8047` n `126` status `ready` deltaP `-6.1401` edge `-0.0484` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.8558` n `126` status `ready` deltaP `-4.4619` edge `-0.0281` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4805` n `126` status `ready` deltaP `-13.1697` edge `-0.0063` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.0755` n `126` status `ready` deltaP `-20.797` edge `-0.0817` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.6438` n `126` status `ready` deltaP `8.4326` edge `0.1164` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.7228` n `126` status `ready` deltaP `-5.529` edge `-0.0921` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.0907` n `126` status `ready` deltaP `16.4434` edge `0.4003` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.9041` n `126` status `ready` deltaP `-27.1825` edge `-0.117` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.3451` n `126` status `ready` deltaP `5.7291` edge `0.1127` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
