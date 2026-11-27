# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T02:07:26.133853+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3209.2416` n `31` status `ready` deltaP `1.7819` edge `267.4425` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3174.243` n `31` status `ready` deltaP `4.3962` edge `264.4966` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.9678` n `31` status `ready` deltaP `34.7222` edge `1.9325` maxDD `0.0`
- `news_risk_high->equity_24h` score `23.1097` n `31` status `ready` deltaP `34.2014` edge `1.6978` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.8935` n `31` status `ready` deltaP `33.8542` edge `1.4321` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4746` n `31` status `ready` deltaP `23.7116` edge `0.7185` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.1374` n `31` status `ready` deltaP `34.4808` edge `0.4963` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2333` n `31` status `ready` deltaP `16.9305` edge `0.828` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.13` n `31` status `ready` deltaP `21.6174` edge `0.3942` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.9429` n `31` status `ready` deltaP `41.8851` edge `0.1455` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.0911` n `31` status `ready` deltaP `35.7639` edge `0.1025` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.9471` n `31` status `ready` deltaP `17.5922` edge `0.147` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.8709` n `31` status `ready` deltaP `32.499` edge `0.0486` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5212` n `31` status `ready` deltaP `30.3458` edge `0.0163` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.175` n `31` status `ready` deltaP `7.316` edge `0.2762` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9369` n `31` status `ready` deltaP `10.31` edge `0.2153` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2587` n `31` status `ready` deltaP `26.439` edge `0.013` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5629` n `31` status `ready` deltaP `12.5098` edge `0.0445` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.161` n `31` status `ready` deltaP `8.5218` edge `0.0036` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5401` n `31` status `ready` deltaP `-3.7087` edge `0.0059` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
