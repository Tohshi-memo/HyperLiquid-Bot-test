# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T13:37:32.267090+00:00`
- Price records: `672`
- Market context records: `7569`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14496`

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

- `market_context_high->commodity_4h` score `0.1881` n `169` status `ready` deltaP `9.3119` edge `0.0296` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1356` n `169` status `ready` deltaP `5.2331` edge `0.0073` maxDD `-1.7657`
- `market_context_high->commodity_24h` score `-0.2324` n `153` status `ready` deltaP `12.4024` edge `0.0563` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.2851` n `169` status `ready` deltaP `1.9476` edge `0.0004` maxDD `-0.6615`
- `market_context_high->commodity_1h` score `-0.3129` n `169` status `ready` deltaP `4.2521` edge `0.0028` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.5094` n `169` status `ready` deltaP `11.1793` edge `0.0328` maxDD `-3.4775`
- `market_context_high->unknown_4h` score `-0.7308` n `169` status `ready` deltaP `10.5715` edge `0.0717` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-0.771` n `169` status `ready` deltaP `1.7858` edge `-0.0138` maxDD `-1.3217`
- `market_context_high->crypto_major_1h` score `-0.7711` n `169` status `ready` deltaP `4.7373` edge `0.0106` maxDD `-7.6171`
- `market_context_high->metal_1h` score `-0.7763` n `169` status `ready` deltaP `0.039` edge `0.0106` maxDD `-1.4971`
- `market_context_high->crypto_alt_1h` score `-0.7844` n `169` status `ready` deltaP `-0.4314` edge `0.0062` maxDD `-5.9775`
- `market_context_high->fx_24h` score `-0.8276` n `153` status `ready` deltaP `8.9488` edge `0.0154` maxDD `-3.8554`
- `market_context_high->unknown_24h` score `-1.3952` n `154` status `ready` deltaP `5.4631` edge `0.0596` maxDD `-9.9917`
- `market_context_high->metal_4h` score `-1.5022` n `169` status `ready` deltaP `0.8253` edge `0.0501` maxDD `-4.8549`
- `market_context_high->equity_1h` score `-1.5048` n `169` status `ready` deltaP `3.608` edge `0.0241` maxDD `-14.6193`
- `market_context_high->crypto_alt_4h` score `-1.8964` n `169` status `ready` deltaP `0.0451` edge `0.0305` maxDD `-15.2477`
- `market_context_high->fx_4h` score `-2.0364` n `169` status `ready` deltaP `-0.5157` edge `0.0022` maxDD `-2.1439`
- `market_context_high->equity_4h` score `-2.2655` n `169` status `ready` deltaP `3.068` edge `0.1884` maxDD `-26.9444`
- `market_context_high->crypto_major_4h` score `-2.5459` n `169` status `ready` deltaP `4.3395` edge `0.0341` maxDD `-23.4879`
- `market_context_high->index_24h` score `-4.1238` n `153` status `ready` deltaP `-19.7604` edge `-0.0058` maxDD `-16.6255`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
