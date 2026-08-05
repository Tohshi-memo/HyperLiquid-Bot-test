# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T04:37:30.156920+00:00`
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

- `market_context_high->unknown_24h` score `15.0521` n `88` status `ready` deltaP `14.315` edge `1.1632` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.7352` n `90` status `ready` deltaP `2.9674` edge `0.5577` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5435` n `90` status `ready` deltaP `16.9276` edge `0.1004` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.3254` n `88` status `ready` deltaP `3.488` edge `0.2635` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.1444` n `88` status `ready` deltaP `27.2096` edge `0.0859` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2726` n `90` status `ready` deltaP `5.4923` edge `0.0277` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0847` n `90` status `ready` deltaP `6.8563` edge `-0.0038` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0696` n `90` status `ready` deltaP `13.1572` edge `0.0072` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5753` n `90` status `ready` deltaP `-1.9062` edge `-0.0116` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6687` n `90` status `ready` deltaP `-1.5036` edge `-0.0223` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7311` n `90` status `ready` deltaP `3.3367` edge `0.0075` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8661` n `90` status `ready` deltaP `-3.2069` edge `-0.0186` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-0.8701` n `88` status `ready` deltaP `5.3031` edge `-0.0026` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3052` n `90` status `ready` deltaP `1.8089` edge `-0.0404` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.8531` n `88` status `ready` deltaP `-6.3289` edge `0.0241` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8988` n `90` status `ready` deltaP `2.5549` edge `-0.1069` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1482` n `90` status `ready` deltaP `-13.0454` edge `-0.063` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3352` n `90` status `ready` deltaP `1.8995` edge `-0.2459` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3817` n `90` status `ready` deltaP `-11.1111` edge `-0.0704` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.8158` n `88` status `ready` deltaP `6.1395` edge `-0.1186` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
