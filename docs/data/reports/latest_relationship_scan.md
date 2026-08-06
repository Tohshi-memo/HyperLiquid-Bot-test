# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T03:07:39.879573+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.4504` n `90` status `ready` deltaP `4.4445` edge `1.0122` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.897` n `109` status `ready` deltaP `-1.6503` edge `0.4353` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2396` n `109` status `ready` deltaP `14.209` edge `0.0932` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7745` n `90` status `ready` deltaP `2.0139` edge `0.2027` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7465` n `90` status `ready` deltaP `24.0278` edge `0.0561` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4083` n `109` status `ready` deltaP `7.7597` edge `0.0239` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0452` n `109` status `ready` deltaP `6.1322` edge `-0.0021` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1399` n `109` status `ready` deltaP `9.0093` edge `0.008` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5682` n `109` status `ready` deltaP `-2.159` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7424` n `109` status `ready` deltaP `-3.3566` edge `-0.0194` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.961` n `109` status `ready` deltaP `0.9552` edge `-0.0061` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2725` n `90` status `ready` deltaP `0.7291` edge `-0.0237` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4186` n `109` status `ready` deltaP `-4.5391` edge `-0.0169` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.667` n `90` status `ready` deltaP `-5.0` edge `0.0391` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8432` n `109` status `ready` deltaP `1.1194` edge `-0.0902` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1643` n `109` status `ready` deltaP `-13.43` edge `-0.0625` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1673` n `109` status `ready` deltaP `0.9272` edge `-0.0478` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.2599` n `109` status `ready` deltaP `-11.1493` edge `-0.06` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.2741` n `109` status `ready` deltaP `2.0326` edge `-0.2417` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.1306` n `90` status `ready` deltaP `9.7917` edge `-0.0298` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
