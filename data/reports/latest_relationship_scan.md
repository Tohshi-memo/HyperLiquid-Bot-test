# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T14:07:34.282044+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11661`

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

- `market_context_high->unknown_24h` score `13.8067` n `89` status `ready` deltaP `8.0778` edge `1.101` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5761` n `98` status `ready` deltaP `1.5275` edge `0.4707` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4359` n `98` status `ready` deltaP `15.5986` edge `0.1003` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.0794` n `89` status `ready` deltaP `26.3187` edge `0.0835` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8721` n `89` status `ready` deltaP `1.6268` edge `0.2178` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4794` n `99` status `ready` deltaP `7.913` edge `0.0288` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0612` n `99` status `ready` deltaP `6.4901` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.083` n `98` status `ready` deltaP `10.3441` edge `0.0064` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5484` n `99` status `ready` deltaP `-1.8538` edge `-0.0085` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6958` n `99` status `ready` deltaP `-2.4163` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8889` n `98` status `ready` deltaP `1.7266` edge `-0.002` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9284` n `99` status `ready` deltaP `-3.9104` edge `-0.0219` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.5019` n `89` status `ready` deltaP `0.5032` edge `-0.0516` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.7343` n `98` status `ready` deltaP `-2.3333` edge `-0.0678` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8085` n `99` status `ready` deltaP `2.4467` edge `-0.0946` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.026` n `98` status `ready` deltaP `-11.2805` edge `-0.0591` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5909` n `89` status `ready` deltaP `-11.9968` edge `-0.0327` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.0895` n `99` status `ready` deltaP `5.3303` edge `-0.2483` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5677` n `99` status `ready` deltaP `-12.776` edge `-0.0748` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0038` n `89` status `ready` deltaP `11.1716` edge `-0.0292` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
