# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T22:22:32.699542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `2274.028` n `138` status `ready` deltaP `1.9097` edge `189.4896` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3509` n `138` status `ready` deltaP `29.0987` edge `1.4274` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.1453` n `138` status `ready` deltaP `30.4499` edge `0.794` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.5268` n `138` status `ready` deltaP `24.7207` edge `0.8604` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.915` n `138` status `ready` deltaP `36.4809` edge `0.1482` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.3473` n `138` status `ready` deltaP `29.2044` edge `0.2598` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `3.0041` n `141` status `ready` deltaP `29.9494` edge `0.2108` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.147` n `141` status `ready` deltaP `11.7421` edge `0.3666` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.2545` n `141` status `ready` deltaP `9.6456` edge `0.1313` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.707` n `141` status `ready` deltaP `8.156` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.495` n `141` status `ready` deltaP `8.9045` edge `0.0109` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1134` n `141` status `ready` deltaP `9.6869` edge `0.0302` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1956` n `141` status `ready` deltaP `3.837` edge `0.0776` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.586` n `141` status `ready` deltaP `0.1805` edge `0.0129` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2959` n `141` status `ready` deltaP `-7.3149` edge `0.0312` maxDD `-3.5531`
- `news_risk_high->crypto_major_4h` score `-1.304` n `141` status `ready` deltaP `-2.3233` edge `0.1198` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3439` n `141` status `ready` deltaP `8.3939` edge `-0.0069` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8001` n `141` status `ready` deltaP `-8.74` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8526` n `141` status `ready` deltaP `-9.1254` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2204` n `141` status `ready` deltaP `-8.355` edge `0.0129` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
