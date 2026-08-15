# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T11:52:34.065361+00:00`
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

- `market_context_high->unknown_24h` score `137.4366` n `128` status `ready` deltaP `-25.1558` edge `11.912` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6127` n `32` status `ready` deltaP `-38.437` edge `4.6406` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6127` n `32` status `ready` deltaP `-38.437` edge `4.6406` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.5685` n `36` status `ready` deltaP `24.4078` edge `0.9226` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6931` n `36` status `ready` deltaP `40.2439` edge `0.3728` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.3672` n `128` status `ready` deltaP `30.9318` edge `0.2468` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9432` n `32` status `ready` deltaP `33.2756` edge `0.1901` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9432` n `32` status `ready` deltaP `33.2756` edge `0.1901` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2471` n `32` status `ready` deltaP `28.2008` edge `0.4721` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2471` n `32` status `ready` deltaP `28.2008` edge `0.4721` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.4757` n `36` status `ready` deltaP `28.5962` edge `0.099` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0121` n `32` status `ready` deltaP `22.0274` edge `0.1224` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0121` n `32` status `ready` deltaP `22.0274` edge `0.1224` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0643` n `128` status `ready` deltaP `20.4649` edge `0.0827` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9364` n `36` status `ready` deltaP `22.3577` edge `0.0255` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7646` n `36` status `ready` deltaP `8.7326` edge `0.1207` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2982` n `32` status `ready` deltaP `13.8099` edge `0.0394` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2982` n `32` status `ready` deltaP `13.8099` edge `0.0394` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6617` n `128` status `ready` deltaP `9.1224` edge `0.024` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5534` n `32` status `ready` deltaP `6.7835` edge `0.015` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
