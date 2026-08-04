# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T18:19:47.089953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `25.5374` n `62` status `ready` deltaP `20.9565` edge `1.9927` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4363` n `89` status `ready` deltaP `1.24` edge `0.5443` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `2.0803` n `62` status `ready` deltaP `15.3617` edge `0.1773` maxDD `-3.1751`
- `market_context_high->commodity_4h` score `1.293` n `89` status `ready` deltaP `15.9872` edge `0.0858` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.1994` n `90` status `ready` deltaP `5.1929` edge `0.0236` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1758` n `90` status `ready` deltaP `7.9042` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1541` n `89` status `ready` deltaP `14.677` edge `0.0079` maxDD `-1.8797`
- `market_context_high->fx_24h` score `-0.1914` n `62` status `ready` deltaP `9.319` edge `0.0425` maxDD `-4.3126`
- `market_context_high->commodity_24h` score `-0.2967` n `62` status `ready` deltaP `18.5596` edge `0.1219` maxDD `-17.3601`
- `market_context_high->index_1h` score `-0.5479` n `90` status `ready` deltaP `0.2928` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.569` n `90` status `ready` deltaP `-2.0559` edge `-0.0098` maxDD `-1.6224`
- `market_context_high->metal_24h` score `-0.5754` n `62` status `ready` deltaP `-11.2847` edge `0.1183` maxDD `-2.6802`
- `market_context_high->crypto_alt_1h` score `-0.7273` n `90` status `ready` deltaP `-2.3087` edge `-0.0068` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7517` n `89` status `ready` deltaP `2.5949` edge `0.0098` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8588` n `89` status `ready` deltaP `4.3334` edge `0.0` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7461` n `90` status `ready` deltaP `4.2016` edge `-0.0983` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0055` n `89` status `ready` deltaP `-11.6505` edge `-0.054` maxDD `-4.7021`
- `market_context_high->index_24h` score `-3.231` n `62` status `ready` deltaP `-15.5018` edge `-0.0914` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4739` n `90` status `ready` deltaP `-12.159` edge `-0.0711` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4756` n `90` status `ready` deltaP `2.1989` edge `-0.2596` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
