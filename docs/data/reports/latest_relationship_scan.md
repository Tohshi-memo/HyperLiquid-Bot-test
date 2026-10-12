# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T18:07:26.333679+00:00`
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

- `market_context_high->crypto_major_24h` score `9.3036` n `58` status `ready` deltaP `29.023` edge `1.3536` maxDD `-23.3459`
- `market_context_high->crypto_alt_24h` score `5.7512` n `58` status `ready` deltaP `17.0439` edge `1.1359` maxDD `-35.6423`
- `risk_on_high->crypto_alt_4h` score `4.357` n `48` status `ready` deltaP `18.9533` edge `0.2815` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.357` n `48` status `ready` deltaP `18.9533` edge `0.2815` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.7218` n `48` status `ready` deltaP `33.5874` edge `0.3385` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7218` n `48` status `ready` deltaP `33.5874` edge `0.3385` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.6551` n `100` status `ready` deltaP `14.0366` edge `0.3559` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.3352` n `100` status `ready` deltaP `17.4207` edge `0.3177` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6149` n `100` status `ready` deltaP `12.2036` edge `0.1483` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9934` n `48` status `ready` deltaP `6.5369` edge `0.0989` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9934` n `48` status `ready` deltaP `6.5369` edge `0.0989` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.674` n `100` status `ready` deltaP `4.3473` edge `0.1035` maxDD `-3.4384`
- `market_context_high->unknown_4h` score `0.6299` n `100` status `ready` deltaP `-3.9268` edge `0.1433` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `0.4264` n `48` status `ready` deltaP `5.514` edge `0.0832` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4264` n `48` status `ready` deltaP `5.514` edge `0.0832` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0094` n `100` status `ready` deltaP `4.6006` edge `0.0036` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1345` n `100` status `ready` deltaP `6.1018` edge `0.0042` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2836` n `100` status `ready` deltaP `9.2195` edge `0.0102` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3171` n `48` status `ready` deltaP `3.2685` edge `0.0037` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3171` n `48` status `ready` deltaP `3.2685` edge `0.0037` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
