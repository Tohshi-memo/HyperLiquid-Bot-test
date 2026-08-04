# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T17:37:39.586976+00:00`
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

- `market_context_high->unknown_24h` score `27.2069` n `59` status `ready` deltaP `21.3954` edge `2.1289` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3721` n `89` status `ready` deltaP `0.7827` edge `0.542` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `2.9138` n `59` status `ready` deltaP `18.8883` edge `0.2031` maxDD `-2.563`
- `market_context_high->commodity_4h` score `1.2396` n `89` status `ready` deltaP `15.5299` edge `0.0844` maxDD `-2.7703`
- `market_context_high->commodity_24h` score `0.6703` n `59` status `ready` deltaP `21.4012` edge `0.1717` maxDD `-13.9421`
- `market_context_high->commodity_1h` score `0.1994` n `90` status `ready` deltaP `5.1929` edge `0.0236` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1746` n `90` status `ready` deltaP `7.9042` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1635` n `89` status `ready` deltaP `14.8294` edge `0.0081` maxDD `-1.8797`
- `market_context_high->fx_24h` score `-0.4896` n `59` status `ready` deltaP `6.6414` edge `0.0355` maxDD `-4.3126`
- `market_context_high->index_1h` score `-0.5293` n `90` status `ready` deltaP `0.5922` edge `-0.0184` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5776` n `90` status `ready` deltaP `-2.2056` edge `-0.0099` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7172` n `90` status `ready` deltaP `-2.159` edge `-0.0065` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7296` n `89` status `ready` deltaP `2.8998` edge `0.0106` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.858` n `89` status `ready` deltaP `4.3334` edge `0.0001` maxDD `-5.7857`
- `market_context_high->metal_24h` score `-1.0176` n `59` status `ready` deltaP `-13.6535` edge `0.0774` maxDD `-2.6802`
- `market_context_high->equity_1h` score `-1.7297` n `90` status `ready` deltaP `4.3513` edge `-0.0972` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9882` n `89` status `ready` deltaP `-11.498` edge `-0.0528` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.4792` n `90` status `ready` deltaP `2.1989` edge `-0.2599` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4907` n `90` status `ready` deltaP `-12.3087` edge `-0.0715` maxDD `-7.6533`
- `market_context_high->index_24h` score `-3.576` n `59` status `ready` deltaP `-17.6054` edge `-0.1216` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
