# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T19:07:26.200622+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `risk_on_high->crypto_alt_24h` score `26.2278` n `36` status `ready` deltaP `51.5625` edge `1.8419` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.2278` n `36` status `ready` deltaP `51.5625` edge `1.8419` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.6793` n `36` status `ready` deltaP `45.4861` edge `1.0867` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.6793` n `36` status `ready` deltaP `45.4861` edge `1.0867` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.6009` n `66` status `ready` deltaP `27.379` edge `0.6604` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.6009` n `66` status `ready` deltaP `27.379` edge `0.6604` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.6895` n `36` status `ready` deltaP `40.1042` edge `0.2901` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.6895` n `36` status `ready` deltaP `40.1042` edge `0.2901` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.3939` n `36` status `ready` deltaP `72.0486` edge `0.0525` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3939` n `36` status `ready` deltaP `72.0486` edge `0.0525` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2542` n `36` status `ready` deltaP `53.4722` edge `0.1647` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2542` n `36` status `ready` deltaP `53.4722` edge `0.1647` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.4857` n `149` status `ready` deltaP `21.054` edge `0.3638` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.3459` n `66` status `ready` deltaP `26.8062` edge `0.2951` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.3459` n `66` status `ready` deltaP `26.8062` edge `0.2951` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5084` n `117` status `ready` deltaP `36.3782` edge `0.2351` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.2839` n `66` status `ready` deltaP `16.3618` edge `0.2962` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.2839` n `66` status `ready` deltaP `16.3618` edge `0.2962` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.6635` n `66` status `ready` deltaP `33.4581` edge `0.1009` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.6635` n `66` status `ready` deltaP `33.4581` edge `0.1009` maxDD `-0.1594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
