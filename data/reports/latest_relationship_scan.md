# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T00:07:29.425408+00:00`
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

- `market_context_high->unknown_24h` score `136.4904` n `128` status `ready` deltaP `-29.948` edge `11.8651` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9977` n `32` status `ready` deltaP `-43.2292` edge `4.5937` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9977` n `32` status `ready` deltaP `-43.2292` edge `4.5937` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.1536` n `36` status `ready` deltaP `16.6666` edge `0.8563` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6717` n `36` status `ready` deltaP `40.3963` edge `0.37` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9202` n `128` status `ready` deltaP `27.8645` edge `0.23` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4963` n `32` status `ready` deltaP `30.2083` edge `0.1733` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4963` n `32` status `ready` deltaP `30.2083` edge `0.1733` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.4568` n `32` status `ready` deltaP `22.9167` edge `0.406` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.4568` n `32` status `ready` deltaP `22.9167` edge `0.406` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.6973` n `36` status `ready` deltaP `20.4861` edge `0.0882` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.662` n `32` status `ready` deltaP `18.5213` edge `0.1166` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.662` n `32` status `ready` deltaP `18.5213` edge `0.1166` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.7829` n `36` status `ready` deltaP `20.5284` edge `0.0249` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7729` n `36` status `ready` deltaP `8.8823` edge `0.1204` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7142` n `128` status `ready` deltaP `16.9588` edge `0.0769` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2072` n `32` status `ready` deltaP `12.9117` edge `0.0378` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2072` n `32` status `ready` deltaP `12.9117` edge `0.0378` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.927` n `32` status `ready` deltaP `11.4583` edge `0.0193` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.927` n `32` status `ready` deltaP `11.4583` edge `0.0193` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
