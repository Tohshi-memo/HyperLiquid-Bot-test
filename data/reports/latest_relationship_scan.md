# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T22:52:30.563677+00:00`
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

- `news_risk_high->unknown_24h` score `2169.2668` n `138` status `ready` deltaP `1.9097` edge `180.7595` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.1083` n `138` status `ready` deltaP `28.7515` edge `1.4095` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.0203` n `138` status `ready` deltaP `30.1027` edge `0.7859` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.3622` n `138` status `ready` deltaP `24.3735` edge `0.849` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.868` n `138` status `ready` deltaP `36.1337` edge `0.1466` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.2751` n `138` status `ready` deltaP `28.8572` edge `0.2561` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.9605` n `141` status `ready` deltaP `29.6445` edge `0.2092` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.199` n `141` status `ready` deltaP `12.047` edge `0.3689` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3025` n `141` status `ready` deltaP `9.945` edge `0.1333` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.707` n `141` status `ready` deltaP `8.156` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4938` n `141` status `ready` deltaP `8.9045` edge `0.0108` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.083` n `141` status `ready` deltaP `9.3821` edge `0.0297` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2159` n `141` status `ready` deltaP `3.5376` edge `0.077` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.586` n `141` status `ready` deltaP `0.1805` edge `0.0129` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2836` n `141` status `ready` deltaP `-2.1709` edge `0.1214` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3204` n `141` status `ready` deltaP `-7.6198` edge `0.0301` maxDD `-3.5531`
- `news_risk_high->fx_4h` score `-1.3613` n `141` status `ready` deltaP `8.089` edge `-0.0071` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8253` n `141` status `ready` deltaP `-9.0394` edge `-0.0038` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8612` n `141` status `ready` deltaP `-9.2751` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2204` n `141` status `ready` deltaP `-8.355` edge `0.0129` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
