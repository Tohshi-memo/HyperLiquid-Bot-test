# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T09:07:35.242536+00:00`
- Price records: `672`
- Market context records: `3671`
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

- `risk_on_high->crypto_major_24h` score `33.9559` n `32` status `ready` deltaP `38.1944` edge `2.5793` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.9559` n `32` status `ready` deltaP `38.1944` edge `2.5793` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `28.3898` n `32` status `ready` deltaP `40.2778` edge `2.0973` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `28.3898` n `32` status `ready` deltaP `40.2778` edge `2.0973` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `25.7616` n `32` status `ready` deltaP `37.3264` edge `1.9131` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `25.7616` n `32` status `ready` deltaP `37.3264` edge `1.9131` maxDD `-0.8779`
- `risk_on_high->index_24h` score `15.8822` n `32` status `ready` deltaP `40.2778` edge `1.055` maxDD `0.0`
- `risk_on_and_context->index_24h` score `15.8822` n `32` status `ready` deltaP `40.2778` edge `1.055` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.5642` n `32` status `ready` deltaP `20.7317` edge `0.9377` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.5642` n `32` status `ready` deltaP `20.7317` edge `0.9377` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `7.2674` n `32` status `ready` deltaP `25.8681` edge `0.4593` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `7.2674` n `32` status `ready` deltaP `25.8681` edge `0.4593` maxDD `-0.7574`
- `market_context_high->index_24h` score `5.4862` n `157` status `ready` deltaP `25.6281` edge `0.4579` maxDD `-11.3924`
- `market_context_high->equity_24h` score `4.1019` n `157` status `ready` deltaP `17.3479` edge `0.7926` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.7092` n `32` status `ready` deltaP `0.8384` edge `0.4046` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7092` n `32` status `ready` deltaP `0.8384` edge `0.4046` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.705` n `32` status `ready` deltaP `10.747` edge `0.3886` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.705` n `32` status `ready` deltaP `10.747` edge `0.3886` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.2916` n `32` status `ready` deltaP `3.2747` edge `0.2507` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2916` n `32` status `ready` deltaP `3.2747` edge `0.2507` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
