# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T02:37:29.595838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8004`

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

- `market_context_high->unknown_4h` score `87.5591` n `153` status `ready` deltaP `1.627` edge `7.3193` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.2465` n `153` status `ready` deltaP `1.4745` edge `1.7263` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.3393` n `153` status `ready` deltaP `9.163` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3223` n `153` status `ready` deltaP `11.6112` edge `0.0093` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.1515` n `118` status `ready` deltaP `22.8681` edge `0.1296` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.0609` n `118` status `ready` deltaP `15.996` edge `0.0094` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1143` n `153` status `ready` deltaP `8.6298` edge `0.007` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.1779` n `153` status `ready` deltaP `2.9011` edge `0.0159` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2485` n `118` status `ready` deltaP `15.0706` edge `0.0249` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3569` n `153` status `ready` deltaP `6.6684` edge `0.0487` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6203` n `153` status `ready` deltaP `-0.5861` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8834` n `153` status `ready` deltaP `4.6828` edge `0.0136` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9399` n `153` status `ready` deltaP `7.8172` edge `-0.0016` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8221` n `153` status `ready` deltaP `1.1555` edge `-0.0137` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9976` n `153` status `ready` deltaP `-0.2759` edge `-0.0058` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4407` n `153` status `ready` deltaP `-6.5369` edge `-0.0255` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4876` n `118` status `ready` deltaP `-2.1473` edge `-0.0753` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.716` n `153` status `ready` deltaP `-1.2205` edge `-0.0925` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-5.7295` n `118` status `ready` deltaP `-10.97` edge `-0.1024` maxDD `-24.0547`
- `market_context_high->equity_24h` score `-6.4741` n `118` status `ready` deltaP `-6.4227` edge `-0.2439` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
