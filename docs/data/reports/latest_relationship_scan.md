# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T12:07:26.791624+00:00`
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

- `market_context_high->unknown_24h` score `137.4577` n `128` status `ready` deltaP `-24.9824` edge `11.9126` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6264` n `32` status `ready` deltaP `-38.2636` edge `4.6412` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6264` n `32` status `ready` deltaP `-38.2636` edge `4.6412` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.6027` n `36` status `ready` deltaP `24.5811` edge `0.9243` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6979` n `36` status `ready` deltaP `40.2439` edge `0.3732` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.3858` n `128` status `ready` deltaP `31.1051` edge `0.2472` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9619` n `32` status `ready` deltaP `33.4489` edge `0.1905` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9619` n `32` status `ready` deltaP `33.4489` edge `0.1905` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2495` n `32` status `ready` deltaP `28.2008` edge `0.4724` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2495` n `32` status `ready` deltaP `28.2008` edge `0.4724` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.4932` n `36` status `ready` deltaP `28.7695` edge `0.0993` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9975` n `32` status `ready` deltaP `21.875` edge `0.1222` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9975` n `32` status `ready` deltaP `21.875` edge `0.1222` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0497` n `128` status `ready` deltaP `20.3125` edge `0.0825` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9364` n `36` status `ready` deltaP `22.3577` edge `0.0255` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7514` n `36` status `ready` deltaP `8.5829` edge `0.1206` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.297` n `32` status `ready` deltaP `13.8099` edge `0.0393` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.297` n `32` status `ready` deltaP `13.8099` edge `0.0393` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6605` n `128` status `ready` deltaP `9.1224` edge `0.0239` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5534` n `32` status `ready` deltaP `6.7835` edge `0.015` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
