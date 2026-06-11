# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T20:52:42.385225+00:00`
- Price records: `672`
- Market context records: `3620`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `42.3189` n `32` status `ready` deltaP `46.7014` edge `3.2195` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `42.3189` n `32` status `ready` deltaP `46.7014` edge `3.2195` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `39.3988` n `32` status `ready` deltaP `48.7847` edge `2.958` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `39.3988` n `32` status `ready` deltaP `48.7847` edge `2.958` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `34.9982` n `32` status `ready` deltaP `45.8333` edge `2.6261` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `34.9982` n `32` status `ready` deltaP `45.8333` edge `2.6261` maxDD `-0.8779`
- `risk_on_high->index_24h` score `22.8148` n `32` status `ready` deltaP `48.7847` edge `1.576` maxDD `0.0`
- `risk_on_and_context->index_24h` score `22.8148` n `32` status `ready` deltaP `48.7847` edge `1.576` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.5248` n `32` status `ready` deltaP `34.375` edge `1.0907` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.5248` n `32` status `ready` deltaP `34.375` edge `1.0907` maxDD `-0.7574`
- `market_context_high->equity_24h` score `13.6688` n `158` status `ready` deltaP `25.367` edge `1.6112` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.5811` n `32` status `ready` deltaP `23.0183` edge `1.0072` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.5811` n `32` status `ready` deltaP `23.0183` edge `1.0072` maxDD `-5.9781`
- `market_context_high->index_24h` score `11.4649` n `158` status `ready` deltaP `33.5948` edge `0.9531` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `6.9963` n `158` status `ready` deltaP `12.4846` edge `1.2729` maxDD `-54.8486`
- `market_context_high->metal_24h` score `5.6155` n `158` status `ready` deltaP `28.2832` edge `0.9854` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.1959` n `32` status `ready` deltaP `3.5823` edge `0.5102` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.1959` n `32` status `ready` deltaP `3.5823` edge `0.5102` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.1062` n `32` status `ready` deltaP `12.8811` edge `0.4258` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.1062` n `32` status `ready` deltaP `12.8811` edge `0.4258` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
