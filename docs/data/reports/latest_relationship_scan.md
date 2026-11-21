# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T18:37:28.030106+00:00`
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

- `market_context_high->unknown_1h` score `9988.2917` n `126` status `ready` deltaP `1.0146` edge `832.3707` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6047.4653` n `126` status `ready` deltaP `-0.6194` edge `503.9901` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2677` n `126` status `ready` deltaP `2.9037` edge `0.0128` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3762` n `126` status `ready` deltaP `1.5112` edge `0.0029` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8327` n `126` status `ready` deltaP `7.3751` edge `0.0247` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4525` n `126` status `ready` deltaP `-9.5547` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1236` n `126` status `ready` deltaP `3.7425` edge `0.004` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3961` n `126` status `ready` deltaP `-9.569` edge `-0.0227` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7704` n `126` status `ready` deltaP `-7.3001` edge `-0.0189` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2031` n `126` status `ready` deltaP `0.3136` edge `-0.0372` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9007` n `126` status `ready` deltaP `-6.4395` edge `-0.0544` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.1695` n `126` status `ready` deltaP `-5.529` edge `-0.0612` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4589` n `126` status `ready` deltaP `-13.1697` edge `-0.0045` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1023` n `126` status `ready` deltaP `-21.1019` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.8209` n `126` status `ready` deltaP `7.0437` edge `0.1109` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.2879` n `126` status `ready` deltaP `-6.4436` edge `-0.1331` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.5112` n `126` status `ready` deltaP `14.8809` edge `0.3568` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8178` n `126` status `ready` deltaP `-26.3145` edge `-0.1156` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.7926` n `126` status `ready` deltaP `3.993` edge `0.0669` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
