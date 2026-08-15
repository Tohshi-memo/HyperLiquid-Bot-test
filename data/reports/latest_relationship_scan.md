# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T15:22:32.712809+00:00`
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

- `market_context_high->unknown_24h` score `137.6796` n `128` status `ready` deltaP `-23.4227` edge `11.9207` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7707` n `32` status `ready` deltaP `-36.7039` edge `4.6493` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7707` n `32` status `ready` deltaP `-36.7039` edge `4.6493` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9707` n `36` status `ready` deltaP `26.6609` edge `0.9411` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7449` n `36` status `ready` deltaP `40.3963` edge `0.3761` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.5177` n `128` status `ready` deltaP `32.3182` edge `0.2501` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.0938` n `32` status `ready` deltaP `34.662` edge `0.1934` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.0938` n `32` status `ready` deltaP `34.662` edge `0.1934` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2015` n `32` status `ready` deltaP `28.0275` edge `0.4674` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2015` n `32` status `ready` deltaP `28.0275` edge `0.4674` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6907` n `36` status `ready` deltaP `30.8492` edge `0.1019` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.888` n `32` status `ready` deltaP `20.6555` edge `0.1212` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.888` n `32` status `ready` deltaP `20.6555` edge `0.1212` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9401` n `128` status `ready` deltaP `19.093` edge `0.0815` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9388` n `36` status `ready` deltaP `22.3577` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.737` n `36` status `ready` deltaP `8.2835` edge `0.1214` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3557` n `32` status `ready` deltaP `14.5584` edge `0.0392` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3557` n `32` status `ready` deltaP `14.5584` edge `0.0392` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7848` n `32` status `ready` deltaP `15.2026` edge `0.1772` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7848` n `32` status `ready` deltaP `15.2026` edge `0.1772` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
