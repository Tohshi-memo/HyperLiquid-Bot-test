# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T21:37:31.301238+00:00`
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

- `news_risk_high->unknown_24h` score `2433.106` n `138` status `ready` deltaP `1.9097` edge `202.7461` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.713` n `138` status `ready` deltaP `29.6196` edge `1.4541` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.3334` n `138` status `ready` deltaP `30.9707` edge `0.8062` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.7797` n `138` status `ready` deltaP `25.2416` edge `0.878` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.9831` n `138` status `ready` deltaP `37.0018` edge `0.1504` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.4549` n `138` status `ready` deltaP `29.7253` edge `0.2653` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `3.0707` n `141` status `ready` deltaP `30.4067` edge `0.2133` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1518` n `141` status `ready` deltaP `11.7421` edge `0.367` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1562` n `141` status `ready` deltaP `9.1965` edge `0.1261` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.707` n `141` status `ready` deltaP `8.156` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4842` n `141` status `ready` deltaP `8.7548` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1608` n `141` status `ready` deltaP `10.1443` edge `0.0311` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.219` n `141` status `ready` deltaP `3.6873` edge `0.0756` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5872` n `141` status `ready` deltaP `0.1805` edge `0.0128` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2566` n `141` status `ready` deltaP `-6.8576` edge `0.0332` maxDD `-3.5531`
- `news_risk_high->crypto_major_4h` score `-1.3001` n `141` status `ready` deltaP `-2.3233` edge `0.1203` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3178` n `141` status `ready` deltaP `8.8512` edge `-0.0066` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8001` n `141` status `ready` deltaP `-8.74` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8534` n `141` status `ready` deltaP `-9.1254` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.252` n `141` status `ready` deltaP `-8.8123` edge `0.0119` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
