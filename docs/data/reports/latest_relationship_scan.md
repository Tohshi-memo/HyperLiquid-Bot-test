# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T08:07:31.832655+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9714`

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

- `market_context_high->crypto_alt_4h` score `7.6087` n `117` status `ready` deltaP `19.3559` edge `0.6499` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.7995` n `117` status `ready` deltaP `23.2541` edge `0.5675` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.1975` n `54` status `ready` deltaP `21.6351` edge `0.417` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.1975` n `54` status `ready` deltaP `21.6351` edge `0.417` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3794` n `48` status `ready` deltaP `30.087` edge `0.2477` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3794` n `48` status `ready` deltaP `30.087` edge `0.2477` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9595` n `54` status `ready` deltaP `36.3595` edge `0.4787` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9595` n `54` status `ready` deltaP `36.3595` edge `0.4787` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.6982` n `117` status `ready` deltaP `-3.467` edge `0.3126` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8887` n `117` status `ready` deltaP `13.7162` edge `0.1727` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4228` n `117` status `ready` deltaP `7.1588` edge `0.1514` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0596` n `117` status `ready` deltaP `12.2408` edge `0.0279` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2316` n `54` status `ready` deltaP `2.6004` edge `0.0252` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2316` n `54` status `ready` deltaP `2.6004` edge `0.0252` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3323` n `117` status `ready` deltaP `1.2474` edge `0.002` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.5056` n `54` status `ready` deltaP `3.4598` edge `0.0147` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5056` n `54` status `ready` deltaP `3.4598` edge `0.0147` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.5291` n `117` status `ready` deltaP `5.768` edge `0.0044` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5414` n `117` status `ready` deltaP `1.0741` edge `-0.0018` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5583` n `54` status `ready` deltaP `0.3549` edge `-0.0008` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
