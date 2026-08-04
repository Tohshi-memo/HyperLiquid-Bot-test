# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T04:37:33.401662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3935` n `46` status `ready` deltaP `26.2983` edge `2.9451` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.6324` n `46` status `ready` deltaP `45.9089` edge `0.514` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.2605` n `46` status `ready` deltaP `38.6096` edge `0.4489` maxDD `-0.434`
- `market_context_high->unknown_4h` score `6.1693` n `87` status `ready` deltaP `1.8678` edge `0.6012` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2754` n `87` status `ready` deltaP `15.7521` edge `0.0859` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.6094` n `87` status `ready` deltaP `18.9866` edge `0.0102` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2613` n `88` status `ready` deltaP `5.8315` edge `0.0245` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2479` n `88` status `ready` deltaP `8.7303` edge `-0.0027` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4195` n `88` status `ready` deltaP `2.3272` edge `-0.0159` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4786` n `87` status `ready` deltaP `5.8067` edge `0.0234` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5269` n `88` status `ready` deltaP `-1.4698` edge `-0.0083` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-1.2875` n `88` status `ready` deltaP `-3.62` edge `-0.0121` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4606` n `88` status `ready` deltaP `6.3623` edge `-0.0761` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.5498` n `46` status `ready` deltaP `-3.0118` edge `0.0115` maxDD `-4.3126`
- `market_context_high->crypto_alt_4h` score `-1.577` n `87` status `ready` deltaP `3.026` edge `-0.0126` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.8044` n `87` status `ready` deltaP `-9.3584` edge `-0.0435` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.0297` n `88` status `ready` deltaP `3.3479` edge `-0.2301` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6103` n `88` status `ready` deltaP `-12.7994` edge `-0.0782` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8113` n `46` status `ready` deltaP `-23.6413` edge `-0.1265` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.474` n `87` status `ready` deltaP `1.5262` edge `-0.3071` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
