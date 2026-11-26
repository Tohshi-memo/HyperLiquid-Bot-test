# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T19:37:27.701427+00:00`
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

- `news_risk_high->unknown_1h` score `3218.3652` n `31` status `ready` deltaP `2.231` edge `268.1998` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3205.8414` n `31` status `ready` deltaP `4.3962` edge `267.1298` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `29.9114` n `31` status `ready` deltaP `39.0625` edge `2.2322` maxDD `0.0`
- `news_risk_high->equity_24h` score `27.3532` n `31` status `ready` deltaP `38.1944` edge `2.0248` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.7634` n `31` status `ready` deltaP `38.3681` edge `1.7245` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.1483` n `31` status `ready` deltaP `25.0836` edge `0.7655` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.0733` n `31` status `ready` deltaP `37.2247` edge `0.556` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.8648` n `31` status `ready` deltaP `24.7424` edge `0.4346` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.5643` n `31` status `ready` deltaP `18.1501` edge `0.8623` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9036` n `31` status `ready` deltaP `41.3643` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.8047` n `31` status `ready` deltaP `39.5833` edge `0.1365` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4159` n `31` status `ready` deltaP `19.688` edge `0.1721` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1808` n `31` status `ready` deltaP `35.5478` edge `0.0541` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.641` n `31` status `ready` deltaP `31.5434` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.32` n `31` status `ready` deltaP `8.5136` edge `0.2868` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0905` n `31` status `ready` deltaP `11.5076` edge `0.227` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4277` n `31` status `ready` deltaP `28.3851` edge `0.0217` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8539` n `31` status `ready` deltaP `14.4915` edge `0.0686` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2913` n `31` status `ready` deltaP `10.5035` edge `0.0071` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4814` n `31` status `ready` deltaP `-3.1099` edge `0.0068` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
