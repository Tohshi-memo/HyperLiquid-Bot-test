# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T10:52:27.915558+00:00`
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

- `market_context_high->unknown_24h` score `137.3523` n `128` status `ready` deltaP `-25.849` edge `11.9096` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.558` n `32` status `ready` deltaP `-39.1302` edge `4.6382` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.558` n `32` status `ready` deltaP `-39.1302` edge `4.6382` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.4194` n `36` status `ready` deltaP `23.7146` edge `0.9148` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6531` n `36` status `ready` deltaP `39.8782` edge `0.3719` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.3353` n `128` status `ready` deltaP `30.7585` edge `0.2453` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9114` n `32` status `ready` deltaP `33.1023` edge `0.1886` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9114` n `32` status `ready` deltaP `33.1023` edge `0.1886` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2347` n `32` status `ready` deltaP `28.2008` edge `0.4705` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2347` n `32` status `ready` deltaP `28.2008` edge `0.4705` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.4022` n `36` status `ready` deltaP `27.9029` edge `0.0975` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0371` n `32` status `ready` deltaP `22.265` edge `0.1229` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0371` n `32` status `ready` deltaP `22.265` edge `0.1229` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0893` n `128` status `ready` deltaP `20.7025` edge `0.0832` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8915` n `36` status `ready` deltaP `21.8417` edge `0.0252` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7622` n `36` status `ready` deltaP `8.7326` edge `0.1205` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3258` n `32` status `ready` deltaP `14.1093` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3258` n `32` status `ready` deltaP `14.1093` edge `0.0397` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6892` n `128` status `ready` deltaP `9.4218` edge `0.0243` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5362` n `32` status `ready` deltaP `6.5687` edge `0.015` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
