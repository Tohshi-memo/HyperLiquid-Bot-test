# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T10:52:32.417148+00:00`
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

- `market_context_high->unknown_1h` score `12051.3091` n `106` status `ready` deltaP `-0.243` edge `1004.2972` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7538.6523` n `106` status `ready` deltaP `-2.4218` edge `628.2677` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1430.9469` n `31` status `ready` deltaP `4.6262` edge `119.2323` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `4.0133` n `31` status `ready` deltaP `19.9874` edge `0.2199` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.6855` n `31` status `ready` deltaP `31.3937` edge `0.023` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.465` n `31` status `ready` deltaP `9.1124` edge `0.3014` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0893` n `31` status `ready` deltaP `8.3639` edge `0.2478` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5065` n `31` status `ready` deltaP `28.3851` edge `0.0318` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1675` n `31` status `ready` deltaP `0.1835` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3371` n `106` status `ready` deltaP `2.3048` edge `0.0079` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4311` n `106` status `ready` deltaP `1.6919` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1137` n `106` status `ready` deltaP `-7.2789` edge `-0.0013` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8581` n `106` status `ready` deltaP `2.9347` edge `-0.0468` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9056` n `31` status `ready` deltaP `-16.9258` edge `-0.0022` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.0191` n `106` status `ready` deltaP `6.0191` edge `-0.0108` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.0957` n `106` status `ready` deltaP `1.5416` edge `-0.0043` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.532` n `106` status `ready` deltaP `-11.4111` edge `-0.0274` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.463` n `106` status `ready` deltaP `-13.9323` edge `-0.0324` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.774` n `106` status `ready` deltaP `-5.361` edge `-0.0677` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
