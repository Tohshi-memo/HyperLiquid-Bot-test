# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T04:22:32.039807+00:00`
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

- `market_context_high->commodity_4h` score `1.1611` n `120` status `ready` deltaP `13.3333` edge `0.0925` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8258` n `109` status `ready` deltaP `3.5334` edge `0.1621` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5785` n `109` status `ready` deltaP `21.4854` edge `0.0515` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4655` n `120` status `ready` deltaP `7.6497` edge `0.0294` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.032` n `120` status `ready` deltaP `6.4521` edge `-0.0039` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2598` n `120` status `ready` deltaP `7.439` edge `0.0031` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5474` n `120` status `ready` deltaP `-2.0758` edge `-0.0069` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7622` n `120` status `ready` deltaP `-2.8443` edge `-0.0077` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9545` n `120` status `ready` deltaP `-1.9261` edge `-0.0133` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0884` n `109` status `ready` deltaP `-0.7122` edge `0.0847` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2735` n `120` status `ready` deltaP `4.2465` edge `-0.0351` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.4674` n `120` status `ready` deltaP `-0.122` edge `0.002` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.5092` n `120` status `ready` deltaP `-5.6911` edge `-0.0301` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8696` n `120` status `ready` deltaP `2.1138` edge `-0.0309` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5362` n `120` status `ready` deltaP `-6.003` edge `-0.034` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.605` n `109` status `ready` deltaP `-9.1513` edge `-0.0951` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8008` n `120` status `ready` deltaP `1.1077` edge `-0.2222` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.336` n `109` status `ready` deltaP `9.8099` edge `-0.0012` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.1929` n `120` status `ready` deltaP `-5.7317` edge `-0.14` maxDD `-27.3622`
- `market_context_high->unknown_24h` score `-8.3238` n `109` status `ready` deltaP `3.7571` edge `-0.7144` maxDD `-0.0104`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
