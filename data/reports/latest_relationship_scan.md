# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T13:07:29.603453+00:00`
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

- `market_context_high->unknown_1h` score `32208.1729` n `45` status `ready` deltaP `2.0159` edge `2684.0104` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21942.8005` n `45` status `ready` deltaP `3.1776` edge `1828.5594` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `973.218` n `31` status `ready` deltaP `2.231` edge `81.1042` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `689.853` n `31` status `ready` deltaP `4.3962` edge `57.4641` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `578.2931` n `31` status `ready` deltaP `5.7292` edge `48.1529` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.8331` n `31` status `ready` deltaP `49.4792` edge `3.3229` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.0757` n `31` status `ready` deltaP `51.0417` edge `3.0827` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.8521` n `31` status `ready` deltaP `53.6458` edge `2.7967` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8289` n `31` status `ready` deltaP `27.3701` edge `0.8903` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.747` n `31` status `ready` deltaP `41.2355` edge `0.7315` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1691` n `31` status `ready` deltaP `37.682` edge `0.7276` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4643` n `31` status `ready` deltaP `18.9123` edge `0.9726` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.9491` n `31` status `ready` deltaP `50.1736` edge `0.2446` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2261` n `31` status `ready` deltaP `44.3157` edge `0.1529` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0301` n `31` status `ready` deltaP `20.8856` edge `0.2153` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3844` n `31` status `ready` deltaP `36.1576` edge `0.067` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7479` n `31` status `ready` deltaP `11.807` edge `0.3197` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7333` n `31` status `ready` deltaP `32.1422` edge `0.022` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5614` n `45` status `ready` deltaP `31.3076` edge `0.0332` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4935` n `31` status `ready` deltaP `13.6034` edge `0.2647` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
