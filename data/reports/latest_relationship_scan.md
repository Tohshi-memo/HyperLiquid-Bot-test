# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T19:22:26.531667+00:00`
- Price records: `672`
- Market context records: `6116`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `9.3266` n `30` status `ready` deltaP `36.9097` edge `0.5459` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.9604` n `30` status `ready` deltaP `70.6597` edge `0.1923` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2141` n `32` status `ready` deltaP `43.8262` edge `0.0636` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3536` n `32` status `ready` deltaP `28.2934` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2519` n `32` status `ready` deltaP `13.6789` edge `0.116` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8645` n `195` status `ready` deltaP `6.189` edge `0.1225` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6135` n `32` status `ready` deltaP `8.4768` edge `0.0683` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0058` n `30` status `ready` deltaP `9.0625` edge `0.026` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `195` status `ready` deltaP `0.9857` edge `-0.0005` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4735` n `30` status `ready` deltaP `14.0973` edge `-0.1129` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6831` n `195` status `ready` deltaP `3.0848` edge `0.0106` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7104` n `195` status `ready` deltaP `-1.6897` edge `-0.0033` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7417` n `195` status `ready` deltaP `0.0399` edge `0.0162` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7987` n `32` status `ready` deltaP `-3.2934` edge `-0.0307` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8632` n `195` status `ready` deltaP `2.0912` edge `-0.006` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.9334` n `195` status `ready` deltaP `1.0889` edge `0.0195` maxDD `-1.381`
- `market_context_high->crypto_major_1h` score `-0.9461` n `195` status `ready` deltaP `4.4642` edge `0.0257` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9624` n `195` status `ready` deltaP `3.4608` edge `0.0288` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.1529` n `32` status `ready` deltaP `-10.5726` edge `-0.021` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.3006` n `195` status `ready` deltaP `-3.5053` edge `0.0019` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
