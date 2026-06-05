# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T20:37:24.466231+00:00`
- Price records: `672`
- Market context records: `3004`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `19.6071` n `98` status `ready` deltaP `7.1995` edge `1.9776` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5416` n `98` status `ready` deltaP `42.6411` edge `0.7719` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.1058` n `98` status `ready` deltaP `19.4374` edge `0.9257` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.7462` n `98` status `ready` deltaP `18.1725` edge `0.8914` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.0345` n `98` status `ready` deltaP `17.7828` edge `0.4824` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2873` n `102` status `ready` deltaP `17.1479` edge `0.141` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.5309` n `102` status `ready` deltaP `19.1057` edge `0.1286` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.1381` n `102` status `ready` deltaP `14.3592` edge `0.1922` maxDD `-9.0276`
- `market_context_high->commodity_1h` score `-0.0973` n `108` status `ready` deltaP `0.9537` edge `0.0185` maxDD `-0.9706`
- `market_context_high->crypto_alt_4h` score `-0.2714` n `102` status `ready` deltaP `22.6536` edge `0.3643` maxDD `-38.3432`
- `market_context_high->equity_1h` score `-0.2745` n `108` status `ready` deltaP `4.4134` edge `0.0375` maxDD `-5.1694`
- `market_context_high->index_1h` score `-0.3024` n `108` status `ready` deltaP `4.4522` edge `0.0181` maxDD `-3.5907`
- `market_context_high->fx_1h` score `-0.4079` n `108` status `ready` deltaP `-2.4507` edge `0.0006` maxDD `-0.2577`
- `market_context_high->crypto_alt_1h` score `-0.8272` n `108` status `ready` deltaP `6.7809` edge `0.0617` maxDD `-14.7034`
- `market_context_high->fx_4h` score `-1.1149` n `102` status `ready` deltaP `-9.8039` edge `0.0003` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-1.3117` n `108` status `ready` deltaP `4.2193` edge `0.03` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-1.3559` n `102` status `ready` deltaP `-0.8489` edge `-0.002` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.5764` n `108` status `ready` deltaP `1.4582` edge `-0.068` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9105` n `98` status `ready` deltaP `-6.8275` edge `-0.0265` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-2.0369` n `108` status `ready` deltaP `-3.8146` edge `-0.0133` maxDD `-6.8143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
