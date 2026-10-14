# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T22:37:30.390768+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9421`

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

- `market_context_high->crypto_alt_4h` score `7.3697` n `117` status `ready` deltaP `19.5083` edge `0.6285` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.982` n `54` status `ready` deltaP `35.5401` edge `0.3449` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.982` n `54` status `ready` deltaP `35.5401` edge `0.3449` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3378` n `117` status `ready` deltaP `21.5773` edge `0.5402` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.9649` n `54` status `ready` deltaP `21.7875` edge `0.3965` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.9649` n `54` status `ready` deltaP `21.7875` edge `0.3965` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6593` n `54` status `ready` deltaP `34.6827` edge `0.4514` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6593` n `54` status `ready` deltaP `34.6827` edge `0.4514` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7916` n `117` status `ready` deltaP `13.7162` edge `0.1643` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2071` n `117` status `ready` deltaP `5.3624` edge `0.1454` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4758` n `117` status `ready` deltaP `14.8322` edge `0.0453` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.2927` n `117` status `ready` deltaP `1.6979` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3015` n `117` status `ready` deltaP `8.0135` edge `0.0084` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3718` n `54` status `ready` deltaP `0.804` edge `0.0192` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3718` n `54` status `ready` deltaP `0.804` edge `0.0192` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.4103` n `54` status `ready` deltaP `2.6004` edge `0.0032` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4103` n `54` status `ready` deltaP `2.6004` edge `0.0032` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4717` n `54` status `ready` deltaP `2.439` edge `0.0278` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4717` n `54` status `ready` deltaP `2.439` edge `0.0278` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.5094` n `117` status `ready` deltaP `1.3744` edge `0.0003` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
