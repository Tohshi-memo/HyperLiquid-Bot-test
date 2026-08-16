# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T00:22:32.908665+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `139.9347` n `103` status `ready` deltaP `-26.5047` edge `18.3854` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.6544` n `32` status `ready` deltaP `-38.6103` edge `4.6471` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6544` n `32` status `ready` deltaP `-38.6103` edge `4.6471` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9147` n `36` status `ready` deltaP `26.1409` edge `0.9399` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.658` n `36` status `ready` deltaP `39.0244` edge `0.378` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.8575` n `103` status `ready` deltaP `38.2663` edge `0.3221` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.7258` n `32` status `ready` deltaP `40.208` edge `0.2091` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7258` n `32` status `ready` deltaP `40.208` edge `0.2091` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.9766` n `32` status `ready` deltaP `26.9877` edge `0.4455` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.9766` n `32` status `ready` deltaP `26.9877` edge `0.4455` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.751` n `36` status `ready` deltaP `31.5425` edge `0.1023` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0205` n `32` status `ready` deltaP `22.0274` edge `0.1231` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0205` n `32` status `ready` deltaP `22.0274` edge `0.1231` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.225` n `104` status `ready` deltaP `19.8639` edge `0.1001` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0034` n `36` status `ready` deltaP `23.1199` edge `0.026` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.761` n `36` status `ready` deltaP `8.4332` edge `0.1224` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.7777` n `32` status `ready` deltaP `9.5274` edge `0.0154` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.7777` n `32` status `ready` deltaP `9.5274` edge `0.0154` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
