# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T11:22:31.534984+00:00`
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

- `market_context_high->unknown_1h` score `12041.8915` n `106` status `ready` deltaP `-0.243` edge `1003.5124` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7530.6733` n `106` status `ready` deltaP `-2.5742` edge `627.6038` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1421.5293` n `31` status `ready` deltaP `4.6262` edge `118.4475` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `3.9978` n `31` status `ready` deltaP `19.8377` edge `0.2196` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.6974` n `31` status `ready` deltaP `31.5434` edge `0.023` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4728` n `31` status `ready` deltaP `9.2621` edge `0.3014` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.069` n `31` status `ready` deltaP `8.0645` edge `0.2472` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4901` n `31` status `ready` deltaP `28.0857` edge `0.0317` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1675` n `31` status `ready` deltaP `0.1835` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3534` n `106` status `ready` deltaP `2.0054` edge `0.0078` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4191` n `106` status `ready` deltaP `1.8416` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1256` n `106` status `ready` deltaP `-7.4286` edge `-0.0013` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8503` n `106` status `ready` deltaP `3.0844` edge `-0.0468` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9176` n `31` status `ready` deltaP `-17.0755` edge `-0.0022` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.0346` n `106` status `ready` deltaP `5.8694` edge `-0.0111` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.1139` n `106` status `ready` deltaP `1.3892` edge `-0.0048` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.532` n `106` status `ready` deltaP `-11.4111` edge `-0.0274` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.4788` n `106` status `ready` deltaP `-14.0848` edge `-0.0327` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.8052` n `106` status `ready` deltaP `-5.6604` edge `-0.0683` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
