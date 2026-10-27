# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T03:07:27.443661+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9550`

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

- `market_context_high->unknown_4h` score `87.5279` n `153` status `ready` deltaP `1.627` edge `7.3167` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.1889` n `153` status `ready` deltaP `1.4745` edge `1.7215` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.3223` n `153` status `ready` deltaP `11.6112` edge `0.0093` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3141` n `153` status `ready` deltaP `8.8636` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.0842` n `120` status `ready` deltaP `21.9641` edge `0.127` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.048` n `120` status `ready` deltaP `16.2002` edge `0.0097` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1151` n `153` status `ready` deltaP `8.6298` edge `0.0069` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.1803` n `153` status `ready` deltaP `2.9011` edge `0.0157` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2343` n `120` status `ready` deltaP `15.3596` edge `0.0248` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3605` n `153` status `ready` deltaP `6.6684` edge `0.0484` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6031` n `153` status `ready` deltaP `-0.2867` edge `-0.0017` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8468` n `153` status `ready` deltaP `4.9822` edge `0.0163` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.943` n `153` status `ready` deltaP `7.8172` edge `-0.002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7871` n `153` status `ready` deltaP `1.4549` edge `-0.0112` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9555` n `153` status `ready` deltaP `0.0235` edge `-0.0024` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4383` n `153` status `ready` deltaP `-6.5369` edge `-0.0253` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4007` n `120` status `ready` deltaP `-1.6464` edge `-0.0675` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.7129` n `153` status `ready` deltaP `-1.2205` edge `-0.0921` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-5.6379` n `120` status `ready` deltaP `-9.8541` edge `-0.0981` maxDD `-24.0547`
- `market_context_high->equity_24h` score `-6.2883` n `120` status `ready` deltaP `-5.8795` edge `-0.2237` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
