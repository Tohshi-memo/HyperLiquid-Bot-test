# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T18:52:29.274475+00:00`
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

- `market_context_high->unknown_24h` score `17708.4324` n `56` status `ready` deltaP `10.2093` edge `1475.6548` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7811.5851` n `37` status `ready` deltaP `11.0298` edge `650.8984` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7811.5851` n `37` status `ready` deltaP `11.0298` edge `650.8984` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9099` n `82` status `ready` deltaP `-5.2505` edge `35.653` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6763` n `82` status `ready` deltaP `36.2027` edge `1.3638` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3796` n `82` status `ready` deltaP `38.0236` edge `1.4252` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.3689` n `82` status `ready` deltaP `27.4432` edge `0.7758` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.1457` n `82` status `ready` deltaP `51.2153` edge `0.2717` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7508` n `82` status `ready` deltaP `26.3121` edge `0.2659` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.607` n `37` status `ready` deltaP `39.8276` edge `0.1184` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.607` n `37` status `ready` deltaP `39.8276` edge `0.1184` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4654` n `56` status `ready` deltaP `39.8276` edge `0.1066` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.5714` n `37` status `ready` deltaP `4.6273` edge `0.4324` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.5714` n `37` status `ready` deltaP `4.6273` edge `0.4324` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.5149` n `56` status `ready` deltaP `5.0616` edge `0.4548` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `0.8624` n `37` status `ready` deltaP `29.2871` edge `0.0013` maxDD `-1.8791`
- `risk_on_and_context->fx_24h` score `0.8624` n `37` status `ready` deltaP `29.2871` edge `0.0013` maxDD `-1.8791`
- `market_context_high->commodity_4h` score `0.5334` n `131` status `ready` deltaP `11.9904` edge `0.011` maxDD `-0.3853`
- `risk_on_high->commodity_4h` score `0.4978` n `59` status `ready` deltaP `10.7483` edge `0.007` maxDD `-0.3069`
- `risk_on_and_context->commodity_4h` score `0.4978` n `59` status `ready` deltaP `10.7483` edge `0.007` maxDD `-0.3069`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
