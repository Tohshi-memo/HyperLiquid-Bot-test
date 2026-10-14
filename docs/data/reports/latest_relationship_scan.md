# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T18:22:29.417059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9370`

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

- `market_context_high->crypto_alt_4h` score `7.1591` n `117` status `ready` deltaP `19.051` edge `0.614` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.4353` n `54` status `ready` deltaP `32.6957` edge `0.3183` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.4353` n `54` status `ready` deltaP `32.6957` edge `0.3183` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2496` n `117` status `ready` deltaP `21.12` edge `0.5359` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.7544` n `54` status `ready` deltaP `21.3302` edge `0.382` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.7544` n `54` status `ready` deltaP `21.3302` edge `0.382` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.602` n `54` status `ready` deltaP `34.2254` edge `0.4471` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.602` n `54` status `ready` deltaP `34.2254` edge `0.4471` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7604` n `117` status `ready` deltaP `13.5665` edge `0.1627` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2454` n `117` status `ready` deltaP `5.8115` edge `0.1456` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.369` n `117` status `ready` deltaP `13.9176` edge `0.0425` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2715` n `117` status `ready` deltaP `8.3129` edge `0.0089` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3469` n `54` status `ready` deltaP `1.2531` edge `0.0194` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3469` n `54` status `ready` deltaP `1.2531` edge `0.0194` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3792` n `117` status `ready` deltaP `0.6468` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.3909` n `54` status `ready` deltaP `2.8998` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3909` n `54` status `ready` deltaP `2.8998` edge `0.0037` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5411` n `54` status `ready` deltaP `1.5244` edge `0.025` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5411` n `54` status `ready` deltaP `1.5244` edge `0.025` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.5696` n `117` status `ready` deltaP `0.3234` edge `-0.0004` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
