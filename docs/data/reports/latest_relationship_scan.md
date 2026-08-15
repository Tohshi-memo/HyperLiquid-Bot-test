# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T09:37:37.660682+00:00`
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

- `market_context_high->unknown_24h` score `137.2434` n `128` status `ready` deltaP `-26.7156` edge `11.9063` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.4872` n `32` status `ready` deltaP `-39.9968` edge `4.6349` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.4872` n `32` status `ready` deltaP `-39.9968` edge `4.6349` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.2457` n `36` status `ready` deltaP `22.848` edge `0.9061` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6363` n `36` status `ready` deltaP `39.8782` edge `0.3705` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.2438` n `128` status `ready` deltaP `30.0652` edge `0.2423` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.8199` n `32` status `ready` deltaP `32.409` edge `0.1856` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8199` n `32` status `ready` deltaP `32.409` edge `0.1856` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2206` n `32` status `ready` deltaP `28.2008` edge `0.4687` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2206` n `32` status `ready` deltaP `28.2008` edge `0.4687` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.3125` n `36` status `ready` deltaP `27.0364` edge `0.0958` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9522` n `32` status `ready` deltaP `21.504` edge `0.1209` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9522` n `32` status `ready` deltaP `21.504` edge `0.1209` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0044` n `128` status `ready` deltaP `19.9415` edge `0.0812` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8526` n `36` status `ready` deltaP `21.3851` edge `0.025` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7454` n `36` status `ready` deltaP `8.5829` edge `0.1201` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2851` n `32` status `ready` deltaP `13.6602` edge `0.0393` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2851` n `32` status `ready` deltaP `13.6602` edge `0.0393` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6485` n `128` status `ready` deltaP `8.9727` edge `0.0239` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5496` n `32` status `ready` deltaP `6.7209` edge `0.0151` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
