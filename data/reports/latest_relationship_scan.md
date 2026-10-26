# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T16:22:32.613545+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7968`

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

- `market_context_high->unknown_4h` score `75.4808` n `151` status `ready` deltaP `0.499` edge `6.3203` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `27.1178` n `154` status `ready` deltaP `1.4309` edge `2.2992` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.435` n `113` status `ready` deltaP `26.5808` edge `0.1456` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1836` n `154` status `ready` deltaP `7.2926` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1247` n `151` status `ready` deltaP `9.3209` edge `0.0081` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0616` n `113` status `ready` deltaP `15.7283` edge `0.0132` maxDD `-4.7426`
- `market_context_high->fx_24h` score `-0.1072` n `113` status `ready` deltaP `17.443` edge `0.0272` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1584` n `154` status `ready` deltaP `7.8875` edge `0.0063` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3212` n `154` status `ready` deltaP `1.8003` edge `0.0113` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6125` n `154` status `ready` deltaP `-0.4511` edge `-0.0018` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6645` n `151` status `ready` deltaP `4.5037` edge `0.0375` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9374` n `154` status `ready` deltaP `3.795` edge `0.0126` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0211` n `151` status `ready` deltaP `6.434` edge `-0.0028` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8492` n `154` status `ready` deltaP `1.1451` edge `-0.0171` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0227` n `154` status `ready` deltaP `-0.6552` edge `-0.0065` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4812` n `151` status `ready` deltaP `-6.939` edge `-0.0262` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3929` n `113` status `ready` deltaP `-2.3359` edge `-0.0619` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8177` n `151` status `ready` deltaP `-1.9908` edge `-0.1004` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0242` n `113` status `ready` deltaP `-2.5644` edge `-0.2007` maxDD `-36.3631`
- `market_context_high->commodity_24h` score `-6.3488` n `113` status `ready` deltaP `-17.3433` edge `-0.1394` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
