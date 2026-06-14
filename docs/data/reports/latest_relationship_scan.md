# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T12:22:34.190763+00:00`
- Price records: `672`
- Market context records: `3891`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `risk_on_high->unknown_4h` score `47.3507` n `72` status `ready` deltaP `5.7418` edge `6.2465` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.3507` n `72` status `ready` deltaP `5.7418` edge `6.2465` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.5718` n `32` status `ready` deltaP `34.0278` edge `2.6584` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.5718` n `32` status `ready` deltaP `34.0278` edge `2.6584` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9819` n `32` status `ready` deltaP `42.0139` edge `1.9684` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9819` n `32` status `ready` deltaP `42.0139` edge `1.9684` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.4668` n `32` status `ready` deltaP `31.7708` edge `1.7589` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.4668` n `32` status `ready` deltaP `31.7708` edge `1.7589` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2264` n `32` status `ready` deltaP `30.0347` edge `0.7353` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2264` n `32` status `ready` deltaP `30.0347` edge `0.7353` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.697` n `209` status `ready` deltaP `-0.9169` edge `1.4056` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.3853` n `152` status `ready` deltaP `18.9876` edge `0.7085` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.3202` n `72` status `ready` deltaP `18.8516` edge `0.4299` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3202` n `72` status `ready` deltaP `18.8516` edge `0.4299` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9714` n `152` status `ready` deltaP `25.4294` edge `0.3587` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.5542` n `152` status `ready` deltaP `23.273` edge `0.2842` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4398` n `72` status `ready` deltaP `24.3394` edge `0.1545` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4398` n `72` status `ready` deltaP `24.3394` edge `0.1545` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.233` n `152` status `ready` deltaP `6.2317` edge `0.5909` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `2.2174` n `209` status `ready` deltaP `15.0039` edge `0.2612` maxDD `-9.4488`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
