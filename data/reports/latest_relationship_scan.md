# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T12:37:35.268261+00:00`
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

- `market_context_high->unknown_1h` score `12036.1951` n `106` status `ready` deltaP `-0.243` edge `1003.0377` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7519.8313` n `106` status `ready` deltaP `-2.5742` edge `626.7003` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1415.8329` n `31` status `ready` deltaP `4.6262` edge `117.9728` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `3.9714` n `31` status `ready` deltaP `19.5383` edge `0.2194` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.7226` n `31` status `ready` deltaP `31.8428` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4915` n `31` status `ready` deltaP `9.4118` edge `0.3028` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1056` n `31` status `ready` deltaP `8.5136` edge `0.2489` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5065` n `31` status `ready` deltaP `28.3851` edge `0.0318` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1543` n `31` status `ready` deltaP `0.3332` edge `0.0111` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3371` n `106` status `ready` deltaP `2.3048` edge `0.0079` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3939` n `106` status `ready` deltaP `2.141` edge `0.0016` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1628` n `106` status `ready` deltaP `-7.8777` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8316` n `106` status `ready` deltaP `3.2341` edge `-0.0454` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9547` n `31` status `ready` deltaP `-17.5246` edge `-0.0023` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.061` n `106` status `ready` deltaP `5.57` edge `-0.0113` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.1881` n `106` status `ready` deltaP `0.627` edge `-0.0059` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.5188` n `106` status `ready` deltaP `-11.2614` edge `-0.0273` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.5347` n `106` status `ready` deltaP `-14.6945` edge `-0.0333` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7488` n `106` status `ready` deltaP `-5.2113` edge `-0.0666` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
