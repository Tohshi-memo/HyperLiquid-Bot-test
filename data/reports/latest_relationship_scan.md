# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T19:37:38.418445+00:00`
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

- `risk_on_high->unknown_4h` score `29.221` n `133` status `ready` deltaP `12.0473` edge `2.4166` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `29.221` n `133` status `ready` deltaP `12.0473` edge `2.4166` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `22.456` n `167` status `ready` deltaP `13.6456` edge `1.8499` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.2533` n `133` status `ready` deltaP `1.0422` edge `1.4052` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.2533` n `133` status `ready` deltaP `1.0422` edge `1.4052` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.7735` n `167` status `ready` deltaP `1.497` edge `1.0342` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.7298` n `127` status `ready` deltaP `18.2127` edge `0.4573` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `1.2616` n `67` status `ready` deltaP `17.7886` edge `0.3366` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.2469` n `107` status `ready` deltaP `13.4589` edge `0.4287` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.2469` n `107` status `ready` deltaP `13.4589` edge `0.4287` maxDD `-19.828`
- `news_risk_high->equity_24h` score `0.6091` n `67` status `ready` deltaP `5.8846` edge `0.2856` maxDD `-15.4056`
- `news_risk_high->crypto_major_24h` score `0.5952` n `67` status `ready` deltaP `14.2854` edge `0.4194` maxDD `-30.7329`
- `news_risk_high->commodity_4h` score `0.4316` n `67` status `ready` deltaP `7.7767` edge `0.0394` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0867` n `133` status `ready` deltaP `12.1134` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0867` n `133` status `ready` deltaP `12.1134` edge `0.0016` maxDD `-1.699`
- `news_risk_high->fx_4h` score `0.0727` n `67` status `ready` deltaP `10.1088` edge `0.0043` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.0586` n `67` status `ready` deltaP `4.6251` edge `-0.003` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0968` n `133` status `ready` deltaP `5.0403` edge `-0.0015` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0968` n `133` status `ready` deltaP `5.0403` edge `-0.0015` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.143` n `67` status `ready` deltaP `4.7569` edge `0.001` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
