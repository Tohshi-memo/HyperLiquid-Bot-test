# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T00:37:24.558422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4570`

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

- `market_context_high->unknown_1h` score `9943.7357` n `126` status `ready` deltaP `1.0146` edge `828.6577` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6020.0393` n `126` status `ready` deltaP `-0.6194` edge `501.7046` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2708` n `126` status `ready` deltaP `3.0534` edge `0.0114` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.468` n `126` status `ready` deltaP `-0.1355` edge `0.0021` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9295` n `126` status `ready` deltaP `6.308` edge `0.0194` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4286` n `126` status `ready` deltaP `-9.2553` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.2961` n `126` status `ready` deltaP `2.2455` edge `-0.0004` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3553` n `126` status `ready` deltaP `-9.1199` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.9297` n `126` status `ready` deltaP `-8.977` edge `-0.021` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.5689` n `126` status `ready` deltaP `-1.1834` edge `-0.0577` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.1981` n `126` status `ready` deltaP `-7.6371` edge `-0.0712` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.1264` n `126` status `ready` deltaP `-9.5238` edge `-0.0011` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.6477` n `126` status `ready` deltaP `-6.5961` edge `-0.1154` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.0478` n `126` status `ready` deltaP `-20.6446` edge `-0.0804` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.032` n `126` status `ready` deltaP `4.9603` edge `0.1072` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.6483` n `126` status `ready` deltaP `-6.7485` edge `-0.1611` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.8299` n `126` status `ready` deltaP `13.4921` edge `0.3252` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8483` n `126` status `ready` deltaP `-26.1409` edge `-0.1193` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.6887` n `126` status `ready` deltaP `3.4722` edge `0.0837` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
