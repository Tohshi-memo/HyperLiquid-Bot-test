# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T07:52:29.526662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4116`

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

- `market_context_high->unknown_1h` score `32237.7913` n `45` status `ready` deltaP `2.1656` edge `2686.4776` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21981.4957` n `45` status `ready` deltaP `3.1776` edge `1831.784` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1002.8363` n `31` status `ready` deltaP `2.3807` edge `83.5714` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `823.2851` n `31` status `ready` deltaP `5.7292` edge `68.5689` maxDD `0.0`
- `news_risk_high->unknown_4h` score `728.5482` n `31` status `ready` deltaP `4.3962` edge `60.6887` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `41.0851` n `31` status `ready` deltaP `45.8333` edge `3.1182` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.8339` n `31` status `ready` deltaP `50.1736` edge `2.985` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.5365` n `31` status `ready` deltaP `50.5208` edge `2.7079` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8834` n `31` status `ready` deltaP `27.8275` edge `0.8918` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.411` n `31` status `ready` deltaP `41.2355` edge `0.7035` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2087` n `31` status `ready` deltaP `37.682` edge `0.7309` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5805` n `31` status `ready` deltaP `18.9123` edge `0.9875` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.3574` n `31` status `ready` deltaP `46.5278` edge `0.2196` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1205` n `31` status `ready` deltaP `43.1004` edge `0.1522` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9702` n `31` status `ready` deltaP `20.5862` edge `0.2123` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3796` n `31` status `ready` deltaP `36.1576` edge `0.0666` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7954` n `31` status `ready` deltaP `12.5555` edge `0.3208` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6902` n `31` status `ready` deltaP `31.6931` edge `0.0214` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4031` n `31` status `ready` deltaP `12.7052` edge `0.2591` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
