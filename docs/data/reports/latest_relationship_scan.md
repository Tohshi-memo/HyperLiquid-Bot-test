# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T14:22:29.487609+00:00`
- Price records: `672`
- Market context records: `3694`
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

- `risk_on_high->crypto_major_24h` score `31.3074` n `32` status `ready` deltaP `34.5486` edge `2.3829` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.3074` n `32` status `ready` deltaP `34.5486` edge `2.3829` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.452` n `32` status `ready` deltaP `36.8056` edge `1.7923` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.452` n `32` status `ready` deltaP `36.8056` edge `1.7923` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.0952` n `32` status `ready` deltaP `33.6806` edge `1.7152` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.0952` n `32` status `ready` deltaP `33.6806` edge `1.7152` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.2962` n `32` status `ready` deltaP `36.6319` edge `0.8638` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.2962` n `32` status `ready` deltaP `36.6319` edge `0.8638` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.4645` n `32` status `ready` deltaP `18.4451` edge `0.8613` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.4645` n `32` status `ready` deltaP `18.4451` edge `0.8613` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `3.8906` n `32` status `ready` deltaP `22.2222` edge `0.2022` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `3.8906` n `32` status `ready` deltaP `22.2222` edge `0.2022` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.5574` n `156` status `ready` deltaP `22.5293` edge `0.2844` maxDD `-9.0519`
- `risk_on_high->equity_4h` score `1.8954` n `32` status `ready` deltaP `8.9177` edge `0.297` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.8954` n `32` status `ready` deltaP `8.9177` edge `0.297` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.7513` n `32` status `ready` deltaP `-1.2957` edge `0.339` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.7513` n `32` status `ready` deltaP `-1.2957` edge `0.339` maxDD `-11.7537`
- `market_context_high->equity_24h` score `1.2122` n `156` status `ready` deltaP `14.3697` edge `0.5189` maxDD `-31.4279`
- `risk_on_high->crypto_major_1h` score `1.1505` n `32` status `ready` deltaP `2.2268` edge `0.2396` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.1505` n `32` status `ready` deltaP `2.2268` edge `0.2396` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
