# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T22:52:26.333562+00:00`
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

- `market_context_high->unknown_24h` score `136.3922` n `128` status `ready` deltaP `-30.816` edge `11.8627` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9339` n `32` status `ready` deltaP `-44.0972` edge `4.5913` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9339` n `32` status `ready` deltaP `-44.0972` edge `4.5913` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.9605` n `36` status `ready` deltaP `15.7986` edge `0.846` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6813` n `36` status `ready` deltaP `40.3963` edge `0.3708` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9238` n `128` status `ready` deltaP `27.8645` edge `0.2303` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4999` n `32` status `ready` deltaP `30.2083` edge `0.1736` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4999` n `32` status `ready` deltaP `30.2083` edge `0.1736` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.2798` n `32` status `ready` deltaP `22.0486` edge `0.3891` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.2798` n `32` status `ready` deltaP `22.0486` edge `0.3891` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.6778` n `32` status `ready` deltaP `18.6738` edge `0.1169` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6778` n `32` status `ready` deltaP `18.6738` edge `0.1169` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.6134` n `36` status `ready` deltaP `19.6181` edge `0.087` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7975` n `36` status `ready` deltaP `20.6809` edge `0.0251` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.73` n `128` status `ready` deltaP `17.1113` edge `0.0772` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.7274` n `36` status `ready` deltaP `8.4332` edge `0.1196` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2347` n `32` status `ready` deltaP `13.2111` edge `0.0381` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2347` n `32` status `ready` deltaP `13.2111` edge `0.0381` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0048` n `32` status `ready` deltaP `12.3264` edge `0.02` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0048` n `32` status `ready` deltaP `12.3264` edge `0.02` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
