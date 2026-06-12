# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T04:37:27.977052+00:00`
- Price records: `672`
- Market context records: `3653`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13201`

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

- `risk_on_high->crypto_major_24h` score `36.1379` n `32` status `ready` deltaP `41.3194` edge `2.7403` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `36.1379` n `32` status `ready` deltaP `41.3194` edge `2.7403` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `32.1666` n `32` status `ready` deltaP `43.4028` edge `2.3912` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `32.1666` n `32` status `ready` deltaP `43.4028` edge `2.3912` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `28.2592` n `32` status `ready` deltaP `40.4514` edge `2.1004` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `28.2592` n `32` status `ready` deltaP `40.4514` edge `2.1004` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.2682` n `32` status `ready` deltaP `43.4028` edge `1.233` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.2682` n `32` status `ready` deltaP `43.4028` edge `1.233` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.3874` n `32` status `ready` deltaP `20.4268` edge `0.925` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.3874` n `32` status `ready` deltaP `20.4268` edge `0.925` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `10.0482` n `32` status `ready` deltaP `28.9931` edge `0.6702` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `10.0482` n `32` status `ready` deltaP `28.9931` edge `0.6702` maxDD `-0.7574`
- `market_context_high->equity_24h` score `7.8787` n `157` status `ready` deltaP `20.4729` edge `1.0865` maxDD `-35.3144`
- `market_context_high->index_24h` score `7.8722` n `157` status `ready` deltaP `28.7531` edge `0.6359` maxDD `-11.3924`
- `market_context_high->metal_24h` score `2.7505` n `157` status `ready` deltaP `23.3004` edge `0.5925` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `2.7452` n `32` status `ready` deltaP `0.8384` edge `0.4076` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7452` n `32` status `ready` deltaP `0.8384` edge `0.4076` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.4652` n `32` status `ready` deltaP `9.375` edge `0.367` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4652` n `32` status `ready` deltaP `9.375` edge `0.367` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.1329` n `157` status `ready` deltaP `7.5017` edge `0.8344` maxDD `-49.5335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
