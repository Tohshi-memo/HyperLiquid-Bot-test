# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T22:37:27.816210+00:00`
- Price records: `672`
- Market context records: `3833`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13787`

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

- `risk_on_high->crypto_major_24h` score `32.8186` n `32` status `ready` deltaP `34.0278` edge `2.5123` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.8186` n `32` status `ready` deltaP `34.0278` edge `2.5123` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.3315` n `32` status `ready` deltaP `42.0139` edge `1.9142` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.3315` n `32` status `ready` deltaP `42.0139` edge `1.9142` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5227` n `32` status `ready` deltaP `31.9444` edge `1.7624` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5227` n `32` status `ready` deltaP `31.9444` edge `1.7624` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2816` n `32` status `ready` deltaP `31.25` edge `0.7318` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2816` n `32` status `ready` deltaP `31.25` edge `0.7318` maxDD `0.0`
- `market_context_high->equity_24h` score `6.6498` n `136` status `ready` deltaP `16.2786` edge `0.7486` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.7764` n `136` status `ready` deltaP `26.1029` edge `0.4213` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.3312` n `49` status `ready` deltaP `10.0641` edge `0.4894` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3312` n `49` status `ready` deltaP `10.0641` edge `0.4894` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.1505` n `136` status `ready` deltaP `24.3362` edge `0.3268` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.2751` n `136` status `ready` deltaP `2.594` edge `0.702` maxDD `-31.0425`
- `risk_on_high->equity_4h` score `2.5477` n `49` status `ready` deltaP `19.929` edge `0.1929` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5477` n `49` status `ready` deltaP `19.929` edge `0.1929` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.6057` n `191` status `ready` deltaP `10.1496` edge `0.2562` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.39` n `32` status `ready` deltaP `14.4097` edge `0.0459` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.39` n `32` status `ready` deltaP `14.4097` edge `0.0459` maxDD `-0.7574`
- `market_context_high->equity_4h` score `0.9923` n `191` status `ready` deltaP `11.4879` edge `0.1765` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
