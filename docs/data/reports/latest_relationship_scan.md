# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T21:07:28.360003+00:00`
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

- `market_context_high->unknown_1h` score `9974.4221` n `126` status `ready` deltaP `1.0146` edge `831.2149` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6023.4979` n `126` status `ready` deltaP `-1.3816` edge `501.9979` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2965` n `126` status `ready` deltaP `2.4546` edge `0.0121` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4276` n `126` status `ready` deltaP `0.613` edge `0.0023` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9517` n `126` status `ready` deltaP `5.8507` edge `0.0196` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4645` n `126` status `ready` deltaP `-9.7044` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.2362` n `126` status `ready` deltaP `2.6946` edge `0.0016` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4476` n `126` status `ready` deltaP `-10.1678` edge `-0.023` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8788` n `126` status `ready` deltaP `-8.5196` edge `-0.0198` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.3926` n `126` status `ready` deltaP `-0.7343` edge `-0.046` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.0746` n `126` status `ready` deltaP `-7.0383` edge `-0.0649` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.3449` n `126` status `ready` deltaP `-11.9544` edge `-0.0031` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.7189` n `126` status `ready` deltaP `-6.9009` edge `-0.1225` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.1267` n `126` status `ready` deltaP `-21.4068` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.039` n `126` status `ready` deltaP `5.3076` edge `0.1043` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.9223` n `126` status `ready` deltaP `-7.0534` edge `-0.1819` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-13.0611` n `126` status `ready` deltaP `13.6657` edge `0.2944` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8315` n `126` status `ready` deltaP `-26.1409` edge `-0.1179` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-16.1945` n `126` status `ready` deltaP `2.4305` edge `0.0258` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
