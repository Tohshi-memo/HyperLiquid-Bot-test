# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T11:07:27.848222+00:00`
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

- `market_context_high->unknown_1h` score `12048.4495` n `106` status `ready` deltaP `-0.243` edge `1004.0589` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7534.7247` n `106` status `ready` deltaP `-2.4218` edge `627.9404` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1428.0873` n `31` status `ready` deltaP `4.6262` edge `118.994` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `3.9978` n `31` status `ready` deltaP `19.8377` edge `0.2196` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.6855` n `31` status `ready` deltaP `31.3937` edge `0.023` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4736` n `31` status `ready` deltaP `9.2621` edge `0.3015` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0799` n `31` status `ready` deltaP `8.2142` edge `0.2476` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4979` n `31` status `ready` deltaP `28.2354` edge `0.0317` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1543` n `31` status `ready` deltaP `0.3332` edge `0.0111` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3456` n `106` status `ready` deltaP `2.1551` edge `0.0078` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4311` n `106` status `ready` deltaP `1.6919` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1256` n `106` status `ready` deltaP `-7.4286` edge `-0.0013` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8496` n `106` status `ready` deltaP `3.0844` edge `-0.0467` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9176` n `31` status `ready` deltaP `-17.0755` edge `-0.0022` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.0346` n `106` status `ready` deltaP `5.8694` edge `-0.0111` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.1115` n `106` status `ready` deltaP `1.3892` edge `-0.0046` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.5188` n `106` status `ready` deltaP `-11.2614` edge `-0.0273` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.4776` n `106` status `ready` deltaP `-14.0848` edge `-0.0326` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7884` n `106` status `ready` deltaP `-5.5107` edge `-0.0679` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
