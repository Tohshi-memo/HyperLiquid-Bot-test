# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T22:37:29.642948+00:00`
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

- `news_risk_high->unknown_24h` score `2221.642` n `138` status `ready` deltaP `1.9097` edge `185.1241` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.2278` n `138` status `ready` deltaP `28.9251` edge `1.4183` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.0822` n `138` status `ready` deltaP `30.2763` edge `0.7899` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.4421` n `138` status `ready` deltaP `24.5471` edge `0.8545` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.8915` n `138` status `ready` deltaP `36.3073` edge `0.1474` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.3118` n `138` status `ready` deltaP `29.0308` edge `0.258` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.9799` n `141` status `ready` deltaP `29.7969` edge `0.2098` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1712` n `141` status `ready` deltaP `11.8945` edge `0.3676` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.2785` n `141` status `ready` deltaP `9.7953` edge `0.1323` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7058` n `141` status `ready` deltaP `8.156` edge `0.0704` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4938` n `141` status `ready` deltaP `8.9045` edge `0.0108` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0976` n `141` status `ready` deltaP `9.5345` edge `0.0299` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2057` n `141` status `ready` deltaP `3.6873` edge `0.0773` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.586` n `141` status `ready` deltaP `0.1805` edge `0.0129` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2977` n `141` status `ready` deltaP `-2.3233` edge `0.1206` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3078` n `141` status `ready` deltaP `-7.4674` edge `0.0307` maxDD `-3.5531`
- `news_risk_high->fx_4h` score `-1.3526` n `141` status `ready` deltaP `8.2414` edge `-0.007` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8121` n `141` status `ready` deltaP `-8.8897` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8604` n `141` status `ready` deltaP `-9.2751` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2204` n `141` status `ready` deltaP `-8.355` edge `0.0129` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
