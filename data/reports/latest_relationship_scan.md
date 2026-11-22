# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T12:52:24.004695+00:00`
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

- `market_context_high->unknown_1h` score `12036.1736` n `106` status `ready` deltaP `-0.3927` edge `1003.0369` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7510.4017` n `106` status `ready` deltaP `-2.5742` edge `625.9145` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1415.8113` n `31` status `ready` deltaP `4.4765` edge `117.972` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `3.9858` n `31` status `ready` deltaP `19.688` edge `0.2196` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.7094` n `31` status `ready` deltaP `31.6931` edge `0.023` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5032` n `31` status `ready` deltaP `9.5615` edge `0.3033` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1111` n `31` status `ready` deltaP `8.5136` edge `0.2496` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5143` n `31` status `ready` deltaP `28.5348` edge `0.0318` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1424` n `31` status `ready` deltaP `0.4829` edge `0.0111` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3293` n `106` status `ready` deltaP `2.4545` edge `0.0079` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4071` n `106` status `ready` deltaP `1.9913` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1748` n `106` status `ready` deltaP `-8.0274` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5187` n `106` status `ready` deltaP `-0.164` edge `0.0036` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8199` n `106` status `ready` deltaP `3.3838` edge `-0.0449` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9667` n `31` status `ready` deltaP `-17.6743` edge `-0.0023` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.0466` n `106` status `ready` deltaP `5.7197` edge `-0.0111` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.2027` n `106` status `ready` deltaP `0.4745` edge `-0.0061` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.5069` n `106` status `ready` deltaP `-11.1117` edge `-0.0273` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.5359` n `106` status `ready` deltaP `-14.6945` edge `-0.0334` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7404` n `106` status `ready` deltaP `-5.2113` edge `-0.0659` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
