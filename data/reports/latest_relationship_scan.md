# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T04:07:30.526849+00:00`
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

- `market_context_high->unknown_24h` score `15.1158` n `88` status `ready` deltaP `14.6622` edge `1.1662` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.7037` n `90` status `ready` deltaP `2.6626` edge `0.5571` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5471` n `90` status `ready` deltaP `16.9276` edge `0.1007` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.3488` n `88` status `ready` deltaP `3.488` edge `0.2665` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.1248` n `88` status `ready` deltaP `26.8624` edge `0.0857` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3037` n `90` status `ready` deltaP `5.7917` edge `0.0283` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1111` n `90` status `ready` deltaP `7.1557` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0601` n `90` status `ready` deltaP `13.0048` edge `0.007` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5768` n `90` status `ready` deltaP `-1.9062` edge `-0.0118` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6796` n `90` status `ready` deltaP `-1.6533` edge `-0.0227` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7264` n `90` status `ready` deltaP `3.3367` edge `0.0081` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-0.8717` n `88` status `ready` deltaP `5.3031` edge `-0.0028` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-0.8731` n `90` status `ready` deltaP `-3.2069` edge `-0.0195` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.3122` n `90` status `ready` deltaP `1.8089` edge `-0.0413` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.8328` n `88` status `ready` deltaP `-6.3289` edge `0.0267` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.9207` n `90` status `ready` deltaP `2.5549` edge `-0.1097` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1758` n `90` status `ready` deltaP `-13.3502` edge `-0.0645` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3376` n `90` status `ready` deltaP `1.8995` edge `-0.2461` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4117` n `90` status `ready` deltaP `-11.2608` edge `-0.0719` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.8854` n `88` status `ready` deltaP `5.7923` edge `-0.1252` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
