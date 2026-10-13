# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T07:22:31.389542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9774`

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

- `market_context_high->crypto_alt_4h` score `7.6195` n `117` status `ready` deltaP `19.3559` edge `0.6508` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.8043` n `117` status `ready` deltaP `23.2541` edge `0.5679` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.2083` n `54` status `ready` deltaP `21.6351` edge `0.4179` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.2083` n `54` status `ready` deltaP `21.6351` edge `0.4179` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3494` n `48` status `ready` deltaP `30.087` edge `0.2452` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3494` n `48` status `ready` deltaP `30.087` edge `0.2452` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9626` n `54` status `ready` deltaP `36.3595` edge `0.4791` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9626` n `54` status `ready` deltaP `36.3595` edge `0.4791` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.7212` n `117` status `ready` deltaP `-3.3146` edge `0.3135` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8419` n `117` status `ready` deltaP `13.4168` edge `0.1708` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4204` n `117` status `ready` deltaP `7.1588` edge `0.1512` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0596` n `117` status `ready` deltaP `12.2408` edge `0.0279` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2331` n `54` status `ready` deltaP `2.6004` edge `0.025` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2331` n `54` status `ready` deltaP `2.6004` edge `0.025` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3323` n `117` status `ready` deltaP `1.2474` edge `0.002` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.5279` n `117` status `ready` deltaP `5.768` edge `0.0045` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5328` n `117` status `ready` deltaP `1.2243` edge `-0.0017` maxDD `-1.3154`
- `risk_on_high->crypto_alt_1h` score `-0.536` n `54` status `ready` deltaP `3.1604` edge `0.0128` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.536` n `54` status `ready` deltaP `3.1604` edge `0.0128` maxDD `-5.8734`
- `risk_on_high->metal_1h` score `-0.5575` n `54` status `ready` deltaP `0.3549` edge `-0.0007` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
