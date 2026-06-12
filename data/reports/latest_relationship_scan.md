# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T17:37:41.201459+00:00`
- Price records: `672`
- Market context records: `3708`
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

- `risk_on_high->crypto_major_24h` score `29.9521` n `32` status `ready` deltaP `32.2917` edge `2.285` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.9521` n `32` status `ready` deltaP `32.2917` edge `2.285` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.8303` n `32` status `ready` deltaP `34.5486` edge `1.6722` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.8303` n `32` status `ready` deltaP `34.5486` edge `1.6722` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.9702` n `32` status `ready` deltaP `31.4236` edge `1.6365` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.9702` n `32` status `ready` deltaP `31.4236` edge `1.6365` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.1532` n `32` status `ready` deltaP `34.375` edge `0.7836` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.1532` n `32` status `ready` deltaP `34.375` edge `0.7836` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8275` n `32` status `ready` deltaP `16.7683` edge `0.8194` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8275` n `32` status `ready` deltaP `16.7683` edge `0.8194` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.6762` n `160` status `ready` deltaP `23.75` edge `0.3453` maxDD `-7.1159`
- `market_context_high->equity_24h` score `4.5265` n `160` status `ready` deltaP `15.7986` edge `0.5928` maxDD `-17.6733`
- `risk_on_high->metal_24h` score `2.5724` n `32` status `ready` deltaP `19.9653` edge `0.1074` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.5724` n `32` status `ready` deltaP `19.9653` edge `0.1074` maxDD `-0.7574`
- `market_context_high->metal_24h` score `1.6422` n `160` status `ready` deltaP `18.7153` edge `0.254` maxDD `-11.3536`
- `risk_on_high->equity_4h` score `1.5767` n `32` status `ready` deltaP `8.3079` edge `0.2602` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5767` n `32` status `ready` deltaP `8.3079` edge `0.2602` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.4001` n `32` status `ready` deltaP `-1.9055` edge `0.3138` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.4001` n `32` status `ready` deltaP `-1.9055` edge `0.3138` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.0141` n `32` status `ready` deltaP `1.7777` edge `0.2251` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
