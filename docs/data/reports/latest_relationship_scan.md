# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T12:07:25.897597+00:00`
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

- `market_context_high->unknown_24h` score `3.8077` n `98` status `ready` deltaP `3.8407` edge `0.296` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.457` n `98` status `ready` deltaP `4.4784` edge `0.2084` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.037` n `109` status `ready` deltaP `12.5322` edge `0.0875` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4883` n `98` status `ready` deltaP `20.5321` edge `0.0463` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3376` n `113` status `ready` deltaP `6.9498` edge `0.0234` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1146` n `113` status `ready` deltaP `7.0598` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3213` n `109` status `ready` deltaP `6.5703` edge `0.001` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6156` n `113` status `ready` deltaP `-3.0271` edge `-0.0093` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7469` n `109` status `ready` deltaP `3.2418` edge `0.0061` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.1804` n `113` status `ready` deltaP `-3.9253` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2482` n `98` status `ready` deltaP `-4.0107` edge `0.0862` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3509` n `113` status `ready` deltaP `-3.8723` edge `-0.0157` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7606` n `113` status `ready` deltaP `1.9435` edge `-0.0822` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.8792` n `109` status `ready` deltaP `-10.0764` edge `-0.0483` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.9505` n `109` status `ready` deltaP `2.4516` edge `-0.0399` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.4704` n `98` status `ready` deltaP `-3.0541` edge `-0.0412` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.0417` n `113` status `ready` deltaP `-9.4417` edge `-0.0532` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.7234` n `98` status `ready` deltaP `6.2464` edge `-0.0271` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.9169` n `109` status `ready` deltaP `-1.9663` edge `-0.3448` maxDD `-34.9766`
- `market_context_high->crypto_major_24h` score `-7.6166` n `98` status `ready` deltaP `-7.4653` edge `-0.2536` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
