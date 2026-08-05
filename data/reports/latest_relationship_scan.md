# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T11:07:25.276173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `14.0272` n `89` status `ready` deltaP `9.8139` edge `1.1078` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4203` n `92` status `ready` deltaP `2.2402` edge `0.5363` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7263` n `92` status `ready` deltaP `18.1336` edge `0.1076` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.2135` n `89` status `ready` deltaP `28.402` edge `0.0868` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9111` n `89` status `ready` deltaP `1.6268` edge `0.2228` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4106` n `98` status `ready` deltaP `7.2926` edge `0.0272` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0843` n `92` status `ready` deltaP `13.4411` edge `0.0072` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0599` n `98` status `ready` deltaP `6.4891` edge `-0.0033` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.545` n `98` status `ready` deltaP `-1.7292` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6286` n `98` status `ready` deltaP `-1.3626` edge `-0.0181` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8958` n `92` status `ready` deltaP `1.7431` edge `-0.003` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9316` n `98` status `ready` deltaP `-4.1366` edge `-0.0208` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.38` n `89` status `ready` deltaP `1.1977` edge `-0.0406` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.546` n `92` status `ready` deltaP `-0.7224` edge `-0.0544` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7512` n `98` status `ready` deltaP `2.8138` edge `-0.0897` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1328` n `92` status `ready` deltaP `-13.1694` edge `-0.0602` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3839` n `89` status `ready` deltaP `-10.087` edge `-0.0189` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.2128` n `98` status `ready` deltaP `4.2986` edge `-0.2517` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5865` n `98` status `ready` deltaP `-12.9659` edge `-0.0751` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1289` n `89` status `ready` deltaP `10.1299` edge `-0.0383` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
