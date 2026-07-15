# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T10:22:28.412643+00:00`
- Price records: `672`
- Market context records: `6807`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8219` n `176` status `ready` deltaP `-1.5467` edge `0.4909` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3403` n `176` status `ready` deltaP `10.2273` edge `0.147` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3146` n `189` status `ready` deltaP `6.2059` edge `0.0184` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.421` n `189` status `ready` deltaP `3.5604` edge `0.0176` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.443` n `189` status `ready` deltaP `-1.1834` edge `-0.0004` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6393` n `189` status `ready` deltaP `-0.9227` edge `-0.0075` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7127` n `189` status `ready` deltaP `-2.6701` edge `-0.0014` maxDD `-0.774`
- `market_context_high->metal_1h` score `-0.7992` n `189` status `ready` deltaP `-6.0356` edge `-0.0051` maxDD `-1.5699`
- `market_context_high->equity_1h` score `-1.3529` n `189` status `ready` deltaP `1.6634` edge `-0.0194` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3817` n `185` status `ready` deltaP `4.7602` edge `-0.0025` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3993` n `185` status `ready` deltaP `-2.5981` edge `-0.0131` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6492` n `185` status `ready` deltaP `1.8375` edge `-0.0277` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.6961` n `189` status `ready` deltaP `-6.1853` edge `-0.01` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.811` n `185` status `ready` deltaP `-6.0094` edge `-0.022` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.276` n `185` status `ready` deltaP `-0.6576` edge `-0.0829` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4738` n `185` status `ready` deltaP `-1.517` edge `-0.0769` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4953` n `185` status `ready` deltaP `-14.1175` edge `0.0394` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4948` n `176` status `ready` deltaP `-9.7853` edge `-0.0057` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.9994` n `185` status `ready` deltaP `-0.81` edge `-0.1817` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.5475` n `176` status `ready` deltaP `-20.9281` edge `-0.236` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
