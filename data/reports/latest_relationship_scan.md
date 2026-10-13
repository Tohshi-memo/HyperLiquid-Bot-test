# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T08:37:38.103522+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9732`

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
- `market_context_high->crypto_major_4h` score `6.8067` n `117` status `ready` deltaP `23.2541` edge `0.5681` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.2083` n `54` status `ready` deltaP `21.6351` edge `0.4179` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.2083` n `54` status `ready` deltaP `21.6351` edge `0.4179` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.4046` n `48` status `ready` deltaP `30.087` edge `0.2498` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4046` n `48` status `ready` deltaP `30.087` edge `0.2498` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9641` n `54` status `ready` deltaP `36.3595` edge `0.4793` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9641` n `54` status `ready` deltaP `36.3595` edge `0.4793` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.6766` n `117` status `ready` deltaP `-3.467` edge `0.3108` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.933` n `117` status `ready` deltaP `14.0156` edge `0.1744` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4468` n `117` status `ready` deltaP `7.3085` edge `0.1524` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.062` n `117` status `ready` deltaP `12.2408` edge `0.0281` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.216` n `54` status `ready` deltaP `2.7501` edge `0.0262` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.216` n `54` status `ready` deltaP `2.7501` edge `0.0262` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3443` n `117` status `ready` deltaP `1.0973` edge `0.002` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.4768` n `54` status `ready` deltaP `3.7592` edge `0.0164` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4768` n `54` status `ready` deltaP `3.7592` edge `0.0164` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.5135` n `117` status `ready` deltaP `5.9177` edge `0.0047` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5422` n `117` status `ready` deltaP `1.0741` edge `-0.0019` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5482` n `54` status `ready` deltaP `0.5046` edge `-0.0005` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
