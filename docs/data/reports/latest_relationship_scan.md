# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T22:22:43.204690+00:00`
- Price records: `672`
- Market context records: `3729`
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

- `risk_on_high->crypto_major_24h` score `29.0328` n `32` status `ready` deltaP `29.8611` edge `2.2246` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.0328` n `32` status `ready` deltaP `29.8611` edge `2.2246` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.2555` n `32` status `ready` deltaP `33.3333` edge `1.6324` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.2555` n `32` status `ready` deltaP `33.3333` edge `1.6324` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.4341` n `32` status `ready` deltaP `30.9028` edge `1.5953` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.4341` n `32` status `ready` deltaP `30.9028` edge `1.5953` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.6531` n `32` status `ready` deltaP `32.6389` edge `0.7535` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.6531` n `32` status `ready` deltaP `32.6389` edge `0.7535` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.3419` n `32` status `ready` deltaP `18.2927` edge `0.8521` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.3419` n `32` status `ready` deltaP `18.2927` edge `0.8521` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.0004` n `156` status `ready` deltaP `18.5897` edge `0.6655` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.0291` n `156` status `ready` deltaP `24.3056` edge `0.371` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `3.7063` n `156` status `ready` deltaP `6.063` edge `0.7148` maxDD `-31.0425`
- `market_context_high->metal_24h` score `3.5163` n `156` status `ready` deltaP `22.4493` edge `0.3032` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `1.9674` n `32` status `ready` deltaP `-0.2287` edge `0.3499` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.9674` n `32` status `ready` deltaP `-0.2287` edge `0.3499` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.7884` n `32` status `ready` deltaP `16.8403` edge `0.0629` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.7884` n `32` status `ready` deltaP `16.8403` edge `0.0629` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.5535` n `32` status `ready` deltaP `8.6128` edge `0.2552` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5535` n `32` status `ready` deltaP `8.6128` edge `0.2552` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
