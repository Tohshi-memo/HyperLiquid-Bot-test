# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T11:37:26.222912+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12066`

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

- `market_context_high->unknown_24h` score `3507.5686` n `109` status `ready` deltaP `13.6165` edge `292.2118` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `496.1749` n `60` status `ready` deltaP `15.4514` edge `41.2449` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `496.1749` n `60` status `ready` deltaP `15.4514` edge `41.2449` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1469` n `82` status `ready` deltaP `-4.0529` edge `31.9981` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.401` n `59` status `ready` deltaP `54.505` edge `1.7601` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `19.8784` n `60` status `ready` deltaP `40.2778` edge `1.411` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.8784` n `60` status `ready` deltaP `40.2778` edge `1.411` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5582` n `59` status `ready` deltaP `29.967` edge `1.3122` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `16.9773` n `109` status `ready` deltaP `33.9322` edge `1.2713` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.2519` n `59` status `ready` deltaP `33.9366` edge `0.8046` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9453` n `60` status `ready` deltaP `37.3264` edge `0.4966` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9453` n `60` status `ready` deltaP `37.3264` edge `0.4966` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6561` n `109` status `ready` deltaP `37.3264` edge `0.4725` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.3861` n `59` status `ready` deltaP `53.6458` edge `0.3412` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.3397` n `60` status `ready` deltaP `41.9613` edge `0.4524` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.3397` n `60` status `ready` deltaP `41.9613` edge `0.4524` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9069` n `59` status `ready` deltaP `51.4713` edge `0.3251` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.9149` n `60` status `ready` deltaP `49.8611` edge `0.0814` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9149` n `60` status `ready` deltaP `49.8611` edge `0.0814` maxDD `-0.0051`
- `risk_on_high->crypto_major_4h` score `4.3627` n `60` status `ready` deltaP `22.7439` edge `0.2978` maxDD `-3.8693`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
