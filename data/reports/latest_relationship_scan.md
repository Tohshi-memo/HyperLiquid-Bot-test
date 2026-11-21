# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T20:22:30.121449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2646`

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

- `market_context_high->unknown_1h` score `9983.5121` n `126` status `ready` deltaP `1.1643` edge `831.9714` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6023.4899` n `126` status `ready` deltaP `-1.0767` edge `501.9952` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2942` n `126` status `ready` deltaP `2.4546` edge `0.0124` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4112` n `126` status `ready` deltaP `0.9124` edge `0.0024` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9178` n `126` status `ready` deltaP `6.308` edge `0.0209` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1835` n `126` status `ready` deltaP `3.1437` edge `0.003` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4476` n `126` status `ready` deltaP `-10.1678` edge `-0.023` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8508` n `126` status `ready` deltaP `-8.2148` edge `-0.0195` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.3338` n `126` status `ready` deltaP `-0.5846` edge `-0.0421` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9619` n `126` status `ready` deltaP `-6.5892` edge `-0.0585` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.3913` n `126` status `ready` deltaP `-12.4752` edge `-0.0035` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.5649` n `126` status `ready` deltaP `-6.4436` edge `-0.1058` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.1279` n `126` status `ready` deltaP `-21.4068` edge `-0.082` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.9745` n `126` status `ready` deltaP `5.8284` edge `0.1062` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.7345` n `126` status `ready` deltaP `-6.5961` edge `-0.1693` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.9238` n `126` status `ready` deltaP `13.6657` edge `0.312` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8195` n `126` status `ready` deltaP `-26.1409` edge `-0.1169` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-16.0945` n `126` status `ready` deltaP `2.7777` edge `0.0363` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
