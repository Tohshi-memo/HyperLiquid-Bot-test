# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T10:37:33.170017+00:00`
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

- `market_context_high->unknown_24h` score `17.8633` n `98` status `ready` deltaP `3.8407` edge `1.4673` maxDD `-0.0103`
- `market_context_high->metal_24h` score `1.5244` n `98` status `ready` deltaP `4.8256` edge `0.2117` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0056` n `109` status `ready` deltaP `12.3798` edge `0.0859` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.5028` n `98` status `ready` deltaP `20.7057` edge `0.047` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3724` n `109` status `ready` deltaP `7.3106` edge `0.0239` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0027` n `109` status `ready` deltaP `5.6831` edge `-0.0031` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2962` n `109` status `ready` deltaP `6.7227` edge `0.0032` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5152` n `109` status `ready` deltaP `-1.4105` edge `-0.0072` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.705` n `109` status `ready` deltaP `-2.7578` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7485` n `109` status `ready` deltaP `3.2418` edge `0.0059` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.4194` n `98` status `ready` deltaP `-5.0524` edge `0.0712` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4642` n `109` status `ready` deltaP `-4.8385` edge `-0.0187` maxDD `-3.0178`
- `market_context_high->unknown_4h` score `-1.5846` n `109` status `ready` deltaP `-0.7356` edge `-0.0276` maxDD `-3.6303`
- `market_context_high->equity_1h` score `-1.7434` n `109` status `ready` deltaP `1.8679` edge `-0.0824` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9618` n `109` status `ready` deltaP `-10.991` edge `-0.0528` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.0993` n `109` status `ready` deltaP `1.5369` edge `-0.0462` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.3566` n `98` status `ready` deltaP `-2.1861` edge `-0.0375` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.1904` n `109` status `ready` deltaP `-10.7002` edge `-0.0572` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.8165` n `98` status `ready` deltaP `5.2048` edge `-0.0321` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-7.3311` n `109` status `ready` deltaP `-2.8809` edge `-0.3876` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
