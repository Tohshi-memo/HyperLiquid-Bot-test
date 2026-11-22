# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T03:22:24.483005+00:00`
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

- `market_context_high->unknown_1h` score `9781.9986` n `126` status `ready` deltaP `0.8649` edge `815.1806` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5850.5057` n `126` status `ready` deltaP `-0.6194` edge `487.5768` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2685` n `126` status `ready` deltaP `3.0534` edge `0.0117` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4486` n `126` status `ready` deltaP `0.1639` edge `0.0026` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8646` n `126` status `ready` deltaP `7.3751` edge `0.0206` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3915` n `126` status `ready` deltaP `-8.8062` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8123` n `126` status `ready` deltaP `-4.8974` edge `0.0019` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.2182` n `126` status `ready` deltaP `2.5449` edge `0.0041` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.2655` n `126` status `ready` deltaP `-8.072` edge `-0.0218` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8896` n `126` status `ready` deltaP `-8.5196` edge `-0.0207` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2642` n `126` status `ready` deltaP `-0.4349` edge `-0.0373` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9366` n `126` status `ready` deltaP `-6.8886` edge `-0.0544` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.016` n `126` status `ready` deltaP `-8.3085` edge `0.0` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.1059` n `126` status `ready` deltaP `-5.0717` edge `-0.0561` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.9126` n `126` status `ready` deltaP `-19.1202` edge `-0.0793` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.9468` n `126` status `ready` deltaP `4.9603` edge `0.1143` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.012` n `126` status `ready` deltaP `-5.529` edge `-0.1162` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.553` n `126` status `ready` deltaP `13.4921` edge `0.3607` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8399` n `126` status `ready` deltaP `-26.1409` edge `-0.1186` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.3633` n `126` status `ready` deltaP `3.8194` edge `0.1231` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
