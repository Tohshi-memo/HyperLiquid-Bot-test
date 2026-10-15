# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T05:22:30.016054+00:00`
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

- `market_context_high->crypto_alt_4h` score `7.9125` n `117` status `ready` deltaP `19.8132` edge `0.6717` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.7711` n `54` status `ready` deltaP `40.2439` edge `0.3793` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7711` n `54` status `ready` deltaP `40.2439` edge `0.3793` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.5097` n `117` status `ready` deltaP `21.8822` edge `0.5525` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.5077` n `54` status `ready` deltaP `22.0924` edge `0.4397` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.5077` n `54` status `ready` deltaP `22.0924` edge `0.4397` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.7711` n `54` status `ready` deltaP `34.9876` edge `0.4637` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7711` n `54` status `ready` deltaP `34.9876` edge `0.4637` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7222` n `120` status `ready` deltaP `13.1188` edge `0.1625` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9814` n `120` status `ready` deltaP `4.2515` edge `0.134` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3652` n `117` status `ready` deltaP `13.7652` edge `0.0432` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3289` n `54` status `ready` deltaP `1.1034` edge `0.0227` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3289` n `54` status `ready` deltaP `1.1034` edge `0.0227` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3841` n `120` status `ready` deltaP `7.1158` edge `0.0075` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3894` n `54` status `ready` deltaP `4.5077` edge `0.0223` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3894` n `54` status `ready` deltaP `4.5077` edge `0.0223` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4204` n `54` status `ready` deltaP `2.301` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4204` n `54` status `ready` deltaP `2.301` edge `0.0039` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4429` n `120` status `ready` deltaP `0.1801` edge `-0.0001` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.4966` n `120` status `ready` deltaP `1.4865` edge `0.0012` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
