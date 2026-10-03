# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T00:52:26.742635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.0679` n `50` status `ready` deltaP `10.4251` edge `30.2744` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.4461` n `50` status `ready` deltaP `10.3659` edge `24.3014` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.1798` n `70` status `ready` deltaP `34.1915` edge `1.0943` maxDD `-2.2476`
- `market_context_high->crypto_alt_24h` score `10.8142` n `50` status `ready` deltaP `21.0486` edge `0.9312` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.5822` n `70` status `ready` deltaP `33.7351` edge `0.6221` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9843` n `50` status `ready` deltaP `31.6528` edge `0.6793` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.6465` n `50` status `ready` deltaP `18.4573` edge `0.5845` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `7.2682` n `106` status `ready` deltaP `28.8743` edge `0.5476` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.0717` n `50` status `ready` deltaP `16.7988` edge `0.5229` maxDD `-7.6465`
- `news_risk_high->crypto_major_24h` score `3.4891` n `70` status `ready` deltaP `9.6528` edge `0.5653` maxDD `-8.5861`
- `market_context_high->crypto_alt_1h` score `3.2326` n `50` status `ready` deltaP `14.8024` edge `0.237` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `3.1019` n `106` status `ready` deltaP `25.8543` edge `0.1474` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0097` n `50` status `ready` deltaP `13.4012` edge `0.2065` maxDD `-2.2692`
- `news_risk_high->crypto_major_4h` score `2.9589` n `106` status `ready` deltaP `21.212` edge `0.385` maxDD `-7.0989`
- `market_context_high->fx_4h` score `2.8287` n `50` status `ready` deltaP `31.622` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->index_24h` score `1.6536` n `70` status `ready` deltaP `19.2361` edge `0.0546` maxDD `-0.2696`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.2694` n `50` status `ready` deltaP `6.0208` edge `0.3088` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.2501` n `106` status `ready` deltaP `5.4062` edge `0.1242` maxDD `-2.4854`
- `news_risk_high->metal_24h` score `1.2239` n `70` status `ready` deltaP `12.1429` edge `0.2019` maxDD `-2.0759`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
