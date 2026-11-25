# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T15:37:31.229880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32188.3921` n `45` status `ready` deltaP `2.1656` edge `2682.361` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21901.0449` n `45` status `ready` deltaP `2.8727` edge `1825.0818` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `953.4371` n `31` status `ready` deltaP `2.3807` edge `79.4548` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `648.0974` n `31` status `ready` deltaP `4.0913` edge `53.9865` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `451.3343` n `31` status `ready` deltaP `5.7292` edge `37.573` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.4516` n `31` status `ready` deltaP `51.2153` edge `3.4462` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.0498` n `31` status `ready` deltaP `52.7778` edge `3.1523` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.5735` n `31` status `ready` deltaP `55.2083` edge `2.8464` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9609` n `31` status `ready` deltaP `27.3701` edge `0.9013` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.957` n `31` status `ready` deltaP `41.2355` edge `0.749` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.3663` n `31` status `ready` deltaP `37.9869` edge `0.742` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5025` n `31` status `ready` deltaP `18.9123` edge `0.9775` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.2548` n `31` status `ready` deltaP `51.9097` edge `0.2585` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3643` n `31` status `ready` deltaP `45.8782` edge `0.154` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0158` n `31` status `ready` deltaP `20.7359` edge `0.2151` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.445` n `31` status `ready` deltaP `36.6149` edge `0.069` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7082` n `31` status `ready` deltaP `31.8428` edge `0.0219` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6964` n `31` status `ready` deltaP `11.5076` edge `0.3151` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4688` n `45` status `ready` deltaP `30.2405` edge `0.0326` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4546` n `31` status `ready` deltaP `13.304` edge `0.2617` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
