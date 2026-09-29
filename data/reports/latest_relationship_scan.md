# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T22:07:34.714736+00:00`
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

- `news_risk_high->unknown_24h` score `2326.4164` n `138` status `ready` deltaP `1.9097` edge `193.8553` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4716` n `138` status `ready` deltaP `29.2723` edge `1.4363` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.2084` n `138` status `ready` deltaP `30.6235` edge `0.7981` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.6115` n `138` status `ready` deltaP `24.8944` edge `0.8663` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.9385` n `138` status `ready` deltaP `36.6545` edge `0.149` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.384` n `138` status `ready` deltaP `29.3781` edge `0.2617` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `3.0271` n `141` status `ready` deltaP `30.1018` edge `0.2117` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1338` n `141` status `ready` deltaP `11.7421` edge `0.3655` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.2173` n `141` status `ready` deltaP `9.4959` edge `0.1292` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.707` n `141` status `ready` deltaP `8.156` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4962` n `141` status `ready` deltaP `8.9045` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1292` n `141` status `ready` deltaP `9.8394` edge `0.0305` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2003` n `141` status `ready` deltaP `3.837` edge `0.077` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.586` n `141` status `ready` deltaP `0.1805` edge `0.0129` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2833` n `141` status `ready` deltaP `-7.1625` edge `0.0318` maxDD `-3.5531`
- `news_risk_high->crypto_major_4h` score `-1.3087` n `141` status `ready` deltaP `-2.3233` edge `0.1192` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3352` n `141` status `ready` deltaP `8.5463` edge `-0.0068` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.7882` n `141` status `ready` deltaP `-8.5903` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8612` n `141` status `ready` deltaP `-9.2751` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2299` n `141` status `ready` deltaP `-8.5074` edge `0.0127` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
