# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T13:22:29.704251+00:00`
- Price records: `672`
- Market context records: `3386`
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

- `risk_on_high->crypto_major_24h` score `55.5902` n `32` status `ready` deltaP `58.3333` edge `4.2479` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.5902` n `32` status `ready` deltaP `58.3333` edge `4.2479` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5949` n `32` status `ready` deltaP `54.6875` edge `4.1168` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5949` n `32` status `ready` deltaP `54.6875` edge `4.1168` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.5301` n `32` status `ready` deltaP `56.7708` edge `3.4157` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5301` n `32` status `ready` deltaP `56.7708` edge `3.4157` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1446` n `32` status `ready` deltaP `50.8681` edge `1.5896` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1446` n `32` status `ready` deltaP `50.8681` edge `1.5896` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.753` n `156` status `ready` deltaP `18.7099` edge `2.4865` maxDD `-56.8787`
- `market_context_high->equity_24h` score `16.966` n `156` status `ready` deltaP `30.4887` edge `2.0522` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `15.9596` n `156` status `ready` deltaP `23.6378` edge `2.2819` maxDD `-81.7614`
- `risk_on_high->crypto_major_4h` score `15.1798` n `32` status `ready` deltaP `28.2012` edge `1.1892` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1798` n `32` status `ready` deltaP `28.2012` edge `1.1892` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.9654` n `32` status `ready` deltaP `29.6875` edge `0.992` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.9654` n `32` status `ready` deltaP `29.6875` edge `0.992` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.7853` n `156` status `ready` deltaP `35.4835` edge `1.001` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `6.9994` n `32` status `ready` deltaP `8.4604` edge `0.7113` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.9994` n `32` status `ready` deltaP `8.4604` edge `0.7113` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5849` n `32` status `ready` deltaP `14.5579` edge `0.476` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5849` n `32` status `ready` deltaP `14.5579` edge `0.476` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
