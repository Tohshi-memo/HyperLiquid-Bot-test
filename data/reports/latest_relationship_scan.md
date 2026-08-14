# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T13:22:30.968165+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `100.7154` n `144` status `ready` deltaP `-32.9861` edge `8.9041` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9455` n `32` status `ready` deltaP `-44.4444` edge `4.5951` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9455` n `32` status `ready` deltaP `-44.4444` edge `4.5951` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5439` n `36` status `ready` deltaP `9.8958` edge `0.7673` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.149` n `36` status `ready` deltaP `37.9573` edge `0.3427` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.8299` n `32` status `ready` deltaP `32.6389` edge `0.1849` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8299` n `32` status `ready` deltaP `32.6389` edge `0.1849` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.963` n `144` status `ready` deltaP `22.2222` edge `0.1791` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.8946` n `32` status `ready` deltaP `20.1982` edge `0.1248` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8946` n `32` status `ready` deltaP `20.1982` edge `0.1248` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.0941` n `36` status `ready` deltaP `14.2361` edge `0.0796` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.9113` n `32` status `ready` deltaP `16.1458` edge `0.253` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.9113` n `32` status `ready` deltaP `16.1458` edge `0.253` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.6734` n `36` status `ready` deltaP `8.4332` edge `0.1151` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.6677` n `36` status `ready` deltaP `19.6138` edge `0.0214` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.2962` n `144` status `ready` deltaP `15.6843` edge `0.0673` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2623` n `32` status `ready` deltaP `13.3608` edge `0.0394` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2623` n `32` status `ready` deltaP `13.3608` edge `0.0394` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2334` n `32` status `ready` deltaP `14.5833` edge `0.024` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2334` n `32` status `ready` deltaP `14.5833` edge `0.024` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
