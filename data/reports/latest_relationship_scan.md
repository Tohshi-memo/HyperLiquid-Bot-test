# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T00:22:29.153309+00:00`
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

- `market_context_high->unknown_24h` score `136.5139` n `128` status `ready` deltaP `-29.7744` edge `11.8659` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.013` n `32` status `ready` deltaP `-43.0556` edge `4.5945` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.013` n `32` status `ready` deltaP `-43.0556` edge `4.5945` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.189` n `36` status `ready` deltaP `16.8402` edge `0.8581` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6583` n `36` status `ready` deltaP `40.2439` edge `0.3699` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9178` n `128` status `ready` deltaP `27.8645` edge `0.2298` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4939` n `32` status `ready` deltaP `30.2083` edge `0.1731` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4939` n `32` status `ready` deltaP `30.2083` edge `0.1731` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.4923` n `32` status `ready` deltaP `23.0903` edge `0.4094` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.4923` n `32` status `ready` deltaP `23.0903` edge `0.4094` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.7148` n `36` status `ready` deltaP `20.6597` edge `0.0885` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6596` n `32` status `ready` deltaP `18.5213` edge `0.1164` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6596` n `32` status `ready` deltaP `18.5213` edge `0.1164` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.7963` n `36` status `ready` deltaP `20.6809` edge `0.025` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7861` n `36` status `ready` deltaP `9.032` edge `0.1205` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7118` n `128` status `ready` deltaP `16.9588` edge `0.0767` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.206` n `32` status `ready` deltaP `12.9117` edge `0.0377` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.206` n `32` status `ready` deltaP `12.9117` edge `0.0377` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.9119` n `32` status `ready` deltaP `11.2847` edge `0.0192` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.9119` n `32` status `ready` deltaP `11.2847` edge `0.0192` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
