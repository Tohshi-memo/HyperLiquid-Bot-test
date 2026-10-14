# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T02:52:28.406329+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9807`

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

- `market_context_high->crypto_alt_4h` score `6.5741` n `117` status `ready` deltaP `16.4595` edge `0.583` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.25` n `52` status `ready` deltaP `32.0` edge `0.3075` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.25` n `52` status `ready` deltaP `32.0` edge `0.3075` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.0538` n `117` status `ready` deltaP `20.9676` edge `0.5206` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.163` n `54` status `ready` deltaP `18.7387` edge `0.3501` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.163` n `54` status `ready` deltaP `18.7387` edge `0.3501` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.4747` n `54` status `ready` deltaP `34.073` edge `0.4318` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4747` n `54` status `ready` deltaP `34.073` edge `0.4318` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.4537` n `117` status `ready` deltaP `-3.6194` edge `0.4599` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.7483` n `117` status `ready` deltaP `13.8659` edge `0.16` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2765` n `117` status `ready` deltaP `6.7097` edge `0.1422` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3106` n `117` status `ready` deltaP `14.2225` edge `0.0356` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3047` n `117` status `ready` deltaP `1.5477` edge `0.0023` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3267` n `54` status `ready` deltaP `2.1513` edge `0.016` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3267` n `54` status `ready` deltaP `2.1513` edge `0.016` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3841` n `117` status `ready` deltaP `7.265` edge `0.0065` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4641` n `54` status `ready` deltaP `1.8519` edge `0.0013` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4641` n `54` status `ready` deltaP `1.8519` edge `0.0013` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5791` n `54` status `ready` deltaP `1.8293` edge `0.0181` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5791` n `54` status `ready` deltaP `1.8293` edge `0.0181` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
