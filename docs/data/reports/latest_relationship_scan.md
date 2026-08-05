# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T14:52:29.159986+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `13.711` n `89` status `ready` deltaP `7.557` edge `1.0965` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5629` n `98` status `ready` deltaP `1.5275` edge `0.4696` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5013` n `98` status `ready` deltaP `16.0559` edge `0.1027` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.0352` n `89` status `ready` deltaP `25.7979` edge `0.0813` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8698` n `89` status `ready` deltaP `1.6268` edge `0.2175` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4377` n `100` status `ready` deltaP `7.6467` edge `0.0271` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0012` n `100` status `ready` deltaP `5.7545` edge `-0.0033` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.0822` n `98` status `ready` deltaP `10.3441` edge `0.0065` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5234` n `100` status `ready` deltaP `-1.5389` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6803` n `100` status `ready` deltaP `-2.1317` edge `-0.0196` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8811` n `98` status `ready` deltaP `1.7266` edge `-0.001` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-1.5126` n `100` status `ready` deltaP `-4.6946` edge `-0.0237` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.5136` n `89` status `ready` deltaP `0.5032` edge `-0.0531` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.7059` n `98` status `ready` deltaP `-2.0284` edge `-0.0662` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7781` n `100` status `ready` deltaP `2.6707` edge `-0.0922` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0252` n `98` status `ready` deltaP `-11.2805` edge `-0.059` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5909` n `89` status `ready` deltaP `-11.9968` edge `-0.0327` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.0939` n `100` status `ready` deltaP `5.6048` edge `-0.2505` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5439` n `100` status `ready` deltaP `-12.4491` edge `-0.075` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-5.9944` n `89` status `ready` deltaP `11.1716` edge `-0.028` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
