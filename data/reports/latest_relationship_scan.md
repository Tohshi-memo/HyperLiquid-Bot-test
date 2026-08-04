# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T16:44:03.744274+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `29.6382` n `55` status `ready` deltaP `21.9665` edge `2.3277` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.2465` n `89` status `ready` deltaP `0.1729` edge `0.5356` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `4.1525` n `55` status `ready` deltaP `24.1887` edge `0.2458` maxDD `-1.8814`
- `market_context_high->commodity_24h` score `2.0125` n `55` status `ready` deltaP `25.7608` edge `0.2437` maxDD `-9.5944`
- `market_context_high->commodity_4h` score `1.1597` n `89` status `ready` deltaP `14.9201` edge `0.0818` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.2261` n `90` status `ready` deltaP `8.503` edge `-0.003` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1984` n `89` status `ready` deltaP `15.4392` edge `0.0085` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.1778` n `90` status `ready` deltaP `5.0432` edge `0.0228` maxDD `-1.3282`
- `market_context_high->index_1h` score `-0.4911` n `90` status `ready` deltaP `1.191` edge `-0.0175` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5379` n `90` status `ready` deltaP `-1.6068` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.6673` n `90` status `ready` deltaP `-1.7099` edge `-0.0031` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.6792` n `89` status `ready` deltaP `3.5096` edge `0.013` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8209` n `89` status `ready` deltaP `4.7907` edge `0.0018` maxDD `-5.7857`
- `market_context_high->fx_24h` score `-0.9278` n `55` status `ready` deltaP `2.5284` edge `0.0264` maxDD `-4.3126`
- `market_context_high->equity_1h` score `-1.6783` n `90` status `ready` deltaP `4.8004` edge `-0.0936` maxDD `-10.619`
- `market_context_high->metal_24h` score `-1.6809` n `55` status `ready` deltaP `-16.7803` edge `0.0132` maxDD `-2.6802`
- `market_context_high->index_4h` score `-1.9331` n `89` status `ready` deltaP `-10.8883` edge `-0.0498` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.4068` n `90` status `ready` deltaP `-11.8596` edge `-0.0675` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4996` n `90` status `ready` deltaP `2.0492` edge `-0.2606` maxDD `-1.2421`
- `market_context_high->index_24h` score `-4.1108` n `55` status `ready` deltaP `-20.8554` edge `-0.1685` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
