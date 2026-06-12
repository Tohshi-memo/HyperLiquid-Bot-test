# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T18:52:31.186131+00:00`
- Price records: `672`
- Market context records: `3713`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13025`

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

- `risk_on_high->crypto_major_24h` score `29.6498` n `32` status `ready` deltaP `31.4236` edge `2.2656` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.6498` n `32` status `ready` deltaP `31.4236` edge `2.2656` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.48` n `32` status `ready` deltaP `33.6806` edge `1.6488` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.48` n `32` status `ready` deltaP `33.6806` edge `1.6488` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.7413` n `32` status `ready` deltaP `30.9028` edge `1.6209` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.7413` n `32` status `ready` deltaP `30.9028` edge `1.6209` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.8762` n `32` status `ready` deltaP `33.5069` edge `0.7663` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.8762` n `32` status `ready` deltaP `33.5069` edge `0.7663` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9165` n `32` status `ready` deltaP `16.9207` edge `0.8258` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9165` n `32` status `ready` deltaP `16.9207` edge `0.8258` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.687` n `162` status `ready` deltaP `23.6304` edge `0.347` maxDD `-7.1159`
- `market_context_high->equity_24h` score `4.5924` n `162` status `ready` deltaP `15.7794` edge `0.5824` maxDD `-16.7253`
- `risk_on_high->metal_24h` score `2.2474` n `32` status `ready` deltaP `19.0972` edge `0.0861` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.2474` n `32` status `ready` deltaP `19.0972` edge `0.0861` maxDD `-0.7574`
- `market_context_high->metal_24h` score `1.9222` n `162` status `ready` deltaP `18.8657` edge `0.2638` maxDD `-10.6843`
- `risk_on_high->crypto_alt_4h` score `1.5639` n `32` status `ready` deltaP `-1.4482` edge `0.3244` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.5639` n `32` status `ready` deltaP `-1.4482` edge `0.3244` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.5422` n `32` status `ready` deltaP `8.1555` edge `0.2568` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5422` n `32` status `ready` deltaP `8.1555` edge `0.2568` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `0.9213` n `32` status `ready` deltaP `1.628` edge `0.2142` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
