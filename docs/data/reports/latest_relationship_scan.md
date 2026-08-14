# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T20:51:01.550121+00:00`
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

- `market_context_high->unknown_24h` score `136.2367` n `128` status `ready` deltaP `-32.2049` edge `11.859` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8328` n `32` status `ready` deltaP `-45.4861` edge `4.5876` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8328` n `32` status `ready` deltaP `-45.4861` edge `4.5876` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.655` n `36` status `ready` deltaP `14.4097` edge `0.8298` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6813` n `36` status `ready` deltaP `40.3963` edge `0.3708` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9322` n `128` status `ready` deltaP `27.8645` edge `0.231` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5083` n `32` status `ready` deltaP `30.2083` edge `0.1743` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5083` n `32` status `ready` deltaP `30.2083` edge `0.1743` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.9502` n `32` status `ready` deltaP `20.6597` edge `0.3561` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.9502` n `32` status `ready` deltaP `20.6597` edge `0.3561` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.6644` n `32` status `ready` deltaP `18.5213` edge `0.1168` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6644` n `32` status `ready` deltaP `18.5213` edge `0.1168` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.4831` n `36` status `ready` deltaP `18.2292` edge `0.0854` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8779` n `36` status `ready` deltaP `21.5955` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7538` n `36` status `ready` deltaP `8.7326` edge `0.1198` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7166` n `128` status `ready` deltaP `16.9588` edge `0.0771` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.3018` n `32` status `ready` deltaP `13.9596` edge `0.0387` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3018` n `32` status `ready` deltaP `13.9596` edge `0.0387` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0875` n `32` status `ready` deltaP `13.1944` edge `0.0211` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0875` n `32` status `ready` deltaP `13.1944` edge `0.0211` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
