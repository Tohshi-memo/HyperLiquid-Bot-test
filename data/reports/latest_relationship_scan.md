# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T04:26:34.374716+00:00`
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

- `market_context_high->unknown_24h` score `37.3911` n `46` status `ready` deltaP `26.2983` edge `2.9449` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.7099` n `46` status `ready` deltaP `46.0825` edge `0.5193` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.2828` n `46` status `ready` deltaP `38.7832` edge `0.4496` maxDD `-0.434`
- `market_context_high->unknown_4h` score `4.0136` n `86` status `ready` deltaP `1.6059` edge `0.6034` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2602` n `86` status `ready` deltaP `15.5169` edge `0.0862` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5783` n `86` status `ready` deltaP `18.6578` edge `0.0098` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2745` n `88` status `ready` deltaP `5.9812` edge `0.0246` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2598` n `88` status `ready` deltaP `8.88` edge `-0.0027` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4195` n `88` status `ready` deltaP `2.3272` edge `-0.0159` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.517` n `86` status `ready` deltaP `5.3389` edge `0.0216` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5175` n `88` status `ready` deltaP `-1.3201` edge `-0.0081` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-1.2887` n `88` status `ready` deltaP `-3.62` edge `-0.0122` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4512` n `88` status `ready` deltaP `6.512` edge `-0.0759` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.5311` n `46` status `ready` deltaP `-2.8382` edge `0.0119` maxDD `-4.3126`
- `market_context_high->crypto_alt_4h` score `-1.6638` n `86` status `ready` deltaP `2.6305` edge `-0.0172` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.8346` n `86` status `ready` deltaP `-9.8341` edge `-0.0442` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.0081` n `88` status `ready` deltaP `3.3479` edge `-0.2283` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6103` n `88` status `ready` deltaP `-12.7994` edge `-0.0782` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8065` n `46` status `ready` deltaP `-23.6413` edge `-0.1261` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.5472` n `86` status `ready` deltaP `1.184` edge `-0.3142` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
