# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T19:52:26.129150+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3144`

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

- `news_risk_high->unknown_1h` score `3217.9956` n `31` status `ready` deltaP `2.231` edge `268.169` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3205.1238` n `31` status `ready` deltaP `4.3962` edge `267.07` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `29.7211` n `31` status `ready` deltaP `38.8889` edge `2.2175` maxDD `0.0`
- `news_risk_high->equity_24h` score `27.1341` n `31` status `ready` deltaP `38.0208` edge `2.0077` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.5792` n `31` status `ready` deltaP `38.1944` edge `1.7103` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.1085` n `31` status `ready` deltaP `24.9311` edge `0.7632` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.0131` n `31` status `ready` deltaP `37.0722` edge `0.552` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.8185` n `31` status `ready` deltaP `24.5688` edge `0.4319` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.5353` n `31` status `ready` deltaP `17.9976` edge `0.8596` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9036` n `31` status `ready` deltaP `41.3643` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.7716` n `31` status `ready` deltaP `39.4097` edge `0.1349` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3955` n `31` status `ready` deltaP `19.5383` edge `0.1714` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.165` n `31` status `ready` deltaP `35.3954` edge `0.0538` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6279` n `31` status `ready` deltaP `31.3937` edge `0.0182` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3052` n `31` status `ready` deltaP `8.3639` edge `0.2859` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0765` n `31` status `ready` deltaP `11.3579` edge `0.2262` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4191` n `31` status `ready` deltaP `28.2354` edge `0.0216` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8477` n `31` status `ready` deltaP `14.4915` edge `0.0678` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3008` n `31` status `ready` deltaP `10.656` edge `0.0073` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4814` n `31` status `ready` deltaP `-3.1099` edge `0.0068` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
