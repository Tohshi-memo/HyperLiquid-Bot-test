# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T05:37:27.715760+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9614`

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

- `market_context_high->crypto_alt_4h` score `7.9883` n `117` status `ready` deltaP `19.9656` edge `0.677` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.7934` n `54` status `ready` deltaP `40.4181` edge `0.38` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7934` n `54` status `ready` deltaP `40.4181` edge `0.38` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.5835` n `54` status `ready` deltaP `22.2448` edge `0.445` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.5835` n `54` status `ready` deltaP `22.2448` edge `0.445` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.5543` n `117` status `ready` deltaP `22.0346` edge `0.5552` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.8001` n `54` status `ready` deltaP `35.14` edge `0.4664` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8001` n `54` status `ready` deltaP `35.14` edge `0.4664` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7582` n `120` status `ready` deltaP `13.2685` edge `0.1645` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0114` n `120` status `ready` deltaP `4.4012` edge `0.1355` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3652` n `117` status `ready` deltaP `13.7652` edge `0.0432` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3094` n `54` status `ready` deltaP `1.2531` edge `0.0242` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3094` n `54` status `ready` deltaP `1.2531` edge `0.0242` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.366` n `54` status `ready` deltaP `4.6574` edge `0.0243` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.366` n `54` status `ready` deltaP `4.6574` edge `0.0243` maxDD `-5.8485`
- `market_context_high->metal_1h` score `-0.3865` n `120` status `ready` deltaP `7.1158` edge `0.0073` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.422` n `54` status `ready` deltaP `2.301` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.422` n `54` status `ready` deltaP `2.301` edge `0.0037` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4561` n `120` status `ready` deltaP `0.03` edge `-0.0002` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.4966` n `120` status `ready` deltaP `1.4865` edge `0.0012` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
