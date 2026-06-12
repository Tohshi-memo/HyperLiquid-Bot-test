# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T02:37:30.923690+00:00`
- Price records: `672`
- Market context records: `3645`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `37.5822` n `32` status `ready` deltaP `42.7083` edge `2.8514` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `37.5822` n `32` status `ready` deltaP `42.7083` edge `2.8514` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `34.0765` n `32` status `ready` deltaP `44.7917` edge `2.5411` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `34.0765` n `32` status `ready` deltaP `44.7917` edge `2.5411` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `29.8163` n `32` status `ready` deltaP `41.8403` edge `2.2209` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `29.8163` n `32` status `ready` deltaP `41.8403` edge `2.2209` maxDD `-0.8779`
- `risk_on_high->index_24h` score `19.3993` n `32` status `ready` deltaP `44.7917` edge `1.318` maxDD `0.0`
- `risk_on_and_context->index_24h` score `19.3993` n `32` status `ready` deltaP `44.7917` edge `1.318` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.7844` n `32` status `ready` deltaP `21.189` edge `0.953` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.7844` n `32` status `ready` deltaP `21.189` edge `0.953` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `11.4157` n `32` status `ready` deltaP `30.3819` edge `0.7749` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `11.4157` n `32` status `ready` deltaP `30.3819` edge `0.7749` maxDD `-0.7574`
- `market_context_high->equity_24h` score `9.7886` n `157` status `ready` deltaP `21.8618` edge `1.2364` maxDD `-35.3144`
- `market_context_high->index_24h` score `9.0033` n `157` status `ready` deltaP `30.142` edge `0.7209` maxDD `-11.3924`
- `market_context_high->metal_24h` score `3.6393` n `157` status `ready` deltaP `24.6892` edge `0.6972` maxDD `-21.6171`
- `market_context_high->crypto_major_24h` score `3.5772` n `157` status `ready` deltaP `8.8906` edge `0.9455` maxDD `-49.5335`
- `risk_on_high->crypto_alt_4h` score `3.2358` n `32` status `ready` deltaP `1.6006` edge `0.4434` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.2358` n `32` status `ready` deltaP `1.6006` edge `0.4434` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.5414` n `32` status `ready` deltaP `9.9848` edge `0.3727` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5414` n `32` status `ready` deltaP `9.9848` edge `0.3727` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
