# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T12:37:29.471934+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5552`

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

- `news_risk_high->unknown_1h` score `3400.2828` n `31` status `ready` deltaP `2.0813` edge `283.3606` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3256.9486` n `31` status `ready` deltaP `3.7864` edge `271.3928` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.634` n `31` status `ready` deltaP `35.3553` edge `1.7338` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.3452` n `31` status `ready` deltaP `33.2756` edge `1.2236` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.7809` n `31` status `ready` deltaP `28.0763` edge `0.8779` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.0758` n `31` status `ready` deltaP `23.4067` edge `0.6873` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.7784` n `31` status `ready` deltaP `17.6927` edge `0.7646` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.6709` n `31` status `ready` deltaP `31.2795` edge `0.3121` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0328` n `31` status `ready` deltaP `41.4491` edge `0.1559` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9849` n `31` status `ready` deltaP `17.2137` edge `0.2448` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.55` n `31` status `ready` deltaP `31.1271` edge `0.031` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4068` n `31` status `ready` deltaP `26.1698` edge `0.0261` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3391` n `31` status `ready` deltaP `28.6991` edge `0.0121` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1748` n `31` status `ready` deltaP `14.4485` edge `0.1036` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0152` n `31` status `ready` deltaP `7.0166` edge `0.2577` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8247` n `31` status `ready` deltaP `9.8609` edge `0.2039` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1169` n `31` status `ready` deltaP `24.3432` edge `0.0088` maxDD `-0.2315`
- `market_context_high->metal_4h` score `1.0974` n `43` status `ready` deltaP `15.2687` edge `0.0308` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4576` n `31` status `ready` deltaP `10.656` edge `0.0274` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.449` n `55` status `ready` deltaP `11.5188` edge `0.0022` maxDD `-0.0471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
