# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T12:52:27.418075+00:00`
- Price records: `672`
- Market context records: `3687`
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

- `risk_on_high->crypto_major_24h` score `31.9788` n `32` status `ready` deltaP `35.5903` edge `2.4319` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.9788` n `32` status `ready` deltaP `35.5903` edge `2.4319` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.421` n `32` status `ready` deltaP `37.8472` edge `1.8661` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.421` n `32` status `ready` deltaP `37.8472` edge `1.8661` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.7137` n `32` status `ready` deltaP `34.7222` edge `1.7598` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.7137` n `32` status `ready` deltaP `34.7222` edge `1.7598` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.9267` n `32` status `ready` deltaP `37.6736` edge `0.9094` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.9267` n `32` status `ready` deltaP `37.6736` edge `0.9094` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.6761` n `32` status `ready` deltaP `18.75` edge `0.8769` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.6761` n `32` status `ready` deltaP `18.75` edge `0.8769` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `4.6771` n `32` status `ready` deltaP `23.2639` edge `0.2608` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `4.6771` n `32` status `ready` deltaP `23.2639` edge `0.2608` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.5307` n `157` status `ready` deltaP `23.0239` edge `0.3123` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `2.0553` n `32` status `ready` deltaP `8.9177` edge `0.3175` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.0553` n `32` status `ready` deltaP `8.9177` edge `0.3175` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.8295` n `32` status `ready` deltaP `-1.1433` edge `0.3445` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.8295` n `32` status `ready` deltaP `-1.1433` edge `0.3445` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.2199` n `32` status `ready` deltaP `2.5262` edge `0.2465` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2199` n `32` status `ready` deltaP `2.5262` edge `0.2465` maxDD `-5.8885`
- `market_context_high->equity_24h` score `1.133` n `157` status `ready` deltaP `14.9173` edge `0.5614` maxDD `-35.3144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
