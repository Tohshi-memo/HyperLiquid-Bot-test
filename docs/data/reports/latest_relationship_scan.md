# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T13:52:26.967112+00:00`
- Price records: `672`
- Market context records: `3388`
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

- `risk_on_high->crypto_major_24h` score `55.505` n `32` status `ready` deltaP `58.3333` edge `4.2408` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.505` n `32` status `ready` deltaP `58.3333` edge `4.2408` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.6117` n `32` status `ready` deltaP `54.6875` edge `4.1182` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.6117` n `32` status `ready` deltaP `54.6875` edge `4.1182` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.4195` n `32` status `ready` deltaP `56.4236` edge `3.4088` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.4195` n `32` status `ready` deltaP `56.4236` edge `3.4088` maxDD `0.0`
- `risk_on_high->index_24h` score `23.12` n `32` status `ready` deltaP `50.6944` edge `1.5887` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.12` n `32` status `ready` deltaP `50.6944` edge `1.5887` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.7098` n `156` status `ready` deltaP `18.7099` edge `2.4829` maxDD `-56.8787`
- `market_context_high->equity_24h` score `17.5356` n `156` status `ready` deltaP `31.4236` edge `2.0706` maxDD `-52.5035`
- `market_context_high->crypto_major_24h` score `17.2329` n `156` status `ready` deltaP `23.6378` edge `2.3009` maxDD `-74.7928`
- `risk_on_high->crypto_major_4h` score `15.1282` n `32` status `ready` deltaP `28.2012` edge `1.1849` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1282` n `32` status `ready` deltaP `28.2012` edge `1.1849` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.85` n `32` status `ready` deltaP `29.3403` edge `0.9847` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.85` n `32` status `ready` deltaP `29.3403` edge `0.9847` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.8539` n `156` status `ready` deltaP `35.9508` edge `1.0036` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `6.891` n `32` status `ready` deltaP `8.1555` edge `0.7043` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.891` n `32` status `ready` deltaP `8.1555` edge `0.7043` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6061` n `32` status `ready` deltaP `14.7104` edge `0.4777` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6061` n `32` status `ready` deltaP `14.7104` edge `0.4777` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
