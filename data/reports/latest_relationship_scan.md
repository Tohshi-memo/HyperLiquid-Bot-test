# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T11:52:29.162744+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `6.1489` n `98` status `ready` deltaP `3.8407` edge `0.4911` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.4757` n `98` status `ready` deltaP `4.652` edge `0.2088` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.02` n `109` status `ready` deltaP `12.3798` edge `0.0871` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4891` n `98` status `ready` deltaP `20.5321` edge `0.0464` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3232` n `113` status `ready` deltaP `6.8001` edge `0.0232` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1134` n `113` status `ready` deltaP `7.0598` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.319` n `109` status `ready` deltaP `6.5703` edge `0.0013` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6149` n `113` status `ready` deltaP `-3.0271` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7493` n `109` status `ready` deltaP `3.2418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.1816` n `113` status `ready` deltaP `-3.9253` edge `-0.0189` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2752` n `98` status `ready` deltaP `-4.1844` edge `0.0839` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3317` n `113` status `ready` deltaP `-3.7226` edge `-0.0151` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7653` n `113` status `ready` deltaP `1.9435` edge `-0.0828` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.8918` n `109` status `ready` deltaP `-10.2288` edge `-0.0489` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.9687` n `109` status `ready` deltaP `2.2991` edge `-0.0404` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.4421` n `98` status `ready` deltaP `-2.8805` edge `-0.04` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.0262` n `113` status `ready` deltaP `-9.292` edge `-0.0529` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.741` n `98` status `ready` deltaP `6.0728` edge `-0.0282` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.9685` n `109` status `ready` deltaP `-2.1187` edge `-0.3504` maxDD `-34.9766`
- `market_context_high->crypto_major_24h` score `-7.6174` n `98` status `ready` deltaP `-7.4653` edge `-0.2537` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
