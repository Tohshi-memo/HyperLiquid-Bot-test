# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T05:22:26.944356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3656`

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

- `news_risk_high->unknown_1h` score `3338.0425` n `31` status `ready` deltaP `1.4825` edge `278.1779` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3194.3781` n `31` status `ready` deltaP `3.634` edge `266.1796` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.3115` n `31` status `ready` deltaP `30.3293` edge `1.4071` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.3936` n `31` status `ready` deltaP `28.2496` edge `0.9278` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.4552` n `31` status `ready` deltaP `24.0901` edge `0.794` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.4127` n `31` status `ready` deltaP `19.7482` edge `0.5731` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.0316` n `31` status `ready` deltaP `27.7734` edge `0.2822` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7426` n `31` status `ready` deltaP `38.6762` edge `0.1502` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.5802` n `31` status `ready` deltaP `13.7293` edge `0.6374` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3735` n `31` status `ready` deltaP `12.361` edge `0.2262` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2325` n `31` status `ready` deltaP `27.5015` edge `0.0112` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.1873` n `31` status `ready` deltaP `27.1637` edge `0.0272` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.1872` n `31` status `ready` deltaP `24.6101` edge `0.0182` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0464` n `31` status `ready` deltaP `13.9994` edge `0.0959` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.655` n `31` status `ready` deltaP `5.0705` edge `0.2245` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5542` n `31` status `ready` deltaP `8.3639` edge `0.1792` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0772` n `31` status `ready` deltaP `23.7444` edge `0.0077` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3175` n `31` status `ready` deltaP `8.2169` edge `0.0257` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.226` n `31` status `ready` deltaP `9.7659` edge `0.0196` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3495` n `31` status `ready` deltaP `-2.2117` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
