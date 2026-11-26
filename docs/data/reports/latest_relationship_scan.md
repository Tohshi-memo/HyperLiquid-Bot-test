# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T08:37:28.036282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_4h` score `3261.4339` n `31` status `ready` deltaP `3.4815` edge `271.7686` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3233.2717` n `31` status `ready` deltaP `1.6322` edge `269.446` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `102.9798` n `31` status `ready` deltaP `1.6322` edge `8.5802` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `39.2335` n `31` status `ready` deltaP `45.8333` edge `2.9639` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.9973` n `31` status `ready` deltaP `46.7014` edge `2.8551` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.3618` n `31` status `ready` deltaP `46.0069` edge `2.3901` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0192` n `31` status `ready` deltaP `27.675` edge `0.8208` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7136` n `31` status `ready` deltaP `39.0539` edge `0.6805` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.4211` n `31` status `ready` deltaP `32.3813` edge `0.5967` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9478` n `31` status `ready` deltaP `18.7598` edge `0.9074` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.4682` n `31` status `ready` deltaP `47.2222` edge `0.2242` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2666` n `31` status `ready` deltaP `44.8365` edge `0.1528` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7782` n `31` status `ready` deltaP `20.5862` edge `0.1963` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5368` n `31` status `ready` deltaP `37.9869` edge `0.0675` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7453` n `31` status `ready` deltaP `32.4416` edge `0.021` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5031` n `31` status `ready` deltaP `10.1603` edge `0.2993` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.311` n `31` status `ready` deltaP `13.4537` edge `0.2423` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1116` n `31` status `ready` deltaP `26.8096` edge `0.0257` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5259` n `31` status `ready` deltaP `29.7324` edge `0.0253` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1101` n `31` status `ready` deltaP `16.7781` edge `0.0862` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
