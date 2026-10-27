# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T02:52:28.930714+00:00`
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

- `market_context_high->unknown_4h` score `87.5183` n `153` status `ready` deltaP `1.627` edge `7.3159` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.2093` n `153` status `ready` deltaP `1.4745` edge `1.7232` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.3273` n `153` status `ready` deltaP `9.0133` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3223` n `153` status `ready` deltaP `11.6112` edge `0.0093` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.1207` n `119` status `ready` deltaP `22.4123` edge `0.1287` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.0524` n `119` status `ready` deltaP `16.1004` edge `0.0098` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1151` n `153` status `ready` deltaP `8.6298` edge `0.0069` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.1791` n `153` status `ready` deltaP `2.9011` edge `0.0158` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2416` n `119` status `ready` deltaP `15.2178` edge `0.0248` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3593` n `153` status `ready` deltaP `6.6684` edge `0.0485` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6117` n `153` status `ready` deltaP `-0.4364` edge `-0.0018` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.867` n `153` status `ready` deltaP `4.8325` edge `0.0147` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9422` n `153` status `ready` deltaP `7.8172` edge `-0.0019` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8058` n `153` status `ready` deltaP `1.3052` edge `-0.0126` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9788` n `153` status `ready` deltaP `-0.1262` edge `-0.0044` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4395` n `153` status `ready` deltaP `-6.5369` edge `-0.0254` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4237` n `119` status `ready` deltaP `-1.8933` edge `-0.0688` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.7129` n `153` status `ready` deltaP `-1.2205` edge `-0.0921` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-5.6839` n `119` status `ready` deltaP `-10.4074` edge `-0.1003` maxDD `-24.0547`
- `market_context_high->equity_24h` score `-6.3685` n `119` status `ready` deltaP `-6.1474` edge `-0.2322` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
