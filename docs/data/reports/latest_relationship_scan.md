# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T06:52:29.958765+00:00`
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

- `market_context_high->unknown_24h` score `37.418` n `46` status `ready` deltaP `26.1247` edge `2.9483` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.013` n `46` status `ready` deltaP `44.3464` edge `0.4728` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.0347` n `46` status `ready` deltaP `37.0471` edge `0.4405` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8405` n `88` status `ready` deltaP `2.2727` edge `0.5711` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1506` n `88` status `ready` deltaP `14.9114` edge `0.0811` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3461` n `88` status `ready` deltaP `18.0848` edge `0.0098` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2649` n `88` status `ready` deltaP `5.9812` edge `0.0238` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4491` n `88` status `ready` deltaP `1.8781` edge `-0.0167` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4976` n `88` status `ready` deltaP `5.5017` edge `0.023` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5105` n `88` status `ready` deltaP `-1.1704` edge `-0.0082` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9647` n `88` status `ready` deltaP `3.2567` edge `-0.0064` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2443` n `88` status `ready` deltaP `-3.3206` edge `-0.0105` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5222` n `88` status `ready` deltaP `5.9132` edge `-0.081` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.7168` n `46` status `ready` deltaP `-4.5743` edge `0.008` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7947` n `88` status `ready` deltaP `-9.2018` edge `-0.0433` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3356` n `88` status `ready` deltaP `3.0485` edge `-0.2536` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.584` n `88` status `ready` deltaP `-12.5` edge `-0.078` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8511` n `46` status `ready` deltaP `-23.9885` edge `-0.1275` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.4712` n `88` status `ready` deltaP `1.3996` edge `-0.3059` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
