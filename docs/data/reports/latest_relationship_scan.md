# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T12:22:27.492319+00:00`
- Price records: `672`
- Market context records: `3685`
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

- `risk_on_high->crypto_major_24h` score `32.2418` n `32` status `ready` deltaP `35.9375` edge `2.4515` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.2418` n `32` status `ready` deltaP `35.9375` edge `2.4515` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.822` n `32` status `ready` deltaP `38.1944` edge `1.8972` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.822` n `32` status `ready` deltaP `38.1944` edge `1.8972` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.9755` n `32` status `ready` deltaP `35.0694` edge `1.7793` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.9755` n `32` status `ready` deltaP `35.0694` edge `1.7793` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.1777` n `32` status `ready` deltaP `38.0208` edge `0.928` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.1777` n `32` status `ready` deltaP `38.0208` edge `0.928` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.7941` n `32` status `ready` deltaP `19.0549` edge `0.8847` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.7941` n `32` status `ready` deltaP `19.0549` edge `0.8847` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `5.0181` n `32` status `ready` deltaP `23.6111` edge `0.2869` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `5.0181` n `32` status `ready` deltaP `23.6111` edge `0.2869` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.7816` n `157` status `ready` deltaP `23.3711` edge `0.3309` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `2.1498` n `32` status `ready` deltaP `9.0701` edge `0.3286` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.1498` n `32` status `ready` deltaP `9.0701` edge `0.3286` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.9379` n `32` status `ready` deltaP `-0.8384` edge `0.3515` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.9379` n `32` status `ready` deltaP `-0.8384` edge `0.3515` maxDD `-11.7537`
- `market_context_high->equity_24h` score `1.534` n `157` status `ready` deltaP `15.2645` edge `0.5925` maxDD `-35.3144`
- `risk_on_high->crypto_major_1h` score `1.2067` n `32` status `ready` deltaP `2.5262` edge `0.2448` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2067` n `32` status `ready` deltaP `2.5262` edge `0.2448` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
