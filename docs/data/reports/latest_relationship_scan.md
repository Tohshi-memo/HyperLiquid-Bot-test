# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T13:22:27.079986+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `10008.0137` n `126` status `ready` deltaP `1.0146` edge `834.0142` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6087.8105` n `126` status `ready` deltaP `-0.6194` edge `507.3522` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2` n `126` status `ready` deltaP `3.9516` edge `0.0145` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3248` n `126` status `ready` deltaP `2.4094` edge `0.0035` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6268` n `126` status `ready` deltaP `10.119` edge `0.0328` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4034` n `126` status `ready` deltaP `-8.9559` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8606` n `126` status `ready` deltaP `-5.812` edge `0.0018` maxDD `-1.794`
- `market_context_high->equity_1h` score `-1.8862` n `126` status `ready` deltaP `5.3892` edge `0.0128` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.2823` n `126` status `ready` deltaP `-8.2217` edge `-0.0222` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5699` n `126` status `ready` deltaP `-5.3184` edge `-0.0154` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.7701` n `126` status `ready` deltaP `1.6609` edge `-0.0101` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.4509` n `126` status `ready` deltaP `-4.9425` edge `-0.0269` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.0323` n `126` status `ready` deltaP `-2.7851` edge `0.0663` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.447` n `123` status `ready` deltaP `-13.2072` edge `-0.0071` maxDD `-6.7014`
- `market_context_high->commodity_4h` score `-6.932` n `126` status `ready` deltaP `-19.2726` edge `-0.0799` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.3309` n `123` status `ready` deltaP `9.1675` edge `0.1159` maxDD `-51.3676`
- `market_context_high->crypto_alt_4h` score `-8.5242` n `126` status `ready` deltaP `-3.8522` edge `-0.0034` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-10.7359` n `123` status `ready` deltaP `18.551` edge `0.4604` maxDD `-145.1715`
- `market_context_high->crypto_alt_24h` score `-14.0029` n `123` status `ready` deltaP `7.5077` edge `0.1798` maxDD `-150.3411`
- `market_context_high->index_24h` score `-14.613` n `123` status `ready` deltaP `-27.0664` edge `-0.1206` maxDD `-39.0031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
