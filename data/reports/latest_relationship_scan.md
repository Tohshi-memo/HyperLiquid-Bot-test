# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T11:07:31.758246+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3247.5193` n `31` status `ready` deltaP `1.6322` edge `270.6333` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3198.9118` n `31` status `ready` deltaP `3.7864` edge `266.5564` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.2582` n `31` status `ready` deltaP `28.4722` edge `1.3317` maxDD `0.0`
- `news_risk_high->equity_24h` score `16.2641` n `31` status `ready` deltaP `27.9514` edge `1.169` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.5051` n `31` status `ready` deltaP `27.6042` edge `0.9414` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.5373` n `31` status `ready` deltaP `20.8153` edge `0.6597` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.4729` n `31` status `ready` deltaP `30.6698` edge `0.383` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.3919` n `31` status `ready` deltaP `13.4244` edge `0.7435` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `4.7057` n `31` status `ready` deltaP `15.8883` edge `0.3137` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->index_24h` score `2.9611` n `31` status `ready` deltaP `29.5139` edge `0.05` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6018` n `31` status `ready` deltaP `30.3649` edge `0.0404` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5345` n `31` status `ready` deltaP `15.9455` edge `0.1236` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3703` n `31` status `ready` deltaP `28.6991` edge `0.0147` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9911` n `31` status `ready` deltaP `6.1184` edge `0.2606` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8161` n `31` status `ready` deltaP `9.5615` edge `0.2048` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1527` n `31` status `ready` deltaP `24.942` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3413` n `31` status `ready` deltaP `11.4427` edge `0.0232` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.038` n `31` status `ready` deltaP `6.9974` edge `-0.002` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5976` n `31` status `ready` deltaP `-4.3075` edge `0.0051` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
