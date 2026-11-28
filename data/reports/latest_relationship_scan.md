# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T16:52:27.413890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7444`

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

- `news_risk_high->unknown_1h` score `3438.4679` n `31` status `ready` deltaP `2.3807` edge `286.5407` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3268.8213` n `31` status `ready` deltaP `3.634` edge `272.3832` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.9851` n `31` status `ready` deltaP `38.1282` edge `1.8279` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0053` n `31` status `ready` deltaP `36.2218` edge `1.3423` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0964` n `31` status `ready` deltaP `29.2894` edge `0.8961` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4287` n `31` status `ready` deltaP `24.4738` edge `0.7096` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9838` n `31` status `ready` deltaP `18.9123` edge `0.7828` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.9798` n `31` status `ready` deltaP `33.5661` edge `0.3226` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.1364` n `31` status `ready` deltaP `42.489` edge `0.1576` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9242` n `31` status `ready` deltaP `17.0403` edge `0.2409` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6949` n `31` status `ready` deltaP `32.8039` edge `0.0319` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4844` n `31` status `ready` deltaP `26.6898` edge `0.0291` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3798` n `31` status `ready` deltaP `29.1482` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3186` n `31` status `ready` deltaP `15.4964` edge `0.1086` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0994` n `31` status `ready` deltaP `7.1663` edge `0.2675` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9938` n `31` status `ready` deltaP `11.0585` edge `0.2176` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5209` n `31` status `ready` deltaP `11.723` edge `0.0284` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.459` n `31` status `ready` deltaP `13.272` edge `0.0261` maxDD `-0.7918`
- `market_context_high->fx_1h` score `0.4328` n `65` status `ready` deltaP `11.3888` edge `0.0017` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
