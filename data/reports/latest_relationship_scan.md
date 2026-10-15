# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T01:07:30.963602+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9422`

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

- `market_context_high->crypto_alt_4h` score `7.2971` n `117` status `ready` deltaP `19.051` edge `0.6255` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.2786` n `54` status `ready` deltaP `37.2822` edge `0.358` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.2786` n `54` status `ready` deltaP `37.2822` edge `0.358` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2968` n `117` status `ready` deltaP `21.4249` edge `0.5378` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.8924` n `54` status `ready` deltaP `21.3302` edge `0.3935` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.8924` n `54` status `ready` deltaP `21.3302` edge `0.3935` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6327` n `54` status `ready` deltaP `34.5303` edge `0.449` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6327` n `54` status `ready` deltaP `34.5303` edge `0.449` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.9427` n `117` status `ready` deltaP `14.6144` edge `0.1709` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.261` n `117` status `ready` deltaP `5.6618` edge `0.1479` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5336` n `117` status `ready` deltaP `14.9847` edge `0.0491` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2919` n `117` status `ready` deltaP `8.1632` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3367` n `54` status `ready` deltaP `1.1034` edge `0.0217` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3367` n `54` status `ready` deltaP `1.1034` edge `0.0217` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3575` n `117` status `ready` deltaP `1.0973` edge `0.0009` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.4041` n `54` status `ready` deltaP `2.7501` edge `0.003` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4041` n `54` status `ready` deltaP `2.7501` edge `0.003` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4341` n `54` status `ready` deltaP `2.5915` edge `0.0316` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4341` n `54` status `ready` deltaP `2.5915` edge `0.0316` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.465` n `54` status `ready` deltaP `4.358` edge `0.0136` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
