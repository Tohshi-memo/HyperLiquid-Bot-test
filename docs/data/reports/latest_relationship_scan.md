# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T03:07:34.046976+00:00`
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

- `market_context_high->unknown_24h` score `136.7579` n `128` status `ready` deltaP `-27.8646` edge `11.8735` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1716` n `32` status `ready` deltaP `-41.1458` edge `4.6021` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1716` n `32` status `ready` deltaP `-41.1458` edge `4.6021` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.5086` n `36` status `ready` deltaP `18.75` edge `0.872` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.538` n `36` status `ready` deltaP `39.0244` edge `0.368` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9178` n `128` status `ready` deltaP `27.8645` edge `0.2298` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4939` n `32` status `ready` deltaP `30.2083` edge `0.1731` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4939` n `32` status `ready` deltaP `30.2083` edge `0.1731` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.8381` n `32` status `ready` deltaP `25.0` edge `0.441` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.8381` n `32` status `ready` deltaP `25.0` edge `0.441` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.888` n `36` status `ready` deltaP `22.5694` edge `0.0902` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6852` n `32` status `ready` deltaP `18.8262` edge `0.1165` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6852` n `32` status `ready` deltaP `18.8262` edge `0.1165` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.7683` n `36` status `ready` deltaP `20.376` edge `0.0247` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.7374` n `128` status `ready` deltaP `17.2637` edge `0.0768` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.7214` n `36` status `ready` deltaP `8.2835` edge `0.1201` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2371` n `32` status `ready` deltaP `13.2111` edge `0.0383` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2371` n `32` status `ready` deltaP `13.2111` edge `0.0383` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.743` n `32` status `ready` deltaP `9.5486` edge `0.0167` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.743` n `32` status `ready` deltaP `9.5486` edge `0.0167` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
