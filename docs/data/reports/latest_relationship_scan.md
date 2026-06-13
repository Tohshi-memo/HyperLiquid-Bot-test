# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T00:37:30.764646+00:00`
- Price records: `672`
- Market context records: `3738`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.725` n `32` status `ready` deltaP `29.6875` edge `2.2001` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.725` n `32` status `ready` deltaP `29.6875` edge `2.2001` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.2555` n `32` status `ready` deltaP `33.3333` edge `1.6324` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.2555` n `32` status `ready` deltaP `33.3333` edge `1.6324` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.2181` n `32` status `ready` deltaP `30.9028` edge `1.5773` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.2181` n `32` status `ready` deltaP `30.9028` edge `1.5773` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5304` n `32` status `ready` deltaP `31.9444` edge `0.7479` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5304` n `32` status `ready` deltaP `31.9444` edge `0.7479` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2819` n `32` status `ready` deltaP `18.2927` edge `0.8471` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2819` n `32` status `ready` deltaP `18.2927` edge `0.8471` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.8004` n `156` status `ready` deltaP `18.5897` edge `0.6655` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.361` n `156` status `ready` deltaP `26.1752` edge `0.3862` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.5345` n `156` status `ready` deltaP `6.5304` edge `0.7807` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.4008` n `156` status `ready` deltaP `26.656` edge `0.3322` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `1.737` n `32` status `ready` deltaP `-0.2287` edge `0.3307` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.737` n `32` status `ready` deltaP `-0.2287` edge `0.3307` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.535` n `32` status `ready` deltaP `15.2778` edge `0.0522` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.535` n `32` status `ready` deltaP `15.2778` edge `0.0522` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.433` n `170` status `ready` deltaP `8.3662` edge `0.2537` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.3407` n `32` status `ready` deltaP `7.8506` edge `0.233` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
