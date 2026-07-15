# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T13:22:32.691443+00:00`
- Price records: `672`
- Market context records: `6820`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `0.8616` n `176` status `ready` deltaP `-1.5467` edge `0.496` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3431` n `176` status `ready` deltaP `10.9217` edge `0.1426` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2399` n `201` status `ready` deltaP `6.1042` edge `0.0253` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3598` n `201` status `ready` deltaP `3.6651` edge `0.022` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3885` n `201` status `ready` deltaP `-0.1959` edge `0.0` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.7739` n `201` status `ready` deltaP `-3.2383` edge `-0.0034` maxDD `-0.9382`
- `market_context_high->metal_1h` score `-0.9462` n `201` status `ready` deltaP `-5.915` edge `-0.008` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0529` n `201` status `ready` deltaP `-2.0452` edge `-0.0058` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.327` n `189` status `ready` deltaP `5.7524` edge `-0.0021` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.387` n `189` status `ready` deltaP `-2.7213` edge `-0.0107` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6146` n `189` status `ready` deltaP `2.4713` edge `-0.0273` maxDD `-6.3606`
- `market_context_high->equity_1h` score `-1.6264` n `201` status `ready` deltaP `0.6845` edge `-0.0274` maxDD `-4.6821`
- `market_context_high->unknown_1h` score `-1.7079` n `201` status `ready` deltaP `-5.2678` edge `-0.0171` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.7954` n `189` status `ready` deltaP `-4.6595` edge `-0.029` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1774` n `189` status `ready` deltaP `-0.4702` edge `-0.0715` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.3669` n `189` status `ready` deltaP `-0.9904` edge `-0.0667` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4215` n `189` status `ready` deltaP `-12.8202` edge `0.0369` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4624` n `176` status `ready` deltaP `-9.7853` edge `-0.003` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.9352` n `189` status `ready` deltaP `-0.0846` edge `-0.1783` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6282` n `176` status `ready` deltaP `-21.9697` edge `-0.2394` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
