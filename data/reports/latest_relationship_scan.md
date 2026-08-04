# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T22:52:25.414247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9857`

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

- `market_context_high->unknown_24h` score `18.0192` n `80` status `ready` deltaP `18.1944` edge `1.3846` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4133` n `90` status `ready` deltaP `1.7479` edge `0.539` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6272` n `90` status `ready` deltaP `17.6897` edge `0.1023` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.0213` n `80` status `ready` deltaP `-0.0347` edge `0.248` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8315` n `80` status `ready` deltaP `22.2569` edge `0.0788` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3145` n `90` status `ready` deltaP `5.9414` edge `0.0282` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1111` n `90` status `ready` deltaP `7.1557` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0941` n `90` status `ready` deltaP `13.6145` edge `0.0073` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.3898` n `80` status `ready` deltaP `6.2153` edge `0.0529` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5597` n `90` status `ready` deltaP `-1.9062` edge `-0.0096` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5736` n `90` status `ready` deltaP `-0.1563` edge `-0.0191` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7038` n `90` status `ready` deltaP `3.3367` edge `0.011` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7523` n `90` status `ready` deltaP `-2.4584` edge `-0.009` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-0.9708` n `90` status `ready` deltaP `3.3333` edge `-0.0077` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7165` n `90` status `ready` deltaP `4.3513` edge `-0.0955` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9054` n `80` status `ready` deltaP `-6.8403` edge `0.0208` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.0255` n `90` status `ready` deltaP `-11.8259` edge `-0.0554` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.4069` n `90` status `ready` deltaP `-11.2608` edge `-0.0715` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4252` n `90` status `ready` deltaP `1.8995` edge `-0.2534` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-5.3113` n `80` status `ready` deltaP `6.8056` edge `-0.0936` maxDD `-39.2828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
