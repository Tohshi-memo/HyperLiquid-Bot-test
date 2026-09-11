# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T17:37:30.646912+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11845`

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

- `news_risk_high->unknown_1h` score `661.1441` n `63` status `ready` deltaP `-4.529` edge `55.1677` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `23.2939` n `91` status `ready` deltaP `41.9013` edge `1.6848` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.2939` n `91` status `ready` deltaP `41.9013` edge `1.6848` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `20.6354` n `153` status `ready` deltaP `36.9383` edge `1.5561` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.5511` n `91` status `ready` deltaP `36.9792` edge `0.5494` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.5511` n `91` status `ready` deltaP `36.9792` edge `0.5494` maxDD `0.0`
- `market_context_high->equity_24h` score `9.2859` n `153` status `ready` deltaP `36.9792` edge `0.5273` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `7.9719` n `91` status `ready` deltaP `40.5739` edge `0.431` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.9719` n `91` status `ready` deltaP `40.5739` edge `0.431` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.2729` n `91` status `ready` deltaP `25.021` edge `1.1724` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2729` n `91` status `ready` deltaP `25.021` edge `1.1724` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.179` n `91` status `ready` deltaP `30.3722` edge `0.3983` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.179` n `91` status `ready` deltaP `30.3722` edge `0.3983` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.482` n `91` status `ready` deltaP `51.5644` edge `0.1173` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.482` n `91` status `ready` deltaP `51.5644` edge `0.1173` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.325` n `153` status `ready` deltaP `43.75` edge `0.1081` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.624` n `91` status `ready` deltaP `34.4127` edge `0.0819` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.624` n `91` status `ready` deltaP `34.4127` edge `0.0819` maxDD `-0.079`
- `market_context_high->crypto_alt_4h` score `3.2506` n `153` status `ready` deltaP `23.4009` edge `0.2854` maxDD `-7.6417`
- `market_context_high->equity_4h` score `2.0256` n `153` status `ready` deltaP `27.2806` edge `0.0696` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
