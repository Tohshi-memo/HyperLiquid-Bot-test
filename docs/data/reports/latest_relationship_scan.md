# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T16:52:24.639338+00:00`
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

- `market_context_high->unknown_1h` score `9998.799` n `126` status `ready` deltaP `0.8649` edge `833.2473` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6070.1535` n `126` status `ready` deltaP `-0.7719` edge `505.8818` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2599` n `126` status `ready` deltaP `3.0534` edge `0.0128` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3847` n `126` status `ready` deltaP `1.3615` edge `0.0028` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.7877` n `126` status `ready` deltaP `7.9849` edge `0.0264` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4274` n `126` status `ready` deltaP `-9.2553` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8614` n `126` status `ready` deltaP `-5.812` edge `0.0017` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.0912` n `126` status `ready` deltaP `4.0419` edge `0.0047` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3326` n `126` status `ready` deltaP `-8.8205` edge `-0.0224` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7826` n `126` status `ready` deltaP `-7.4526` edge `-0.0189` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.1372` n `126` status `ready` deltaP `0.613` edge `-0.0337` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8359` n `126` status `ready` deltaP `-6.1401` edge `-0.051` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.9872` n `126` status `ready` deltaP `-4.9192` edge `-0.0419` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4745` n `126` status `ready` deltaP `-13.1697` edge `-0.0058` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.0901` n `126` status `ready` deltaP `-20.9494` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.6757` n `126` status `ready` deltaP `8.259` edge `0.1149` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.9285` n `126` status `ready` deltaP `-5.9863` edge `-0.1062` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.2254` n `126` status `ready` deltaP `15.9226` edge `0.3865` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8842` n `126` status `ready` deltaP `-27.0089` edge `-0.1165` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.4939` n `126` status `ready` deltaP `5.2083` edge `0.0971` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
