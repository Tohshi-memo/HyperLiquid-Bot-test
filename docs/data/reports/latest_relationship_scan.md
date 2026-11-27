# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T21:22:33.633741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2832`

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

- `news_risk_high->unknown_1h` score `3293.5801` n `31` status `ready` deltaP `1.6322` edge `274.4717` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3173.3157` n `31` status `ready` deltaP `3.3191` edge `264.4265` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.0038` n `31` status `ready` deltaP `26.8631` edge `1.2379` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.3436` n `31` status `ready` deltaP `26.6898` edge `0.8507` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.3197` n `31` status `ready` deltaP `23.9168` edge `0.8672` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2411` n `31` status `ready` deltaP `21.0438` edge `0.6335` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4653` n `31` status `ready` deltaP `29.6853` edge `0.3056` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1499` n `31` status `ready` deltaP `14.4105` edge `0.7059` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6682` n `31` status `ready` deltaP `38.6762` edge `0.144` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6704` n `31` status `ready` deltaP `12.1877` edge `0.2521` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.345` n `31` status `ready` deltaP `28.9243` edge `0.0286` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2337` n `31` status `ready` deltaP `27.5015` edge `0.0113` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2124` n `31` status `ready` deltaP `24.6101` edge `0.0203` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1675` n `31` status `ready` deltaP `14.7479` edge `0.101` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8796` n `31` status `ready` deltaP `5.9687` edge `0.2473` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6587` n `31` status `ready` deltaP `8.3639` edge `0.1926` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1224` n `31` status `ready` deltaP `24.4929` edge `0.0085` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4472` n `31` status `ready` deltaP `10.5759` edge `0.0266` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3656` n `31` status `ready` deltaP `11.6708` edge `0.0248` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3244` n `31` status `ready` deltaP `-1.9123` edge `0.0119` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
