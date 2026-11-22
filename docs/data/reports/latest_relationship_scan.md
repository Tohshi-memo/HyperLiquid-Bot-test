# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T02:07:27.900226+00:00`
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

- `market_context_high->unknown_1h` score `9786.2586` n `126` status `ready` deltaP `0.8649` edge `815.5356` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5856.0809` n `126` status `ready` deltaP `-0.6194` edge `488.0414` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.316` n `126` status `ready` deltaP `2.3049` edge `0.0106` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.493` n `126` status `ready` deltaP `-0.5846` edge `0.0019` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9121` n `126` status `ready` deltaP `6.6129` edge `0.0196` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3915` n `126` status `ready` deltaP `-8.8062` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8535` n `126` status `ready` deltaP `-5.6596` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.3194` n `126` status `ready` deltaP `-8.6708` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->equity_1h` score `-2.3537` n `126` status `ready` deltaP `1.7964` edge `-0.0022` maxDD `-13.1399`
- `market_context_high->index_4h` score `-2.9443` n `126` status `ready` deltaP `-9.1294` edge `-0.0212` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.6685` n `126` status `ready` deltaP `-1.1834` edge `-0.066` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.2533` n `126` status `ready` deltaP `-7.6371` edge `-0.0758` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.0486` n `126` status `ready` deltaP `-8.6558` edge `-0.0004` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.3967` n `126` status `ready` deltaP `-5.8339` edge `-0.0883` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.9808` n `126` status `ready` deltaP `-19.8824` edge `-0.0799` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.9768` n `126` status `ready` deltaP `4.9603` edge `0.1118` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.3789` n `126` status `ready` deltaP `-6.2912` edge `-0.1417` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.6919` n `126` status `ready` deltaP `13.4921` edge `0.3429` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8375` n `126` status `ready` deltaP `-26.1409` edge `-0.1184` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.5249` n `126` status `ready` deltaP `3.4722` edge `0.1047` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
