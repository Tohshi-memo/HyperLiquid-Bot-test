# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T21:52:25.847112+00:00`
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

- `market_context_high->unknown_24h` score `19.4231` n `76` status `ready` deltaP `18.8231` edge `1.4974` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3833` n `90` status `ready` deltaP `1.7479` edge `0.5365` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5678` n `90` status `ready` deltaP `17.2324` edge `0.1004` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7343` n `76` status `ready` deltaP `-2.0742` edge `0.2248` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6568` n `76` status `ready` deltaP `19.6911` edge `0.0735` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2594` n `90` status `ready` deltaP `5.4923` edge `0.0266` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1274` n `90` status `ready` deltaP `14.2243` edge `0.0075` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1111` n `90` status `ready` deltaP `7.1557` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->crypto_alt_24h` score `-0.3131` n `76` status `ready` deltaP `4.8702` edge `0.0717` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.541` n `90` status `ready` deltaP `-1.6068` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5448` n `90` status `ready` deltaP `0.2928` edge `-0.0184` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7156` n `90` status `ready` deltaP `-2.159` edge `-0.0063` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7243` n `90` status `ready` deltaP `3.0318` edge `0.0104` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9034` n `90` status `ready` deltaP `3.7906` edge `-0.0021` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6378` n `90` status `ready` deltaP `4.9501` edge `-0.0894` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0123` n `90` status `ready` deltaP `-11.8259` edge `-0.0537` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.0911` n `76` status `ready` deltaP `-8.2511` edge `0.0064` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3637` n `90` status `ready` deltaP `-11.2608` edge `-0.0679` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4492` n `90` status `ready` deltaP `1.8995` edge `-0.2554` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-4.3059` n `76` status `ready` deltaP `8.8085` edge `-0.0553` maxDD `-34.4368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
