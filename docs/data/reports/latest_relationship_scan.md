# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T00:07:29.364935+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11717`

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

- `market_context_high->unknown_24h` score `137.4222` n `104` status `ready` deltaP `-26.6582` edge `18.0643` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.6697` n `32` status `ready` deltaP `-38.437` edge `4.6479` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6697` n `32` status `ready` deltaP `-38.437` edge `4.6479` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9334` n `36` status `ready` deltaP `26.3142` edge `0.9403` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6713` n `36` status `ready` deltaP `39.1768` edge `0.3781` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.8307` n `104` status `ready` deltaP `38.1116` edge `0.3209` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.6976` n `32` status `ready` deltaP `40.0347` edge `0.2079` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6976` n `32` status `ready` deltaP `40.0347` edge `0.2079` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.9926` n `32` status `ready` deltaP `27.161` edge `0.4464` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.9926` n `32` status `ready` deltaP `27.161` edge `0.4464` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7661` n `36` status `ready` deltaP `31.7158` edge `0.1024` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0059` n `32` status `ready` deltaP `21.875` edge `0.1229` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0059` n `32` status `ready` deltaP `21.875` edge `0.1229` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2993` n `104` status `ready` deltaP `20.6731` edge `0.1009` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0156` n `36` status `ready` deltaP `23.2723` edge `0.026` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.761` n `36` status `ready` deltaP `8.4332` edge `0.1224` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3737` n `32` status `ready` deltaP `14.7081` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.7777` n `32` status `ready` deltaP `9.5274` edge `0.0154` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.7777` n `32` status `ready` deltaP `9.5274` edge `0.0154` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
