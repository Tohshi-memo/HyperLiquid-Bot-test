# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T04:52:29.631135+00:00`
- Price records: `672`
- Market context records: `3654`
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

- `risk_on_high->crypto_major_24h` score `35.9224` n `32` status `ready` deltaP `41.1458` edge `2.7235` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.9224` n `32` status `ready` deltaP `41.1458` edge `2.7235` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `31.9271` n `32` status `ready` deltaP `43.2292` edge `2.3724` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `31.9271` n `32` status `ready` deltaP `43.2292` edge `2.3724` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `28.0257` n `32` status `ready` deltaP `40.2778` edge `2.0821` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `28.0257` n `32` status `ready` deltaP `40.2778` edge `2.0821` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.1247` n `32` status `ready` deltaP `43.2292` edge `1.2222` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.1247` n `32` status `ready` deltaP `43.2292` edge `1.2222` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.3392` n `32` status `ready` deltaP `20.2744` edge `0.922` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.3392` n `32` status `ready` deltaP `20.2744` edge `0.922` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `9.8831` n `32` status `ready` deltaP `28.8194` edge `0.6576` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `9.8831` n `32` status `ready` deltaP `28.8194` edge `0.6576` maxDD `-0.7574`
- `market_context_high->index_24h` score `7.7287` n `157` status `ready` deltaP `28.5795` edge `0.6251` maxDD `-11.3924`
- `market_context_high->equity_24h` score `7.6392` n `157` status `ready` deltaP `20.2993` edge `1.0677` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.6766` n `32` status `ready` deltaP `0.686` edge `0.4029` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.6766` n `32` status `ready` deltaP `0.686` edge `0.4029` maxDD `-11.7537`
- `market_context_high->metal_24h` score `2.6431` n `157` status `ready` deltaP `23.1267` edge `0.5799` maxDD `-21.6171`
- `risk_on_high->equity_4h` score `2.477` n `32` status `ready` deltaP `9.5274` edge `0.3675` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.477` n `32` status `ready` deltaP `9.5274` edge `0.3675` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.9174` n `157` status `ready` deltaP `7.3281` edge `0.8176` maxDD `-49.5335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
