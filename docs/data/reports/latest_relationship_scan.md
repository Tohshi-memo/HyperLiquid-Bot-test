# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T20:22:28.221262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `164.085` n `118` status `ready` deltaP `-28.0513` edge `14.152` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.8899` n `32` status `ready` deltaP `-35.8373` edge `4.6588` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.8899` n `32` status `ready` deltaP `-35.8373` edge `4.6588` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9707` n `36` status `ready` deltaP `26.6609` edge `0.9411` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7711` n `36` status `ready` deltaP `40.2439` edge `0.3793` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2469` n `118` status `ready` deltaP `35.9134` edge `0.2869` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.4027` n `32` status `ready` deltaP `37.6083` edge `0.1995` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4027` n `32` status `ready` deltaP `37.6083` edge `0.1995` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0898` n `32` status `ready` deltaP `27.6809` edge `0.4554` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0898` n `32` status `ready` deltaP `27.6809` edge `0.4554` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7058` n `36` status `ready` deltaP `31.0225` edge `0.102` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9791` n `32` status `ready` deltaP `21.5701` edge `0.1227` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9791` n `32` status `ready` deltaP `21.5701` edge `0.1227` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.987` n `118` status `ready` deltaP `18.8688` edge `0.0869` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.94` n `36` status `ready` deltaP `22.3577` edge `0.0258` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.749` n `36` status `ready` deltaP `8.2835` edge `0.1224` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3593` n `32` status `ready` deltaP `14.5584` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3593` n `32` status `ready` deltaP `14.5584` edge `0.0395` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7848` n `32` status `ready` deltaP `15.2026` edge `0.1772` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7848` n `32` status `ready` deltaP `15.2026` edge `0.1772` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
