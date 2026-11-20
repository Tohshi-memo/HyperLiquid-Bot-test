# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T19:07:30.245542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2758`

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

- `market_context_high->unknown_1h` score `10158.6305` n `126` status `ready` deltaP `1.4638` edge `846.5626` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6197.9613` n `126` status `ready` deltaP `-0.3145` edge `516.5294` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6471` n `108` status `ready` deltaP `26.794` edge `1.0957` maxDD `-57.8734`
- `market_context_high->crypto_alt_24h` score `-0.0295` n `108` status `ready` deltaP `13.8311` edge `0.8954` maxDD `-72.5383`
- `market_context_high->metal_1h` score `-0.1672` n `126` status `ready` deltaP `4.4007` edge `0.0157` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2804` n `126` status `ready` deltaP `3.3076` edge `0.0032` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5066` n `126` status `ready` deltaP `12.1007` edge `0.035` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4094` n `126` status `ready` deltaP `-8.9559` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8287` n `126` status `ready` deltaP `5.988` edge `0.0136` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9816` n `126` status `ready` deltaP `-7.7937` edge `-0.0005` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1864` n `126` status `ready` deltaP `-7.3235` edge `-0.0202` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3987` n `126` status `ready` deltaP `-2.8794` edge `-0.0174` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4343` n `126` status `ready` deltaP `2.5591` edge `0.0119` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1188` n `126` status `ready` deltaP `-3.4455` edge `-0.0092` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1929` n `126` status `ready` deltaP `1.0259` edge `0.1485` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.9198` n `108` status `ready` deltaP `12.963` edge `0.1096` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.7412` n `108` status `ready` deltaP `-18.5185` edge `-0.011` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.844` n `126` status `ready` deltaP `-19.8824` edge `-0.0685` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.0302` n `126` status `ready` deltaP `1.7881` edge `0.0835` maxDD `-46.5016`
- `market_context_high->index_24h` score `-13.1724` n `108` status `ready` deltaP `-26.3888` edge `-0.1588` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
