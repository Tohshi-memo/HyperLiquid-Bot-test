# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T07:07:29.177898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12876`

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

- `market_context_high->unknown_24h` score `18658.0655` n `55` status `ready` deltaP `13.3775` edge `1554.7548` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.2275` n `82` status `ready` deltaP `-4.9511` edge `31.5108` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.6949` n `82` status `ready` deltaP `31.8851` edge `1.3108` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.6572` n `82` status `ready` deltaP `37.589` edge `1.3679` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.5443` n `55` status `ready` deltaP `48.3554` edge `0.5705` maxDD `-0.8009`
- `market_context_high->crypto_alt_24h` score `9.8473` n `55` status `ready` deltaP `19.8674` edge `0.7709` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.9195` n `82` status `ready` deltaP `19.6858` edge `0.6234` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.3605` n `82` status `ready` deltaP `44.9102` edge `0.2483` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6157` n `82` status `ready` deltaP `24.3987` edge `0.2674` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.299` n `55` status `ready` deltaP `42.1875` edge `0.077` maxDD `0.0`
- `market_context_high->index_24h` score `4.2065` n `55` status `ready` deltaP `44.4003` edge `0.0896` maxDD `-0.1382`
- `market_context_high->metal_24h` score `0.7929` n `55` status `ready` deltaP `11.2058` edge `0.1144` maxDD `-1.9958`
- `news_risk_high->index_4h` score `0.3138` n `82` status `ready` deltaP `10.9756` edge `0.0299` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.2729` n `64` status `ready` deltaP `10.3277` edge `0.1336` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2729` n `64` status `ready` deltaP `10.3277` edge `0.1336` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.1592` n `65` status `ready` deltaP `5.3017` edge `0.0035` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1592` n `65` status `ready` deltaP `5.3017` edge `0.0035` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.2507` n `129` status `ready` deltaP `1.8312` edge `-0.0015` maxDD `-0.5278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
