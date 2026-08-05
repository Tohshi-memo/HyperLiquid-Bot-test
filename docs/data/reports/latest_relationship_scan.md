# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T20:22:50.620533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `12.9028` n `90` status `ready` deltaP `4.4445` edge `1.0499` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.0732` n `106` status `ready` deltaP `-2.3038` edge `0.371` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.392` n `106` status `ready` deltaP `15.5891` edge `0.0967` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.911` n `90` status `ready` deltaP `2.0139` edge `0.2202` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8833` n `90` status `ready` deltaP `24.7223` edge `0.069` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4455` n `109` status `ready` deltaP `7.9094` edge `0.026` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `109` status `ready` deltaP `6.1322` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0556` n `106` status `ready` deltaP `10.5097` edge `0.0088` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5027` n `109` status `ready` deltaP `-1.1111` edge `-0.0076` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7409` n `106` status `ready` deltaP `3.3277` edge `0.0063` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8234` n `109` status `ready` deltaP `-4.5542` edge `-0.0218` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.461` n `90` status `ready` deltaP `0.5555` edge `-0.0467` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.6177` n `109` status `ready` deltaP `-5.2876` edge `-0.0285` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.6316` n `106` status `ready` deltaP `-0.3135` edge `-0.0681` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.9367` n `109` status `ready` deltaP `0.3709` edge `-0.0972` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.245` n `106` status `ready` deltaP `-14.2919` edge `-0.0671` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3437` n `90` status `ready` deltaP `-9.6875` edge `-0.0164` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.483` n `109` status `ready` deltaP `-12.0475` edge `-0.0726` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6616` n `109` status `ready` deltaP `1.5835` edge `-0.271` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0436` n `90` status `ready` deltaP `10.8334` edge `-0.0256` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
