# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T04:37:25.070010+00:00`
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

- `market_context_high->commodity_4h` score `1.1441` n `120` status `ready` deltaP `13.1809` edge `0.0921` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8174` n `109` status `ready` deltaP `3.5334` edge `0.1614` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5792` n `109` status `ready` deltaP `21.4854` edge `0.0516` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4524` n `120` status `ready` deltaP `7.5` edge `0.0293` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0398` n `120` status `ready` deltaP `6.6018` edge `-0.0039` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2495` n `120` status `ready` deltaP `7.5915` edge `0.0034` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.556` n `120` status `ready` deltaP `-2.2255` edge `-0.007` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7482` n `120` status `ready` deltaP `-2.6946` edge `-0.0069` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9665` n `120` status `ready` deltaP `-2.0758` edge `-0.0133` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0868` n `109` status `ready` deltaP `-0.7122` edge `0.0849` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2633` n `120` status `ready` deltaP `4.3962` edge `-0.0348` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.488` n `120` status `ready` deltaP `-0.2744` edge `0.0013` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.4989` n `120` status `ready` deltaP `-5.5387` edge `-0.0298` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.872` n `120` status `ready` deltaP `2.1138` edge `-0.0311` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5195` n `120` status `ready` deltaP `-5.8533` edge `-0.0336` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.6194` n `109` status `ready` deltaP `-9.1513` edge `-0.0963` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8016` n `120` status `ready` deltaP `1.1077` edge `-0.2223` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.336` n `109` status `ready` deltaP `9.8099` edge `-0.0012` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2061` n `120` status `ready` deltaP `-5.7317` edge `-0.1411` maxDD `-27.3622`
- `market_context_high->crypto_major_24h` score `-8.3991` n `109` status `ready` deltaP `-10.1377` edge `-0.3361` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
