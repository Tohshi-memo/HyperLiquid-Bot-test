# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T12:22:38.812483+00:00`
- Price records: `672`
- Market context records: `3382`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `55.7774` n `32` status `ready` deltaP `58.3333` edge `4.2635` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.7774` n `32` status `ready` deltaP `58.3333` edge `4.2635` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5781` n `32` status `ready` deltaP `54.6875` edge `4.1154` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5781` n `32` status `ready` deltaP `54.6875` edge `4.1154` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.5757` n `32` status `ready` deltaP `56.7708` edge `3.4195` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5757` n `32` status `ready` deltaP `56.7708` edge `3.4195` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1254` n `32` status `ready` deltaP `50.8681` edge `1.588` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1254` n `32` status `ready` deltaP `50.8681` edge `1.588` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.1283` n `154` status `ready` deltaP `19.5008` edge `2.5125` maxDD `-56.8787`
- `risk_on_high->crypto_major_4h` score `15.283` n `32` status `ready` deltaP `28.2012` edge `1.1978` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.283` n `32` status `ready` deltaP `28.2012` edge `1.1978` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `15.1984` n `154` status `ready` deltaP `24.4453` edge `2.2947` maxDD `-88.2905`
- `risk_on_high->metal_24h` score `14.1913` n `32` status `ready` deltaP `30.3819` edge `1.0062` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.1913` n `32` status `ready` deltaP `30.3819` edge `1.0062` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.7765` n `154` status `ready` deltaP `35.2837` edge `1.0016` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.9876` n `154` status `ready` deltaP `30.1474` edge `2.0493` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.1774` n `32` status `ready` deltaP `8.7652` edge `0.7241` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1774` n `32` status `ready` deltaP `8.7652` edge `0.7241` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5629` n `32` status `ready` deltaP `14.4055` edge `0.4742` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5629` n `32` status `ready` deltaP `14.4055` edge `0.4742` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
