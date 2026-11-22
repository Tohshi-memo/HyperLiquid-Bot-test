# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T04:37:27.739458+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4576`

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

- `market_context_high->unknown_1h` score `9861.7931` n `125` status `ready` deltaP `1.2766` edge `821.8274` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `5918.3234` n `125` status `ready` deltaP `-0.6829` edge `493.2287` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2375` n `125` status `ready` deltaP `3.5904` edge `0.0121` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.404` n `125` status `ready` deltaP `0.3952` edge `0.0026` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8409` n `125` status `ready` deltaP `7.7561` edge `0.0211` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4328` n `125` status `ready` deltaP `-9.3078` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8159` n `125` status `ready` deltaP `-4.9671` edge `0.0019` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.0739` n `125` status `ready` deltaP `3.5437` edge `0.0053` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3089` n `125` status `ready` deltaP `-8.5545` edge `-0.0222` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8623` n `125` status `ready` deltaP `-8.2085` edge `-0.0205` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.1486` n `125` status `ready` deltaP `0.0958` edge `-0.0312` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8797` n `125` status `ready` deltaP `-6.5521` edge `-0.0519` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-5.9605` n `125` status `ready` deltaP `-8.2069` edge `-0.0003` maxDD `-7.002`
- `market_context_high->crypto_major_4h` score `-5.9724` n `125` status `ready` deltaP `-4.589` edge `-0.0422` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.9007` n `125` status `ready` deltaP `-18.9866` edge `-0.0792` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.0488` n `125` status `ready` deltaP `4.3444` edge `0.1099` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.8326` n `125` status `ready` deltaP `-4.7415` edge `-0.1065` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.909` n `125` status `ready` deltaP `13.1556` edge `0.3173` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.9513` n `125` status `ready` deltaP `-26.9028` edge `-0.1228` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.6376` n `125` status `ready` deltaP `3.375` edge `0.0909` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
