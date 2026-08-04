# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T06:37:30.909686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `37.4415` n `46` status `ready` deltaP `26.2983` edge `2.9491` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.0749` n `46` status `ready` deltaP `44.52` edge `0.4768` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.0582` n `46` status `ready` deltaP `37.2207` edge `0.4413` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8405` n `88` status `ready` deltaP `2.2727` edge `0.5711` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1506` n `88` status `ready` deltaP `14.9114` edge `0.0811` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3556` n `88` status `ready` deltaP `18.2372` edge `0.01` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2517` n `88` status `ready` deltaP `5.8315` edge `0.0237` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1952` n `88` status `ready` deltaP `8.1315` edge `-0.0031` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4491` n `88` status `ready` deltaP `1.8781` edge `-0.0167` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4865` n `88` status `ready` deltaP `5.6541` edge `0.0234` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5183` n `88` status `ready` deltaP `-1.3201` edge `-0.0082` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9686` n `88` status `ready` deltaP `3.2567` edge `-0.0069` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2479` n `88` status `ready` deltaP `-3.3206` edge `-0.0108` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5214` n `88` status `ready` deltaP `5.9132` edge `-0.0809` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.6993` n `46` status `ready` deltaP `-4.4007` edge `0.0083` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7844` n `88` status `ready` deltaP `-9.0493` edge `-0.043` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3476` n `88` status `ready` deltaP `2.8988` edge `-0.2536` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5852` n `88` status `ready` deltaP `-12.5` edge `-0.0781` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8511` n `46` status `ready` deltaP `-23.9885` edge `-0.1275` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.4516` n `88` status `ready` deltaP `1.5521` edge `-0.3044` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
