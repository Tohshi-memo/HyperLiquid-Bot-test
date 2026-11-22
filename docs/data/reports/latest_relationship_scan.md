# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T19:22:30.607423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4102`

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

- `market_context_high->unknown_1h` score `12012.7232` n `106` status `ready` deltaP `-0.6921` edge `1001.0847` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7480.0217` n `106` status `ready` deltaP `-2.2694` edge `623.3808` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1392.3609` n `31` status `ready` deltaP `4.1771` edge `116.0198` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1230.1633` n `31` status `ready` deltaP `3.9388` edge `102.493` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0356` n `31` status `ready` deltaP `40.2734` edge `0.7827` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.8341` n `31` status `ready` deltaP `24.6262` edge `0.8257` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6762` n `31` status `ready` deltaP `14.7964` edge `0.899` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9415` n `31` status `ready` deltaP `19.2389` edge `0.2189` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4926` n `31` status `ready` deltaP `36.31` edge `0.075` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6711` n `31` status `ready` deltaP `31.244` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4198` n `31` status `ready` deltaP `9.1124` edge `0.2956` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0549` n `31` status `ready` deltaP `8.3639` edge `0.2434` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5669` n `31` status `ready` deltaP `21.0464` edge `0.1163` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5314` n `31` status `ready` deltaP `28.8342` edge `0.032` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7895` n `31` status `ready` deltaP `17.6682` edge `0.0232` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0813` n `31` status `ready` deltaP `1.2314` edge `0.0112` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3122` n `106` status `ready` deltaP `2.7539` edge `0.0081` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4454` n `106` status `ready` deltaP `1.5422` edge `0.0013` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2346` n `106` status `ready` deltaP `-8.7759` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5204` n `106` status `ready` deltaP `-0.3164` edge `0.0044` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
