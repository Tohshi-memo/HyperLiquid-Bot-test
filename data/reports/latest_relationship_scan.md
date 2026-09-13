# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T00:07:29.564859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12511`

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

- `market_context_high->unknown_24h` score `16568.3726` n `59` status `ready` deltaP `12.0616` edge `1380.6225` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.4752` n `82` status `ready` deltaP `-5.5499` edge `31.9521` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.2481` n `82` status `ready` deltaP `33.1004` edge `1.3488` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.061` n `82` status `ready` deltaP `39.8459` edge `1.3865` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.3496` n `59` status `ready` deltaP `23.055` edge `0.7915` maxDD `-3.9523`
- `market_context_high->equity_24h` score `10.2598` n `59` status `ready` deltaP `45.3125` edge `0.5529` maxDD `0.0`
- `news_risk_high->index_24h` score `6.022` n `82` status `ready` deltaP `41.2644` edge `0.2444` maxDD `-0.0797`
- `news_risk_high->equity_24h` score `6.0026` n `82` status `ready` deltaP `14.8247` edge `0.5794` maxDD `-6.5742`
- `news_risk_high->metal_24h` score `5.0939` n `82` status `ready` deltaP `29.0862` edge `0.276` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2819` n `59` status `ready` deltaP `42.7083` edge `0.0721` maxDD `0.0`
- `market_context_high->index_24h` score `3.9006` n `59` status `ready` deltaP `41.8639` edge `0.0852` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.42` n `59` status `ready` deltaP `9.884` edge `0.1077` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.1088` n `82` status `ready` deltaP `7.3171` edge `0.028` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1033` n `53` status `ready` deltaP `6.1236` edge `0.0008` maxDD `-0.3081`
- `risk_on_high->index_1h` score `-0.0086` n `53` status `ready` deltaP `5.7056` edge `0.0005` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0086` n `53` status `ready` deltaP `5.7056` edge `0.0005` maxDD `-0.1711`
- `risk_on_high->crypto_alt_4h` score `-0.0151` n `51` status `ready` deltaP `6.274` edge `0.1237` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `-0.0151` n `51` status `ready` deltaP `6.274` edge `0.1237` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.0851` n `53` status `ready` deltaP `1.7512` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
