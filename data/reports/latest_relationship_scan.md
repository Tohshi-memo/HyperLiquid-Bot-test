# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T11:22:33.381858+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11210`

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

- `news_risk_high->unknown_4h` score `396.805` n `78` status `ready` deltaP `-22.303` edge `33.3051` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `22.1013` n `78` status `ready` deltaP `46.0337` edge `1.574` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.9496` n `78` status `ready` deltaP `19.4444` edge `1.6995` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.919` n `78` status `ready` deltaP `36.4316` edge `1.3141` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1978` n `78` status `ready` deltaP `48.4642` edge `1.1214` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6509` n `78` status `ready` deltaP `61.5918` edge `0.3279` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5547` n `78` status `ready` deltaP `38.6618` edge `0.3339` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9268` n `52` status `ready` deltaP `37.5` edge `0.2439` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9268` n `52` status `ready` deltaP `37.5` edge `0.2439` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6298` n `137` status `ready` deltaP `30.2007` edge `0.237` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.6238` n `52` status `ready` deltaP `42.3477` edge `0.0239` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.6238` n `52` status `ready` deltaP `42.3477` edge `0.0239` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.2268` n `137` status `ready` deltaP `39.1613` edge `0.0294` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8514` n `52` status `ready` deltaP `24.3082` edge `0.0272` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8514` n `52` status `ready` deltaP `24.3082` edge `0.0272` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7511` n `149` status `ready` deltaP `20.8105` edge `0.049` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8342` n `149` status `ready` deltaP `13.3666` edge `0.0181` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7327` n `78` status `ready` deltaP `17.7259` edge `0.0386` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2198` n `52` status `ready` deltaP `7.7614` edge `0.007` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2198` n `52` status `ready` deltaP `7.7614` edge `0.007` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
