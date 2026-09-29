# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T21:07:36.245145+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7170`

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

- `news_risk_high->unknown_24h` score `2537.866` n `138` status `ready` deltaP `1.9097` edge `211.4761` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.94` n `138` status `ready` deltaP `29.9668` edge `1.4707` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.4572` n `138` status `ready` deltaP `31.318` edge `0.8142` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.9117` n `138` status `ready` deltaP `25.2416` edge `0.889` maxDD `-22.5043`
- `news_risk_high->index_24h` score `4.0288` n `138` status `ready` deltaP `37.349` edge `0.1519` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.5271` n `138` status `ready` deltaP `30.0725` edge `0.269` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `3.0925` n `141` status `ready` deltaP `30.5591` edge `0.2141` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1422` n `141` status `ready` deltaP `11.7421` edge `0.3662` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1154` n `141` status `ready` deltaP `8.8971` edge `0.1247` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7058` n `141` status `ready` deltaP `8.156` edge `0.0704` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.471` n `141` status `ready` deltaP `8.6051` edge `0.0109` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1912` n `141` status `ready` deltaP `10.4491` edge `0.0316` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.24` n `141` status `ready` deltaP `3.3879` edge `0.0749` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5872` n `141` status `ready` deltaP `0.1805` edge `0.0128` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2306` n `141` status `ready` deltaP `-6.5527` edge `0.0345` maxDD `-3.5531`
- `news_risk_high->crypto_major_4h` score `-1.304` n `141` status `ready` deltaP `-2.3233` edge `0.1198` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3083` n `141` status `ready` deltaP `9.0036` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8253` n `141` status `ready` deltaP `-9.0394` edge `-0.0038` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8355` n `141` status `ready` deltaP `-8.826` edge `-0.009` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2764` n `141` status `ready` deltaP `-9.1172` edge `0.0108` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
