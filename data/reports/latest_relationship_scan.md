# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T05:37:29.590206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `14.9185` n `88` status `ready` deltaP `13.6205` edge `1.1567` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.7159` n `90` status `ready` deltaP `2.815` edge `0.5571` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5641` n `90` status `ready` deltaP `17.08` edge `0.1011` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.2527` n `88` status `ready` deltaP `3.1408` edge `0.2565` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.1468` n `88` status `ready` deltaP `27.2096` edge `0.0862` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2714` n `90` status `ready` deltaP `5.4923` edge `0.0276` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0847` n `90` status `ready` deltaP `6.8563` edge `-0.0038` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0727` n `90` status `ready` deltaP `13.1572` edge `0.0076` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.548` n `90` status `ready` deltaP `-1.4571` edge `-0.0111` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6562` n `90` status `ready` deltaP `-1.3539` edge `-0.0217` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7467` n `90` status `ready` deltaP `3.3367` edge `0.0055` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8653` n `90` status `ready` deltaP `-3.2069` edge `-0.0185` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-0.9437` n `88` status `ready` deltaP `4.6086` edge `-0.0074` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3145` n `90` status `ready` deltaP `1.8089` edge `-0.0416` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8801` n `90` status `ready` deltaP `2.5549` edge `-0.1045` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9187` n `88` status `ready` deltaP `-6.6761` edge `0.018` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1318` n `90` status `ready` deltaP `-13.0454` edge `-0.0609` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.31` n `90` status `ready` deltaP `2.1989` edge `-0.2458` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3805` n `90` status `ready` deltaP `-11.1111` edge `-0.0703` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.6651` n `88` status `ready` deltaP `6.834` edge `-0.1039` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
