# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T08:07:27.285689+00:00`
- Price records: `672`
- Market context records: `3363`
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

- `risk_on_high->crypto_major_24h` score `57.1273` n `32` status `ready` deltaP `60.4167` edge `4.3621` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `57.1273` n `32` status `ready` deltaP `60.4167` edge `4.3621` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.7573` n `32` status `ready` deltaP `55.3819` edge `4.1257` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.7573` n `32` status `ready` deltaP `55.3819` edge `4.1257` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.0989` n `32` status `ready` deltaP `56.7708` edge `3.4631` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.0989` n `32` status `ready` deltaP `56.7708` edge `3.4631` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1914` n `32` status `ready` deltaP `50.8681` edge `1.5935` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1914` n `32` status `ready` deltaP `50.8681` edge `1.5935` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.427` n `32` status `ready` deltaP `28.2012` edge `1.2098` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.427` n `32` status `ready` deltaP `28.2012` edge `1.2098` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.2411` n `32` status `ready` deltaP `33.3333` edge `1.074` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.2411` n `32` status `ready` deltaP `33.3333` edge `1.074` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `12.9581` n `161` status `ready` deltaP `17.5131` edge `2.4571` maxDD `-66.0047`
- `market_context_high->index_24h` score `12.0755` n `161` status `ready` deltaP `35.9613` edge `1.022` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.7085` n `161` status `ready` deltaP `31.305` edge `2.0058` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3392` n `32` status `ready` deltaP `8.6128` edge `0.7386` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3392` n `32` status `ready` deltaP `8.6128` edge `0.7386` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.562` n `32` status `ready` deltaP `14.253` edge `0.4751` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.562` n `32` status `ready` deltaP `14.253` edge `0.4751` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3704` n `161` status `ready` deltaP `20.6846` edge `2.0476` maxDD `-138.5276`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
