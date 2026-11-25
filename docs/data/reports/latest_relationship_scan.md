# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T11:52:27.583972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3780`

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

- `market_context_high->unknown_1h` score `32219.3257` n `45` status `ready` deltaP `2.0159` edge `2684.9398` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21959.1289` n `45` status `ready` deltaP `3.1776` edge `1829.9201` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `984.3708` n `31` status `ready` deltaP `2.231` edge `82.0336` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `706.1814` n `31` status `ready` deltaP `4.3962` edge `58.8248` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `630.5603` n `31` status `ready` deltaP `5.7292` edge `52.5085` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.1085` n `31` status `ready` deltaP `48.6111` edge `3.2683` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.6837` n `31` status `ready` deltaP `50.5208` edge `3.0535` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.5253` n `31` status `ready` deltaP `52.9514` edge `2.7741` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8469` n `31` status `ready` deltaP `27.3701` edge `0.8918` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.6582` n `31` status `ready` deltaP `41.2355` edge `0.7241` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2159` n `31` status `ready` deltaP `37.682` edge `0.7315` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5438` n `31` status `ready` deltaP `18.9123` edge `0.9828` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.7992` n `31` status `ready` deltaP `49.3056` edge `0.2379` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1658` n `31` status `ready` deltaP `43.6212` edge `0.1525` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0086` n `31` status `ready` deltaP `20.7359` edge `0.2145` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3808` n `31` status `ready` deltaP `36.1576` edge `0.0667` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7627` n `31` status `ready` deltaP `11.9567` edge `0.3206` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.9925` edge `0.0219` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6016` n `45` status `ready` deltaP `31.7649` edge `0.0335` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4624` n `31` status `ready` deltaP `13.304` edge `0.2627` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
