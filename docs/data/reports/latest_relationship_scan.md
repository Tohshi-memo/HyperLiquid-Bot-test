# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T07:22:22.965306+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4562`

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

- `market_context_high->unknown_1h` score `11016.9498` n `114` status `ready` deltaP `1.0006` edge `918.0923` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6794.1104` n `114` status `ready` deltaP `-1.4548` edge `566.2161` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1536` n `114` status `ready` deltaP `5.2185` edge `0.012` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2883` n `114` status `ready` deltaP `3.2514` edge `0.003` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.3394` n `114` status `ready` deltaP `-9.9932` edge `-0.0017` maxDD `-0.4637`
- `market_context_high->crypto_major_1h` score `-1.5382` n `114` status `ready` deltaP `3.2514` edge `-0.0079` maxDD `-13.8788`
- `market_context_high->metal_4h` score `-1.5928` n `114` status `ready` deltaP `5.7124` edge `0.0098` maxDD `-10.1161`
- `market_context_high->fx_4h` score `-1.6761` n `114` status `ready` deltaP `-2.6396` edge `0.0024` maxDD `-1.6419`
- `market_context_high->equity_1h` score `-1.7967` n `114` status `ready` deltaP `6.3531` edge `0.0055` maxDD `-13.1399`
- `market_context_high->crypto_alt_1h` score `-2.3252` n `114` status `ready` deltaP `-5.3919` edge `-0.0511` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.5067` n `114` status `ready` deltaP `-10.613` edge `-0.0252` maxDD `-4.3687`
- `market_context_high->index_4h` score `-2.9799` n `114` status `ready` deltaP `-9.0795` edge `-0.0245` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-5.3007` n `114` status `ready` deltaP `-7.6663` edge `-0.0019` maxDD `-6.4306`
- `market_context_high->crypto_major_4h` score `-5.964` n `114` status `ready` deltaP `-4.9235` edge `-0.0389` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.8055` n `114` status `ready` deltaP `-17.7043` edge `-0.0848` maxDD `-15.1436`
- `market_context_high->metal_24h` score `-9.2723` n `114` status `ready` deltaP `-2.9696` edge `0.0567` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.8989` n `114` status `ready` deltaP `-5.0759` edge `-0.1098` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.9968` n `114` status `ready` deltaP `-27.595` edge `-0.3355` maxDD `-64.4102`
- `market_context_high->crypto_major_24h` score `-14.2342` n `114` status `ready` deltaP `10.4715` edge `0.1653` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.5928` n `114` status `ready` deltaP `-30.5373` edge `-0.1552` maxDD `-39.9159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
