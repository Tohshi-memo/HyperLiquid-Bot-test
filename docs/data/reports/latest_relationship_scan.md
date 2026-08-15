# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T04:56:05.173916+00:00`
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

- `market_context_high->unknown_24h` score `136.6975` n `128` status `ready` deltaP `-28.5591` edge `11.8731` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1323` n `32` status `ready` deltaP `-41.8403` edge `4.6017` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1323` n `32` status `ready` deltaP `-41.8403` edge `4.6017` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.6934` n `36` status `ready` deltaP `19.9652` edge `0.8793` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4298` n `36` status `ready` deltaP `37.9573` edge `0.3661` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9262` n `128` status `ready` deltaP `27.8645` edge `0.2305` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5023` n `32` status `ready` deltaP `30.2083` edge `0.1738` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5023` n `32` status `ready` deltaP `30.2083` edge `0.1738` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.977` n `32` status `ready` deltaP `26.2153` edge `0.4507` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.977` n `32` status `ready` deltaP `26.2153` edge `0.4507` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.9948` n `36` status `ready` deltaP `23.7847` edge `0.091` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.751` n `32` status `ready` deltaP `19.5884` edge `0.1169` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.751` n `32` status `ready` deltaP `19.5884` edge `0.1169` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.8032` n `128` status `ready` deltaP `18.0259` edge `0.0772` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.6891` n `36` status `ready` deltaP `19.4613` edge `0.0242` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6544` n `36` status `ready` deltaP `7.535` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2359` n `32` status `ready` deltaP `13.2111` edge `0.0382` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2359` n `32` status `ready` deltaP `13.2111` edge `0.0382` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.6912` n `32` status `ready` deltaP `9.2014` edge `0.0147` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.6912` n `32` status `ready` deltaP `9.2014` edge `0.0147` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
