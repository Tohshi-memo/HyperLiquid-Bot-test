# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T11:22:25.882918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5558`

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

- `news_risk_high->unknown_1h` score `3384.8112` n `31` status `ready` deltaP `2.0813` edge `282.0713` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3258.721` n `31` status `ready` deltaP `3.7864` edge `271.5405` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.8735` n `31` status `ready` deltaP `34.4887` edge `1.6762` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6123` n `31` status `ready` deltaP `32.409` edge `1.1683` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.5858` n `31` status `ready` deltaP `27.9029` edge `0.8628` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.7784` n `31` status `ready` deltaP `22.6445` edge `0.6676` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.575` n `31` status `ready` deltaP `16.9305` edge `0.7436` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.5271` n `31` status `ready` deltaP `30.5173` edge `0.3052` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0244` n `31` status `ready` deltaP `41.4491` edge `0.1552` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8844` n `31` status `ready` deltaP `16.3471` edge `0.2422` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4794` n `31` status `ready` deltaP `30.3649` edge `0.0302` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3888` n `31` status `ready` deltaP `26.1698` edge `0.0246` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3247` n `31` status `ready` deltaP `28.5494` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1376` n `31` status `ready` deltaP `14.1491` edge `0.1025` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9699` n `31` status `ready` deltaP `7.0166` edge `0.2519` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7514` n `31` status `ready` deltaP `9.2621` edge `0.1985` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1146` n `31` status `ready` deltaP `24.3432` edge `0.0085` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.765` n `38` status `ready` deltaP `10.6787` edge `0.0337` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.422` n `31` status `ready` deltaP `10.0462` edge `0.0269` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3452` n `31` status `ready` deltaP `11.4427` edge `0.0237` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
