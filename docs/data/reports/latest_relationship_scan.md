# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T18:37:31.287098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `8.0646` n `60` status `ready` deltaP `27.0139` edge `1.273` maxDD `-27.8667`
- `risk_on_high->crypto_alt_4h` score `4.4474` n `48` status `ready` deltaP `19.2582` edge `0.287` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.4474` n `48` status `ready` deltaP `19.2582` edge `0.287` maxDD `-1.9151`
- `market_context_high->crypto_alt_24h` score `4.0665` n `60` status `ready` deltaP `15.0347` edge `1.0176` maxDD `-41.7191`
- `risk_on_high->crypto_major_4h` score `3.775` n `48` status `ready` deltaP `33.8923` edge `0.3433` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.775` n `48` status `ready` deltaP `33.8923` edge `0.3433` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.7455` n `100` status `ready` deltaP `14.3415` edge `0.3614` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.4172` n `100` status `ready` deltaP `17.7256` edge `0.3225` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5825` n `100` status `ready` deltaP `11.9042` edge `0.1476` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9611` n `48` status `ready` deltaP `6.2375` edge `0.0982` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9611` n `48` status `ready` deltaP `6.2375` edge `0.0982` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.9121` n `100` status `ready` deltaP `-3.7744` edge `0.1658` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.6764` n `100` status `ready` deltaP `4.3473` edge `0.1037` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.428` n `48` status `ready` deltaP `5.514` edge `0.0834` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.428` n `48` status `ready` deltaP `5.514` edge `0.0834` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0258` n `100` status `ready` deltaP `4.9009` edge `0.0037` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1489` n `100` status `ready` deltaP `5.9521` edge `0.004` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2824` n `100` status `ready` deltaP `9.2195` edge `0.0103` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3315` n `48` status `ready` deltaP `3.1188` edge `0.0035` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3315` n `48` status `ready` deltaP `3.1188` edge `0.0035` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
