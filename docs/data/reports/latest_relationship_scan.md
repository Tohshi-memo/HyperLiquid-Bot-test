# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T06:22:25.115789+00:00`
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

- `market_context_high->unknown_24h` score `136.7222` n `128` status `ready` deltaP `-28.3855` edge `11.874` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1484` n `32` status `ready` deltaP `-41.6667` edge `4.6026` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1484` n `32` status `ready` deltaP `-41.6667` edge `4.6026` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.8246` n `36` status `ready` deltaP `20.6597` edge `0.8856` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4578` n `36` status `ready` deltaP `38.2622` edge `0.3664` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9466` n `128` status `ready` deltaP `27.8645` edge `0.2322` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5227` n `32` status `ready` deltaP `30.2083` edge `0.1755` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5227` n `32` status `ready` deltaP `30.2083` edge `0.1755` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0873` n `32` status `ready` deltaP `27.2569` edge `0.4579` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0873` n `32` status `ready` deltaP `27.2569` edge `0.4579` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.0937` n `36` status `ready` deltaP `24.8264` edge `0.0923` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7462` n `32` status `ready` deltaP `19.5884` edge `0.1165` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7462` n `32` status `ready` deltaP `19.5884` edge `0.1165` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.7984` n `128` status `ready` deltaP `18.0259` edge `0.0768` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7281` n `36` status `ready` deltaP `19.9187` edge `0.0244` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6663` n `36` status `ready` deltaP `7.6847` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1844` n `32` status `ready` deltaP `12.6123` edge `0.0379` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1844` n `32` status `ready` deltaP `12.6123` edge `0.0379` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.6153` n `32` status `ready` deltaP `8.5069` edge `0.013` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.6153` n `32` status `ready` deltaP `8.5069` edge `0.013` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
