# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T07:52:25.372557+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12880`

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

- `market_context_high->unknown_24h` score `17051.0849` n `58` status `ready` deltaP `13.5656` edge `1420.8385` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.1915` n `82` status `ready` deltaP `-5.2505` edge `31.5098` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.6702` n `82` status `ready` deltaP `31.7115` edge `1.3099` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.6452` n `82` status `ready` deltaP `37.589` edge `1.3669` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `9.9454` n `58` status `ready` deltaP `21.1985` edge `0.7702` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.9433` n `58` status `ready` deltaP `43.7978` edge `0.513` maxDD `-3.4438`
- `news_risk_high->equity_24h` score `7.0428` n `82` status `ready` deltaP `20.2066` edge `0.6302` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.4129` n `82` status `ready` deltaP `45.431` edge `0.2492` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5644` n `82` status `ready` deltaP `23.8779` edge `0.2666` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2707` n `58` status `ready` deltaP `42.0139` edge `0.0758` maxDD `0.0`
- `market_context_high->index_24h` score `3.7296` n `58` status `ready` deltaP `40.595` edge `0.0805` maxDD `-0.56`
- `market_context_high->metal_24h` score `0.8707` n `58` status `ready` deltaP `12.5658` edge `0.1153` maxDD `-1.9958`
- `news_risk_high->index_4h` score `0.3407` n `82` status `ready` deltaP `11.4329` edge `0.0303` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.2713` n `65` status `ready` deltaP `9.8476` edge `0.1366` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2713` n `65` status `ready` deltaP `9.8476` edge `0.1366` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.146` n `65` status `ready` deltaP `5.152` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.146` n `65` status `ready` deltaP `5.152` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.137` n `65` status `ready` deltaP `3.0147` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.137` n `65` status `ready` deltaP `3.0147` edge `0.0015` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.2309` n `132` status `ready` deltaP `2.0867` edge `-0.0015` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
