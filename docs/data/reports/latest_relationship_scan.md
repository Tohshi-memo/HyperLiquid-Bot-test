# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T10:22:23.997963+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4008`

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

- `market_context_high->unknown_1h` score `12055.4347` n `106` status `ready` deltaP `0.0564` edge `1004.639` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7543.0397` n `106` status `ready` deltaP `-2.2694` edge `628.6323` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.3285` n `106` status `ready` deltaP `2.4545` edge `0.008` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4179` n `106` status `ready` deltaP `1.8416` edge `0.0016` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1137` n `106` status `ready` deltaP `-7.2789` edge `-0.0013` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8527` n `106` status `ready` deltaP `2.9347` edge `-0.0461` maxDD `-13.8788`
- `market_context_high->equity_1h` score `-1.9963` n `106` status `ready` deltaP `6.1688` edge `-0.0099` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.0909` n `106` status `ready` deltaP `1.5416` edge `-0.0039` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.5308` n `106` status `ready` deltaP `-11.4111` edge `-0.0273` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.446` n `106` status `ready` deltaP `-13.7799` edge `-0.032` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7608` n `106` status `ready` deltaP `-5.361` edge `-0.0666` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-4.9001` n `106` status `ready` deltaP `-8.3432` edge `-0.0034` maxDD `-5.9453`
- `market_context_high->commodity_4h` score `-6.8088` n `106` status `ready` deltaP `-17.5736` edge `-0.0906` maxDD `-14.7712`
- `market_context_high->metal_24h` score `-10.2901` n `106` status `ready` deltaP `-9.3913` edge `0.0147` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-11.4538` n `106` status `ready` deltaP `-8.968` edge `-0.2018` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-11.6175` n `106` status `ready` deltaP `-9.5777` edge `-0.223` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.756` n `106` status `ready` deltaP `-28.0071` edge `-0.3592` maxDD `-62.4905`
- `market_context_high->crypto_major_24h` score `-16.005` n `106` status `ready` deltaP `6.7479` edge `-0.0369` maxDD `-152.134`
- `market_context_high->index_24h` score `-16.1849` n `106` status `ready` deltaP `-33.6806` edge `-0.1846` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
