# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T12:07:29.618949+00:00`
- Price records: `672`
- Market context records: `3890`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13665`

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

- `risk_on_high->unknown_4h` score `47.3922` n `72` status `ready` deltaP `5.8943` edge `6.2508` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.3922` n `72` status `ready` deltaP `5.8943` edge `6.2508` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.5466` n `32` status `ready` deltaP `34.0278` edge `2.6563` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.5466` n `32` status `ready` deltaP `34.0278` edge `2.6563` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9627` n `32` status `ready` deltaP `42.0139` edge `1.9668` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9627` n `32` status `ready` deltaP `42.0139` edge `1.9668` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.4289` n `32` status `ready` deltaP `31.5972` edge `1.7569` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.4289` n `32` status `ready` deltaP `31.5972` edge `1.7569` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2144` n `32` status `ready` deltaP `30.0347` edge `0.7343` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2144` n `32` status `ready` deltaP `30.0347` edge `0.7343` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.8317` n `208` status `ready` deltaP `-0.9967` edge `1.4234` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.3671` n `151` status `ready` deltaP `18.8351` edge `0.708` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.3408` n `72` status `ready` deltaP `19.004` edge `0.4306` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3408` n `72` status `ready` deltaP `19.004` edge `0.4306` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9833` n `151` status `ready` deltaP `25.3989` edge `0.3599` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.5578` n `151` status `ready` deltaP `23.1685` edge `0.2852` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4386` n `72` status `ready` deltaP `24.3394` edge `0.1544` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4386` n `72` status `ready` deltaP `24.3394` edge `0.1544` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.2385` n `208` status `ready` deltaP `14.9976` edge `0.263` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.2274` n `151` status `ready` deltaP `6.027` edge `0.5918` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
