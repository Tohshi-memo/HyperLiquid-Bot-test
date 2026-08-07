# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T03:52:23.531007+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->commodity_4h` score `1.1999` n `120` status `ready` deltaP `13.6382` edge `0.0937` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.856` n `109` status `ready` deltaP `3.7004` edge `0.1635` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5761` n `109` status `ready` deltaP `21.4854` edge `0.0512` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4931` n `120` status `ready` deltaP `7.9491` edge `0.0297` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0234` n `120` status `ready` deltaP `6.3024` edge `-0.004` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2811` n `120` status `ready` deltaP `7.1341` edge `0.0024` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5389` n `120` status `ready` deltaP `-1.9261` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7747` n `120` status `ready` deltaP `-2.994` edge `-0.0083` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9545` n `120` status `ready` deltaP `-1.9261` edge `-0.0133` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1009` n `109` status `ready` deltaP `-0.8792` edge `0.0842` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2766` n `120` status `ready` deltaP `4.2465` edge `-0.0355` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.4298` n `120` status `ready` deltaP `0.1829` edge `0.0031` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.5336` n `120` status `ready` deltaP `-5.996` edge `-0.0312` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8708` n `120` status `ready` deltaP `2.1138` edge `-0.031` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.571` n `120` status `ready` deltaP `-6.3024` edge `-0.0349` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.5387` n `109` status `ready` deltaP `-8.8174` edge `-0.0918` maxDD `-4.5445`
- `market_context_high->unknown_24h` score `-3.8922` n `109` status `ready` deltaP `3.7571` edge `-0.3451` maxDD `-0.0104`
- `market_context_high->equity_4h` score `-5.8181` n `120` status `ready` deltaP `0.9553` edge `-0.2234` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3337` n `109` status `ready` deltaP `9.8099` edge `-0.0009` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.1833` n `120` status `ready` deltaP `-5.7317` edge `-0.1392` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
