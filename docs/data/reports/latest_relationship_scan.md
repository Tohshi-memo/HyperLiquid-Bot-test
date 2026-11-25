# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T16:37:32.551962+00:00`
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

- `market_context_high->unknown_1h` score `32183.8753` n `45` status `ready` deltaP `2.1656` edge `2681.9846` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21880.7589` n `45` status `ready` deltaP `2.8727` edge `1823.3913` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `948.9203` n `31` status `ready` deltaP `2.3807` edge `79.0784` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `627.8114` n `31` status `ready` deltaP `4.0913` edge `52.296` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `398.6003` n `31` status `ready` deltaP `5.7292` edge `33.1785` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.022` n `31` status `ready` deltaP `51.9097` edge `3.4891` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.3274` n `31` status `ready` deltaP `53.4722` edge `3.1708` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.761` n `31` status `ready` deltaP `55.9028` edge `2.8574` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0356` n `31` status `ready` deltaP `27.675` edge `0.9055` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `12.0134` n `31` status `ready` deltaP `41.2355` edge `0.7537` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.5708` n `31` status `ready` deltaP `38.4442` edge `0.756` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5268` n `31` status `ready` deltaP `19.0647` edge `0.9796` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.3679` n `31` status `ready` deltaP `52.6042` edge `0.2633` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4283` n `31` status `ready` deltaP `46.5726` edge `0.1547` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0686` n `31` status `ready` deltaP `20.7359` edge `0.2195` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5118` n `31` status `ready` deltaP `37.2247` edge `0.0705` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7405` n `31` status `ready` deltaP `32.1422` edge `0.0226` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.673` n `31` status `ready` deltaP `11.3579` edge `0.3131` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4688` n `45` status `ready` deltaP `30.2405` edge `0.0326` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4491` n `31` status `ready` deltaP `13.304` edge `0.261` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
