# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T11:22:27.754689+00:00`
- Price records: `672`
- Market context records: `3681`
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

- `risk_on_high->crypto_major_24h` score `32.7497` n `32` status `ready` deltaP `36.6319` edge `2.4892` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.7497` n `32` status `ready` deltaP `36.6319` edge `2.4892` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.6623` n `32` status `ready` deltaP `38.8889` edge `1.9626` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.6623` n `32` status `ready` deltaP `38.8889` edge `1.9626` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `24.4954` n `32` status `ready` deltaP `35.7639` edge `1.818` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `24.4954` n `32` status `ready` deltaP `35.7639` edge `1.818` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.7048` n `32` status `ready` deltaP `38.7153` edge `0.9673` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.7048` n `32` status `ready` deltaP `38.7153` edge `0.9673` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.1417` n `32` status `ready` deltaP `19.6646` edge `0.9096` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.1417` n `32` status `ready` deltaP `19.6646` edge `0.9096` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `5.7144` n `32` status `ready` deltaP `24.3056` edge `0.3403` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `5.7144` n `32` status `ready` deltaP `24.3056` edge `0.3403` maxDD `-0.7574`
- `market_context_high->index_24h` score `4.3088` n `157` status `ready` deltaP `24.0656` edge `0.3702` maxDD `-11.3924`
- `market_context_high->equity_24h` score `2.3744` n `157` status `ready` deltaP `15.959` edge `0.6579` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.3639` n `32` status `ready` deltaP `9.5274` edge `0.353` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.3639` n `32` status `ready` deltaP `9.5274` edge `0.353` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.265` n `32` status `ready` deltaP `-0.2287` edge `0.3747` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.265` n `32` status `ready` deltaP `-0.2287` edge `0.3747` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.2449` n `32` status `ready` deltaP `2.8256` edge `0.2477` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2449` n `32` status `ready` deltaP `2.8256` edge `0.2477` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
