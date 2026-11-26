# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T11:52:33.497485+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_1h` score `3233.6749` n `31` status `ready` deltaP `1.6322` edge `269.4796` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3225.5347` n `31` status `ready` deltaP `3.4815` edge `268.777` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `103.383` n `31` status `ready` deltaP `1.6322` edge `8.6138` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `36.0276` n `31` status `ready` deltaP `44.4444` edge `2.706` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.0073` n `31` status `ready` deltaP `43.5764` edge `2.7101` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.2312` n `31` status `ready` deltaP `43.75` edge `2.2276` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.9159` n `31` status `ready` deltaP `27.5226` edge `0.8132` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7492` n `31` status `ready` deltaP `39.6637` edge `0.6794` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.6862` n `31` status `ready` deltaP `30.1244` edge `0.5505` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0259` n `31` status `ready` deltaP `19.8269` edge `0.9103` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9996` n `31` status `ready` deltaP `44.9653` edge `0.2002` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.0344` n `31` status `ready` deltaP `42.5795` edge `0.1485` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8405` n `31` status `ready` deltaP `21.0353` edge `0.1985` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5539` n `31` status `ready` deltaP `38.2917` edge `0.0669` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7884` n `31` status `ready` deltaP `32.8907` edge `0.0216` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5024` n `31` status `ready` deltaP `10.0106` edge `0.3002` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2573` n `31` status `ready` deltaP `12.8549` edge `0.2394` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.985` n `31` status `ready` deltaP `25.4377` edge `0.0243` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4869` n `31` status `ready` deltaP `29.1336` edge `0.0243` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0432` n `31` status `ready` deltaP `16.0159` edge `0.0827` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
