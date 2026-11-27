# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T22:52:32.924117+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3302.2261` n `31` status `ready` deltaP `1.6322` edge `275.1922` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3166.7729` n `31` status `ready` deltaP `3.3291` edge `263.8812` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.3474` n `31` status `ready` deltaP `27.9029` edge `1.2596` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4054` n `31` status `ready` deltaP `26.8631` edge `0.8547` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.0665` n `31` status `ready` deltaP `23.9168` edge `0.8461` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1843` n `31` status `ready` deltaP `20.6628` edge `0.6313` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4901` n `31` status `ready` deltaP `29.7551` edge `0.3072` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1376` n `31` status `ready` deltaP `14.3391` edge `0.7048` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6778` n `31` status `ready` deltaP `38.6762` edge `0.1448` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.572` n `31` status `ready` deltaP `12.1877` edge `0.2439` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3528` n `31` status `ready` deltaP `28.993` edge `0.0288` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.3042` n `31` status `ready` deltaP `15.6461` edge `0.1064` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.2888` n `31` status `ready` deltaP `28.1003` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1992` n `31` status `ready` deltaP `24.6101` edge `0.0192` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.9466` n `31` status `ready` deltaP `6.4178` edge `0.2529` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7351` n `31` status `ready` deltaP `8.9627` edge `0.1984` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1325` n `31` status `ready` deltaP `24.6426` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3976` n `31` status `ready` deltaP `9.7413` edge `0.0258` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3531` n `31` status `ready` deltaP `11.5952` edge `0.0237` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3627` n `31` status `ready` deltaP `-2.3614` edge `0.0117` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
