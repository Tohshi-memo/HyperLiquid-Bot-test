# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T08:22:27.964949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10126`

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

- `market_context_high->unknown_4h` score `34.7731` n `119` status `ready` deltaP `-2.2508` edge `2.9774` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `11.0189` n `53` status `ready` deltaP `21.4885` edge `1.5277` maxDD `-13.6617`
- `market_context_high->crypto_alt_24h` score `8.796` n `53` status `ready` deltaP `9.8566` edge `1.4069` maxDD `-20.5936`
- `risk_on_high->crypto_alt_4h` score `4.1548` n `51` status `ready` deltaP `21.1352` edge `0.2501` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.1548` n `51` status `ready` deltaP `21.1352` edge `0.2501` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6178` n `51` status `ready` deltaP `35.2492` edge `0.3141` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6178` n `51` status `ready` deltaP `35.2492` edge `0.3141` maxDD `-4.1548`
- `market_context_high->equity_24h` score `3.04` n `53` status `ready` deltaP `9.3816` edge `0.4675` maxDD `-7.5571`
- `market_context_high->index_24h` score `2.0214` n `53` status `ready` deltaP `28.6196` edge `0.1244` maxDD `-0.4833`
- `risk_on_high->crypto_alt_1h` score `1.3737` n `52` status `ready` deltaP `7.9457` edge `0.1212` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.3737` n `52` status `ready` deltaP `7.9457` edge `0.1212` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.0164` n `52` status `ready` deltaP `7.2432` edge `0.1017` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.0164` n `52` status `ready` deltaP `7.2432` edge `0.1017` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `0.9773` n `120` status `ready` deltaP `8.0739` edge `0.1227` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.8008` n `119` status `ready` deltaP `11.7198` edge `0.2351` maxDD `-11.1784`
- `market_context_high->unknown_1h` score `0.4077` n `120` status `ready` deltaP `-5.6237` edge `0.1051` maxDD `-1.024`
- `market_context_high->crypto_major_1h` score `0.2946` n `120` status `ready` deltaP `3.7176` edge `0.0893` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.1694` n `119` status `ready` deltaP `5.1688` edge `0.2355` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.1886` n `120` status `ready` deltaP `5.1697` edge `0.0059` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.2306` n `120` status `ready` deltaP `1.1926` edge `0.0005` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
