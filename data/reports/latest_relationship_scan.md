# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T04:22:28.644374+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_1h` score `32243.9101` n `45` status `ready` deltaP `2.1656` edge `2686.9875` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21974.3005` n `45` status `ready` deltaP `3.1776` edge `1831.1844` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1008.9551` n `31` status `ready` deltaP `2.3807` edge `84.0813` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `721.353` n `31` status `ready` deltaP `4.3962` edge `60.0891` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.3288` n `31` status `ready` deltaP `44.4444` edge `2.9811` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.0743` n `31` status `ready` deltaP `50.1736` edge `2.9217` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.4912` n `31` status `ready` deltaP `49.3056` edge `2.6289` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.005` n `31` status `ready` deltaP `28.1323` edge `0.8999` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2287` n `31` status `ready` deltaP `41.2355` edge `0.6883` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.6927` n `31` status `ready` deltaP `35.8527` edge `0.7001` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5257` n `31` status `ready` deltaP `18.7598` edge `0.9815` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9686` n `31` status `ready` deltaP `44.0972` edge `0.2034` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3725` n `31` status `ready` deltaP `45.5309` edge `0.157` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7052` n `31` status `ready` deltaP `19.0892` edge `0.2002` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2217` n `31` status `ready` deltaP `34.6332` edge `0.0636` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.733` n `31` status `ready` deltaP `12.2561` edge `0.3148` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.592` n `31` status `ready` deltaP `30.6452` edge `0.0202` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3611` n `31` status `ready` deltaP `12.2561` edge `0.2567` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5898` n `31` status `ready` deltaP `30.1815` edge `0.0305` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
