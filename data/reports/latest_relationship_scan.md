# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T09:37:29.953265+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4152`

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

- `market_context_high->unknown_1h` score `32228.8957` n `45` status `ready` deltaP `2.1656` edge `2685.7363` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21966.4153` n `45` status `ready` deltaP `3.1776` edge `1830.5273` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `993.9407` n `31` status `ready` deltaP `2.3807` edge `82.8301` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `721.4831` n `31` status `ready` deltaP `5.7292` edge `60.0854` maxDD `0.0`
- `news_risk_high->unknown_4h` score `713.4678` n `31` status `ready` deltaP `4.3962` edge `59.432` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `41.9743` n `31` status `ready` deltaP `47.0486` edge `3.1842` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.1735` n `31` status `ready` deltaP `50.1736` edge `3.0133` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.9846` n `31` status `ready` deltaP `51.5625` edge `2.7383` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8061` n `31` status `ready` deltaP `27.3701` edge `0.8884` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.5191` n `31` status `ready` deltaP `41.2355` edge `0.7125` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2699` n `31` status `ready` deltaP `37.682` edge `0.736` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5657` n `31` status `ready` deltaP `18.9123` edge `0.9856` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.5458` n `31` status `ready` deltaP `47.7431` edge `0.2272` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1169` n `31` status `ready` deltaP `43.1004` edge `0.1519` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0313` n `31` status `ready` deltaP `21.0353` edge `0.2144` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.382` n `31` status `ready` deltaP `36.1576` edge `0.0668` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7798` n `31` status `ready` deltaP `12.2561` edge `0.3208` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7046` n `31` status `ready` deltaP `31.8428` edge `0.0216` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6528` n `45` status `ready` deltaP `32.3746` edge `0.0337` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4117` n `31` status `ready` deltaP `12.8549` edge `0.2592` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
