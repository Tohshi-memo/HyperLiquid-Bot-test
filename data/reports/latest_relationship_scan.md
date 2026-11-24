# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T16:52:26.686005+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4272`

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

- `market_context_high->unknown_1h` score `32296.3778` n `45` status `ready` deltaP `1.7165` edge `2691.3628` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22107.9703` n `45` status `ready` deltaP `2.7202` edge `1842.3266` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1061.4228` n `31` status `ready` deltaP `1.9316` edge `88.4566` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `855.0228` n `31` status `ready` deltaP `3.9388` edge `71.2313` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.5115` n `31` status `ready` deltaP `49.4792` edge `2.7961` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.3912` n `31` status `ready` deltaP `41.3194` edge `2.6738` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6899` n `31` status `ready` deltaP `47.0486` edge `2.4105` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.1461` n `31` status `ready` deltaP `24.6262` edge `0.8517` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.0978` n `31` status `ready` deltaP `41.2355` edge `0.6774` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.476` n `31` status `ready` deltaP `33.1088` edge `0.617` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.8978` n `31` status `ready` deltaP `15.8635` edge `0.9203` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.3654` n `31` status `ready` deltaP `53.517` edge `0.1865` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.237` n `31` status `ready` deltaP `39.0625` edge `0.176` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5732` n `31` status `ready` deltaP `19.0892` edge `0.1892` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9497` n `31` status `ready` deltaP `32.1942` edge `0.0572` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8999` n `45` status `ready` deltaP `35.1185` edge `0.036` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6418` n `31` status `ready` deltaP `11.9567` edge `0.3051` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5824` n `31` status `ready` deltaP `30.6452` edge `0.0194` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2933` n `31` status `ready` deltaP `11.5076` edge `0.253` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6708` n `31` status `ready` deltaP `31.2294` edge `0.0339` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
