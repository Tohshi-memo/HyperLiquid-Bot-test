# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T19:07:31.237383+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->unknown_4h` score `29.8634` n `133` status `ready` deltaP `12.3521` edge `2.4681` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `29.8634` n `133` status `ready` deltaP `12.3521` edge `2.4681` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `23.0984` n `167` status `ready` deltaP `13.9504` edge `1.9014` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.3085` n `133` status `ready` deltaP `1.0422` edge `1.4098` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.3085` n `133` status `ready` deltaP `1.0422` edge `1.4098` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.8287` n `167` status `ready` deltaP `1.497` edge `1.0388` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.9124` n `127` status `ready` deltaP `18.56` edge `0.4702` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `1.5089` n `67` status `ready` deltaP `18.1359` edge `0.366` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.4295` n `107` status `ready` deltaP `13.8062` edge `0.4416` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.4295` n `107` status `ready` deltaP `13.8062` edge `0.4416` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `0.8792` n `67` status `ready` deltaP `14.6326` edge `0.4535` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `0.7278` n `67` status `ready` deltaP `6.2319` edge `0.2985` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.4316` n `67` status `ready` deltaP `7.7767` edge `0.0394` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `news_risk_high->fx_4h` score `0.0617` n `67` status `ready` deltaP `9.9563` edge `0.0044` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.0765` n `67` status `ready` deltaP `4.3257` edge `-0.0033` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1147` n `133` status `ready` deltaP `4.7409` edge `-0.0018` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1147` n `133` status `ready` deltaP `4.7409` edge `-0.0018` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1286` n `67` status `ready` deltaP `4.9066` edge `0.0012` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
