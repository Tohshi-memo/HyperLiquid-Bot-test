# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T12:22:31.943079+00:00`
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

- `market_context_high->unknown_1h` score `12036.2035` n `106` status `ready` deltaP `-0.243` edge `1003.0384` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7522.3549` n `106` status `ready` deltaP `-2.5742` edge `626.9106` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1415.8413` n `31` status `ready` deltaP `4.6262` edge `117.9735` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `3.9678` n `31` status `ready` deltaP `19.5383` edge `0.2191` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.7214` n `31` status `ready` deltaP `31.8428` edge `0.023` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4853` n `31` status `ready` deltaP `9.4118` edge `0.302` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0908` n `31` status `ready` deltaP `8.3639` edge `0.248` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4979` n `31` status `ready` deltaP `28.2354` edge `0.0317` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1663` n `31` status `ready` deltaP `0.1835` edge `0.0111` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3456` n `106` status `ready` deltaP `2.1551` edge `0.0078` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3951` n `106` status `ready` deltaP `2.141` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1628` n `106` status `ready` deltaP `-7.8777` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8379` n `106` status `ready` deltaP `3.2341` edge `-0.0462` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9547` n `31` status `ready` deltaP `-17.5246` edge `-0.0023` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.0646` n `106` status `ready` deltaP `5.57` edge `-0.0116` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.1747` n `106` status `ready` deltaP `0.7794` edge `-0.0058` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.5308` n `106` status `ready` deltaP `-11.4111` edge `-0.0273` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.5347` n `106` status `ready` deltaP `-14.6945` edge `-0.0333` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7716` n `106` status `ready` deltaP `-5.361` edge `-0.0675` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
