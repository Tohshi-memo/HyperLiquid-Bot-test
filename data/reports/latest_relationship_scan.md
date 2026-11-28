# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T17:52:28.487699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7510`

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

- `news_risk_high->unknown_1h` score `3439.3632` n `31` status `ready` deltaP `2.231` edge `286.6163` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3272.1463` n `31` status `ready` deltaP `3.4815` edge `272.6613` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.2133` n `31` status `ready` deltaP `38.8215` edge `1.8423` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3764` n `31` status `ready` deltaP `36.9151` edge `1.3686` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1492` n `31` status `ready` deltaP `29.2894` edge `0.9005` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5011` n `31` status `ready` deltaP `24.7787` edge `0.7136` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.021` n `31` status `ready` deltaP `33.871` edge `0.324` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9893` n `31` status `ready` deltaP `18.9123` edge `0.7835` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.1792` n `31` status `ready` deltaP `43.0089` edge `0.1577` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9098` n `31` status `ready` deltaP `17.0403` edge `0.2397` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7351` n `31` status `ready` deltaP `33.2612` edge `0.0322` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4964` n `31` status `ready` deltaP `26.6898` edge `0.0301` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3774` n `31` status `ready` deltaP `29.1482` edge `0.0123` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3066` n `31` status `ready` deltaP `15.3467` edge `0.1086` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0994` n `31` status `ready` deltaP `7.1663` edge `0.2675` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0063` n `31` status `ready` deltaP `11.2082` edge `0.2182` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5581` n `31` status `ready` deltaP `12.3328` edge `0.0291` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.5109` n `64` status `ready` deltaP `10.8994` edge `0.0095` maxDD `-0.1673`
- `news_risk_high->metal_4h` score `0.4844` n `31` status `ready` deltaP `13.7293` edge `0.0263` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
