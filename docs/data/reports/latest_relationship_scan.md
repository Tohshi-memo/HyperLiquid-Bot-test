# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T04:07:28.166139+00:00`
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

- `market_context_high->unknown_24h` score `12.3796` n `90` status `ready` deltaP `4.4445` edge `1.0063` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0656` n `109` status `ready` deltaP `-1.1929` edge `0.4463` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.26` n `109` status `ready` deltaP `14.209` edge `0.0949` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7713` n `90` status `ready` deltaP `2.0139` edge `0.2023` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7199` n `90` status `ready` deltaP `23.6806` edge `0.055` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4551` n `109` status `ready` deltaP `8.2088` edge `0.0248` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0188` n `109` status `ready` deltaP `5.8328` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1422` n `109` status `ready` deltaP `9.0093` edge `0.0077` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.565` n `109` status `ready` deltaP `-2.159` edge `-0.0086` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7268` n `109` status `ready` deltaP `-3.0572` edge `-0.0194` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9815` n `109` status `ready` deltaP `0.6504` edge `-0.0067` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3137` n `90` status `ready` deltaP `0.2083` edge `-0.0255` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4893` n `109` status `ready` deltaP `-5.1379` edge `-0.0188` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.5537` n `90` status `ready` deltaP `-4.3056` edge `0.049` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8494` n `109` status `ready` deltaP `1.1194` edge `-0.091` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.1443` n `109` status `ready` deltaP `1.0796` edge `-0.0469` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1635` n `109` status `ready` deltaP `-13.43` edge `-0.0624` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.237` n `109` status `ready` deltaP `2.332` edge `-0.2406` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3163` n `109` status `ready` deltaP `-11.5984` edge `-0.0617` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1784` n `90` status `ready` deltaP `9.0973` edge `-0.0313` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
