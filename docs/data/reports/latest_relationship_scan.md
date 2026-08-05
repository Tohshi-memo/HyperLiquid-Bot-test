# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T08:52:27.038709+00:00`
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

- `market_context_high->unknown_24h` score `14.4943` n `88` status `ready` deltaP `11.3636` edge `1.1364` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5821` n `90` status `ready` deltaP `1.4431` edge `0.5551` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5872` n `90` status `ready` deltaP `17.3849` edge `0.101` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.168` n `88` status `ready` deltaP `27.5568` edge `0.0866` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9249` n `88` status `ready` deltaP `1.231` edge `0.2272` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2571` n `92` status `ready` deltaP `5.5845` edge `0.0258` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0616` n `90` status `ready` deltaP `13.0048` edge `0.0072` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4726` n `92` status `ready` deltaP `-0.5923` edge `-0.0072` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5809` n `92` status `ready` deltaP `-0.3254` edge `-0.0189` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8593` n `92` status `ready` deltaP `-3.3325` edge `-0.0169` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.9238` n `90` status `ready` deltaP `1.355` edge `-0.004` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2451` n `88` status `ready` deltaP `2.3517` edge `-0.031` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.4373` n `90` status `ready` deltaP `0.437` edge `-0.0482` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7354` n `92` status `ready` deltaP `3.6124` edge `-0.093` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0672` n `90` status `ready` deltaP `-12.2832` edge `-0.0577` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2225` n `88` status `ready` deltaP `-8.933` edge `-0.0059` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.342` n `92` status `ready` deltaP `-10.8696` edge `-0.0687` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.3423` n `92` status `ready` deltaP `2.4408` edge `-0.2501` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.1749` n `88` status `ready` deltaP `9.0909` edge `-0.0561` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
