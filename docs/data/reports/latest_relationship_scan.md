# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T08:37:26.595618+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10130`

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

- `market_context_high->unknown_4h` score `34.3579` n `119` status `ready` deltaP `-2.2508` edge `2.9428` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `11.3344` n `52` status `ready` deltaP `22.476` edge `1.5487` maxDD `-12.9661`
- `market_context_high->crypto_alt_24h` score `9.3221` n `52` status `ready` deltaP `10.8441` edge `1.4475` maxDD `-19.3056`
- `risk_on_high->crypto_alt_4h` score `3.8109` n `51` status `ready` deltaP `19.3269` edge `0.2335` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8109` n `51` status `ready` deltaP `19.3269` edge `0.2335` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4536` n `51` status `ready` deltaP `33.441` edge `0.3051` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4536` n `51` status `ready` deltaP `33.441` edge `0.3051` maxDD `-4.1548`
- `market_context_high->equity_24h` score `3.0002` n `52` status `ready` deltaP `8.7206` edge `0.4668` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.9954` n `52` status `ready` deltaP `28.2852` edge `0.1233` maxDD `-0.4833`
- `risk_on_high->crypto_alt_1h` score `1.2258` n `51` status `ready` deltaP `7.3412` edge `0.1129` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.2258` n `51` status `ready` deltaP `7.3412` edge `0.1129` maxDD `-2.4421`
- `market_context_high->crypto_alt_1h` score `0.9299` n `119` status `ready` deltaP `7.9014` edge `0.1199` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.7378` n `119` status `ready` deltaP `11.032` edge `0.2316` maxDD `-11.1784`
- `market_context_high->unknown_1h` score `0.7264` n `119` status `ready` deltaP `-5.1502` edge `0.1285` maxDD `-1.024`
- `risk_on_high->crypto_major_1h` score `0.5676` n `51` status `ready` deltaP `6.5633` edge `0.0943` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.5676` n `51` status `ready` deltaP `6.5633` edge `0.0943` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.2621` n `119` status `ready` deltaP `3.4821` edge `0.0867` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.0388` n `119` status `ready` deltaP `4.481` edge `0.2292` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.2094` n `119` status `ready` deltaP `4.9552` edge `0.0056` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.2413` n `119` status `ready` deltaP `0.9712` edge `0.0006` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
