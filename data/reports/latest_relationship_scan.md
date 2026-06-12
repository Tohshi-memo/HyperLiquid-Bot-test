# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T14:37:35.928895+00:00`
- Price records: `672`
- Market context records: `3695`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `31.1976` n `32` status `ready` deltaP `34.375` edge `2.3749` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.1976` n `32` status `ready` deltaP `34.375` edge `2.3749` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.3062` n `32` status `ready` deltaP `36.6319` edge `1.7813` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.3062` n `32` status `ready` deltaP `36.6319` edge `1.7813` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.0009` n `32` status `ready` deltaP `33.5069` edge `1.7085` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.0009` n `32` status `ready` deltaP `33.5069` edge `1.7085` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.2031` n `32` status `ready` deltaP `36.4583` edge `0.8572` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.2031` n `32` status `ready` deltaP `36.4583` edge `0.8572` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.3887` n `32` status `ready` deltaP `18.2927` edge `0.856` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.3887` n `32` status `ready` deltaP `18.2927` edge `0.856` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `3.7903` n `32` status `ready` deltaP `22.0486` edge `0.195` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `3.7903` n `32` status `ready` deltaP `22.0486` edge `0.195` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.4643` n `156` status `ready` deltaP `22.3557` edge `0.2778` maxDD `-9.0519`
- `risk_on_high->equity_4h` score `1.8619` n `32` status `ready` deltaP `8.9177` edge `0.2927` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.8619` n `32` status `ready` deltaP `8.9177` edge `0.2927` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.6959` n `32` status `ready` deltaP `-1.4482` edge `0.3354` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.6959` n `32` status `ready` deltaP `-1.4482` edge `0.3354` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.1162` n `32` status `ready` deltaP `2.0771` edge `0.2362` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.1162` n `32` status `ready` deltaP `2.0771` edge `0.2362` maxDD `-5.8885`
- `market_context_high->equity_24h` score `1.0663` n `156` status `ready` deltaP `14.196` edge `0.5079` maxDD `-31.4279`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
