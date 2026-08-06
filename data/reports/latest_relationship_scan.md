# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T10:52:27.609500+00:00`
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

- `market_context_high->unknown_24h` score `15.5341` n `98` status `ready` deltaP `3.8407` edge `1.2732` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.5136` n `98` status `ready` deltaP `4.8256` edge `0.2108` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0056` n `109` status `ready` deltaP `12.3798` edge `0.0859` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.502` n `98` status `ready` deltaP `20.7057` edge `0.0469` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3556` n `109` status `ready` deltaP `7.1609` edge `0.0235` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0027` n `109` status `ready` deltaP `5.6831` edge `-0.0031` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2994` n `109` status `ready` deltaP `6.7227` edge `0.0028` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5152` n `109` status `ready` deltaP `-1.4105` edge `-0.0072` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6957` n `109` status `ready` deltaP `-2.6081` edge `-0.0184` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7493` n `109` status `ready` deltaP `3.2418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3908` n `98` status `ready` deltaP `-4.8788` edge `0.0737` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4642` n `109` status `ready` deltaP `-4.8385` edge `-0.0187` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7102` n `109` status `ready` deltaP `2.0176` edge `-0.0804` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.9469` n `109` status `ready` deltaP `-10.8386` edge `-0.0519` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.0727` n `109` status `ready` deltaP `1.6894` edge `-0.045` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.3777` n `98` status `ready` deltaP `-2.3597` edge `-0.0381` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.1904` n `109` status `ready` deltaP `-10.7002` edge `-0.0572` maxDD `-7.6533`
- `market_context_high->unknown_4h` score `-3.5641` n `109` status `ready` deltaP `-0.7356` edge `-0.1925` maxDD `-3.6349`
- `market_context_high->commodity_24h` score `-6.8028` n `98` status `ready` deltaP `5.3784` edge `-0.0315` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-7.1999` n `109` status `ready` deltaP `-2.7285` edge `-0.376` maxDD `-34.9766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
