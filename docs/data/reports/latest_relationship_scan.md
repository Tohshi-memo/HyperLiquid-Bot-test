# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T22:37:28.670319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11650`

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

- `news_risk_high->unknown_24h` score `1087.4079` n `79` status `ready` deltaP `-0.9186` edge `90.6279` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.449` n `47` status `ready` deltaP `8.1698` edge `5.9067` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.277` n `47` status `ready` deltaP `29.5545` edge `4.032` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.7704` n `47` status `ready` deltaP `24.782` edge `2.5203` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2104` n `47` status `ready` deltaP `33.2003` edge `1.9151` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6269` n `47` status `ready` deltaP `34.4156` edge `0.4191` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.853` n `47` status `ready` deltaP `32.6278` edge `0.1274` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7703` n `47` status `ready` deltaP `17.7542` edge `0.1543` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.575` n `47` status `ready` deltaP `29.758` edge `0.0316` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3809` n `47` status `ready` deltaP `11.2124` edge `0.1071` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0769` n `47` status `ready` deltaP `12.3646` edge `0.0476` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9304` n `111` status `ready` deltaP `9.3287` edge `0.1064` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8277` n `47` status `ready` deltaP `13.1131` edge `0.0094` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.59` n `79` status `ready` deltaP `22.7167` edge `0.0903` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5464` n `47` status `ready` deltaP `11.0077` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3974` n `47` status `ready` deltaP `4.6899` edge `0.0923` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2559` n `47` status `ready` deltaP `4.6025` edge `0.0724` maxDD `-4.5405`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`
- `news_risk_high->equity_1h` score `0.0448` n `111` status `ready` deltaP `3.164` edge `0.0354` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `0.0352` n `111` status `ready` deltaP `3.9125` edge `0.0524` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
