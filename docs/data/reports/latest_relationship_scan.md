# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T13:22:35.315098+00:00`
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

- `news_risk_high->unknown_1h` score `3403.1364` n `31` status `ready` deltaP `2.231` edge `283.5974` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3237.3166` n `31` status `ready` deltaP `3.7864` edge `269.7568` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.9984` n `31` status `ready` deltaP `35.8752` edge `1.7607` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.736` n `31` status `ready` deltaP `33.7955` edge `1.2527` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.9257` n `31` status `ready` deltaP `28.5962` edge `0.8865` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2108` n `31` status `ready` deltaP `23.864` edge `0.6955` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.8662` n `31` status `ready` deltaP `18.1501` edge `0.7728` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.7519` n `31` status `ready` deltaP `31.7369` edge `0.3158` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0665` n `31` status `ready` deltaP `41.7957` edge `0.1564` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.0174` n `31` status `ready` deltaP `17.5603` edge `0.2452` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.5914` n `31` status `ready` deltaP `31.5844` edge `0.0314` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4453` n `31` status `ready` deltaP `26.5165` edge `0.027` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3678` n `31` status `ready` deltaP `28.9985` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2551` n `31` status `ready` deltaP `14.8976` edge `0.1073` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0963` n `31` status `ready` deltaP `7.316` edge `0.2661` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.905` n `31` status `ready` deltaP `10.31` edge `0.2112` maxDD `-1.5232`
- `market_context_high->metal_4h` score `1.259` n `46` status `ready` deltaP `17.5437` edge `0.0291` maxDD `-0.2914`
- `news_risk_high->metal_1h` score `1.1449` n `31` status `ready` deltaP `24.7923` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4655` n `31` status `ready` deltaP `10.8084` edge `0.0274` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.353` n `31` status `ready` deltaP `11.4427` edge `0.0247` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
