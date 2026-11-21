# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T22:07:29.789960+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `32`

- Symbol pattern count: `3608`

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

- `market_context_high->unknown_1h` score `9975.2309` n `126` status `ready` deltaP `1.4638` edge `831.2793` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6019.4053` n `126` status `ready` deltaP `-0.9243` edge `501.6538` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.3082` n `126` status `ready` deltaP `2.4546` edge `0.0106` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4525` n `126` status `ready` deltaP `0.1639` edge `0.0021` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9761` n `126` status `ready` deltaP `5.5458` edge `0.0185` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.878` n `126` status `ready` deltaP `-6.1169` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.2914` n `126` status `ready` deltaP `2.3952` edge `-0.001` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4488` n `126` status `ready` deltaP `-10.1678` edge `-0.0231` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.897` n `126` status `ready` deltaP `-8.6721` edge `-0.0203` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.5401` n `126` status `ready` deltaP `-0.884` edge `-0.0573` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.2042` n `126` status `ready` deltaP `-7.188` edge `-0.0747` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.2785` n `126` status `ready` deltaP `-11.2599` edge `-0.0022` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.8441` n `126` status `ready` deltaP `-7.3582` edge `-0.1355` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.1243` n `126` status `ready` deltaP `-21.4068` edge `-0.0817` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.08` n `126` status `ready` deltaP `4.9603` edge `0.1032` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.9727` n `126` status `ready` deltaP `-7.0534` edge `-0.1861` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-13.1396` n `126` status `ready` deltaP `13.4921` edge `0.2855` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8435` n `126` status `ready` deltaP `-26.1409` edge `-0.1189` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-16.1726` n `126` status `ready` deltaP `2.4305` edge `0.0286` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
