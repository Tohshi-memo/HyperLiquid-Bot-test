# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T05:37:25.811591+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3983`

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

- `news_risk_high->unknown_1h` score `3222.5185` n `31` status `ready` deltaP `1.6322` edge `268.5499` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3201.5815` n `31` status `ready` deltaP `3.4815` edge `266.7809` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `92.2266` n `31` status `ready` deltaP `1.6322` edge `7.6841` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `41.7125` n `31` status `ready` deltaP `47.9167` edge `3.1566` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.4984` n `31` status `ready` deltaP `48.7847` edge `2.9663` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.9852` n `31` status `ready` deltaP `48.0903` edge `2.5115` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7691` n `31` status `ready` deltaP `26.3031` edge `0.8091` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2927` n `31` status `ready` deltaP `37.3771` edge `0.6566` maxDD `-2.178`
- `news_risk_high->metal_24h` score `10.1374` n `31` status `ready` deltaP `34.4646` edge `0.6425` maxDD `-0.1986`
- `news_risk_high->index_24h` score `6.8352` n `31` status `ready` deltaP `49.3056` edge `0.2409` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7749` n `31` status `ready` deltaP `17.2354` edge `0.8954` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6031` n `31` status `ready` deltaP `19.8377` edge `0.1867` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3558` n `31` status `ready` deltaP `36.31` edge `0.0636` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6459` n `31` status `ready` deltaP `31.3937` edge `0.0197` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4345` n `31` status `ready` deltaP `9.7112` edge `0.2935` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.237` n `31` status `ready` deltaP `12.7052` edge `0.2378` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0752` n `31` status `ready` deltaP `26.5048` edge `0.0247` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.49` n `31` status `ready` deltaP `29.2833` edge `0.0237` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1008` n `31` status `ready` deltaP `16.7781` edge `0.085` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
