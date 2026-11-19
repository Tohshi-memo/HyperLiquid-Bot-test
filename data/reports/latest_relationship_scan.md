# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T15:22:30.436392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `12270.1507` n `106` status `ready` deltaP `0.6101` edge `1022.5283` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8044.8286` n `102` status `ready` deltaP `-0.3736` edge `670.4333` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `25.1318` n `88` status `ready` deltaP `45.8017` edge `1.8483` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.6396` n `88` status `ready` deltaP `23.3586` edge `1.4758` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8529` n `102` status `ready` deltaP `3.4194` edge `0.4135` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2302` n `102` status `ready` deltaP `4.3341` edge `0.2812` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5061` n `102` status `ready` deltaP `18.5348` edge `0.0476` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.3679` n `88` status `ready` deltaP `18.7184` edge `0.2147` maxDD `-14.7068`
- `market_context_high->crypto_major_1h` score `-0.2364` n `106` status `ready` deltaP `4.3272` edge `0.0805` maxDD `-6.5061`
- `market_context_high->metal_1h` score `-0.298` n `106` status `ready` deltaP `4.0871` edge `0.0144` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3193` n `106` status `ready` deltaP `2.3952` edge `0.0043` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.797` n `106` status `ready` deltaP `-2.4263` edge `0.0362` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-0.9448` n `106` status `ready` deltaP `5.2254` edge `0.0219` maxDD `-10.8962`
- `market_context_high->index_4h` score `-1.2406` n `102` status `ready` deltaP `-3.3776` edge `-0.0022` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.5888` n `106` status `ready` deltaP `-11.3518` edge `-0.0016` maxDD `-0.4097`
- `market_context_high->fx_4h` score `-2.3677` n `102` status `ready` deltaP `-14.7537` edge `-0.0036` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4816` n `106` status `ready` deltaP `-10.3181` edge `-0.0302` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.0762` n `88` status `ready` deltaP `-22.9009` edge `-0.0097` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.3794` n `102` status `ready` deltaP `-31.0049` edge `-0.1297` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.4058` n `102` status `ready` deltaP `-8.3901` edge `-0.0602` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
