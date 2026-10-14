# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T19:41:08.044945+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9670`

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

- `market_context_high->crypto_alt_4h` score `7.1807` n `117` status `ready` deltaP `19.051` edge `0.6158` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.6296` n `54` status `ready` deltaP `33.5652` edge `0.3287` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.6296` n `54` status `ready` deltaP `33.5652` edge `0.3287` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2678` n `117` status `ready` deltaP `21.2724` edge `0.5364` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.776` n `54` status `ready` deltaP `21.3302` edge `0.3838` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.776` n `54` status `ready` deltaP `21.3302` edge `0.3838` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6138` n `54` status `ready` deltaP `34.3778` edge `0.4476` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6138` n `54` status `ready` deltaP `34.3778` edge `0.4476` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.776` n `117` status `ready` deltaP `13.5665` edge `0.164` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2538` n `117` status `ready` deltaP `5.8115` edge `0.1463` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.375` n `117` status `ready` deltaP `13.9176` edge `0.043` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2907` n `117` status `ready` deltaP `8.1632` edge `0.0083` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3414` n `54` status `ready` deltaP `1.2531` edge `0.0201` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3414` n `54` status `ready` deltaP `1.2531` edge `0.0201` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3419` n `117` status `ready` deltaP `1.0973` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.7501` edge `0.0031` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.7501` edge `0.0031` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5372` n `54` status `ready` deltaP `1.5244` edge `0.0255` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5372` n `54` status `ready` deltaP `1.5244` edge `0.0255` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.5696` n `117` status `ready` deltaP `0.3234` edge `-0.0004` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
