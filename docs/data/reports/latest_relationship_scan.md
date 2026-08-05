# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T09:37:32.733676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.4275` n `88` status `ready` deltaP `10.8428` edge `1.1343` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4395` n `92` status `ready` deltaP `2.2402` edge `0.5379` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7059` n `92` status `ready` deltaP `18.1336` edge `0.1059` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1785` n `88` status `ready` deltaP `27.7304` edge `0.0868` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8859` n `88` status `ready` deltaP `1.231` edge `0.2222` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2751` n `92` status `ready` deltaP `5.7342` edge `0.0263` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0859` n `92` status `ready` deltaP `13.4411` edge `0.0074` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4711` n `92` status `ready` deltaP `-0.5923` edge `-0.007` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.57` n `92` status `ready` deltaP `-0.1757` edge `-0.0185` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8383` n `92` status `ready` deltaP `-3.0331` edge `-0.0162` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.8966` n `92` status `ready` deltaP `1.7431` edge `-0.0031` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.312` n `88` status `ready` deltaP `1.8308` edge `-0.0361` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5203` n `92` status `ready` deltaP `-0.7224` edge `-0.0511` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7011` n `92` status `ready` deltaP `3.9118` edge `-0.0906` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1361` n `92` status `ready` deltaP `-13.3219` edge `-0.0596` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2956` n `88` status `ready` deltaP `-9.4539` edge `-0.0118` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3228` n `92` status `ready` deltaP `-10.7199` edge `-0.0681` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.3495` n `92` status `ready` deltaP `2.5905` edge `-0.2517` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0643` n `88` status `ready` deltaP `9.6117` edge `-0.0454` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
