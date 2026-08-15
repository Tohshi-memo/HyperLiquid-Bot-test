# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T22:37:26.514931+00:00`
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

- `market_context_high->unknown_24h` score `123.3384` n `110` status `ready` deltaP `-27.4539` edge `16.264` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.7581` n `32` status `ready` deltaP `-37.3971` edge `4.6523` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7581` n `32` status `ready` deltaP `-37.3971` edge `4.6523` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9791` n `36` status `ready` deltaP `26.6609` edge `0.9418` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7115` n `36` status `ready` deltaP `39.6341` edge `0.3784` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6491` n `110` status `ready` deltaP `37.1766` edge `0.312` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.5508` n `32` status `ready` deltaP `38.9948` edge `0.2026` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5508` n `32` status `ready` deltaP `38.9948` edge `0.2026` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.029` n `32` status `ready` deltaP `27.6809` edge `0.4476` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.029` n `32` status `ready` deltaP `27.6809` edge `0.4476` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.8239` n `36` status `ready` deltaP `32.409` edge `0.1026` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9256` n `32` status `ready` deltaP `20.9604` edge `0.1223` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9256` n `32` status `ready` deltaP `20.9604` edge `0.1223` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2537` n `110` status `ready` deltaP `21.0172` edge `0.0948` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0168` n `36` status `ready` deltaP `23.2723` edge `0.0261` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7993` n `36` status `ready` deltaP `8.8823` edge `0.1226` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.412` n `32` status `ready` deltaP `15.1572` edge `0.0399` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.412` n `32` status `ready` deltaP `15.1572` edge `0.0399` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7903` n `32` status `ready` deltaP `15.2026` edge `0.1779` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7903` n `32` status `ready` deltaP `15.2026` edge `0.1779` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
