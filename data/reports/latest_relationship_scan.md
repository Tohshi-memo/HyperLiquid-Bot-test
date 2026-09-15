# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T09:07:27.603364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11176`

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

- `news_risk_high->unknown_4h` score `397.7482` n `78` status `ready` deltaP `-22.303` edge `33.3837` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7319` n `78` status `ready` deltaP `45.1656` edge `1.549` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.6207` n `78` status `ready` deltaP `18.2292` edge `1.6802` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.4232` n `78` status `ready` deltaP `34.8691` edge `1.2832` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.0406` n `78` status `ready` deltaP `48.4642` edge `1.1083` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6974` n `78` status `ready` deltaP `62.1127` edge `0.3283` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5559` n `78` status `ready` deltaP `38.6618` edge `0.334` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0004` n `52` status `ready` deltaP `38.1944` edge `0.2454` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0004` n `52` status `ready` deltaP `38.1944` edge `0.2454` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7034` n `137` status `ready` deltaP `30.8951` edge `0.2385` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.8052` n `52` status `ready` deltaP `43.9102` edge `0.0286` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.8052` n `52` status `ready` deltaP `43.9102` edge `0.0286` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.4082` n `137` status `ready` deltaP `40.7238` edge `0.0341` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9483` n `52` status `ready` deltaP `25.0703` edge `0.0302` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9483` n `52` status `ready` deltaP `25.0703` edge `0.0302` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8481` n `149` status `ready` deltaP `21.5726` edge `0.052` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8413` n `149` status `ready` deltaP `13.5163` edge `0.0177` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7027` n `78` status `ready` deltaP `17.2686` edge `0.0378` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2409` n `52` status `ready` deltaP `8.0608` edge `0.0077` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2409` n `52` status `ready` deltaP `8.0608` edge `0.0077` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
