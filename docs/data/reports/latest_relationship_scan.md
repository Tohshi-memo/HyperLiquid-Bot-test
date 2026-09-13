# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T18:56:06.660975+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12738`

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

- `market_context_high->unknown_24h` score `17708.4276` n `56` status `ready` deltaP `10.2093` edge `1475.6544` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7811.5779` n `37` status `ready` deltaP `11.0298` edge `650.8978` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7811.5779` n `37` status `ready` deltaP `11.0298` edge `650.8978` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9135` n `82` status `ready` deltaP `-5.2505` edge `35.6533` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6775` n `82` status `ready` deltaP `36.2027` edge `1.3639` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3808` n `82` status `ready` deltaP `38.0236` edge `1.4253` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.3689` n `82` status `ready` deltaP `27.4432` edge `0.7758` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.1457` n `82` status `ready` deltaP `51.2153` edge `0.2717` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7508` n `82` status `ready` deltaP `26.3121` edge `0.2659` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.6058` n `37` status `ready` deltaP `39.8276` edge `0.1183` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6058` n `37` status `ready` deltaP `39.8276` edge `0.1183` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4654` n `56` status `ready` deltaP `39.8276` edge `0.1066` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.5612` n `37` status `ready` deltaP `4.6273` edge `0.4311` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.5612` n `37` status `ready` deltaP `4.6273` edge `0.4311` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.5087` n `56` status `ready` deltaP `5.0616` edge `0.454` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `0.8616` n `37` status `ready` deltaP `29.2871` edge `0.0012` maxDD `-1.8791`
- `risk_on_and_context->fx_24h` score `0.8616` n `37` status `ready` deltaP `29.2871` edge `0.0012` maxDD `-1.8791`
- `market_context_high->commodity_4h` score `0.5322` n `131` status `ready` deltaP `11.9904` edge `0.0109` maxDD `-0.3853`
- `risk_on_high->commodity_4h` score `0.4978` n `59` status `ready` deltaP `10.7483` edge `0.007` maxDD `-0.3069`
- `risk_on_and_context->commodity_4h` score `0.4978` n `59` status `ready` deltaP `10.7483` edge `0.007` maxDD `-0.3069`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
