# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T11:07:32.270950+00:00`
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

- `market_context_high->unknown_24h` score `13.1893` n `98` status `ready` deltaP `3.8407` edge `1.0778` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.5052` n `98` status `ready` deltaP `4.8256` edge `0.2101` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.008` n `109` status `ready` deltaP `12.3798` edge `0.0861` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4915` n `98` status `ready` deltaP `20.5321` edge `0.0467` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3865` n `110` status `ready` deltaP `7.4115` edge `0.0244` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0179` n `110` status `ready` deltaP `5.9254` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3104` n `109` status `ready` deltaP `6.5703` edge `0.0024` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5353` n `110` status `ready` deltaP `-1.7528` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7181` n `110` status `ready` deltaP `-2.9504` edge `-0.019` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7493` n `109` status `ready` deltaP `3.2418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3615` n `98` status `ready` deltaP `-4.7052` edge `0.0763` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4965` n `110` status `ready` deltaP `-5.1225` edge `-0.0195` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7622` n `110` status `ready` deltaP `1.6168` edge `-0.0844` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.9327` n `109` status `ready` deltaP `-10.6861` edge `-0.0511` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.0389` n `109` status `ready` deltaP `1.8418` edge `-0.0432` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.3741` n `98` status `ready` deltaP `-2.3597` edge `-0.0378` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.2095` n `110` status `ready` deltaP `-10.9091` edge `-0.0574` maxDD `-7.6533`
- `market_context_high->unknown_4h` score `-5.5405` n `109` status `ready` deltaP `-0.7356` edge `-0.3572` maxDD `-3.6349`
- `market_context_high->commodity_24h` score `-6.7883` n `98` status `ready` deltaP `5.552` edge `-0.0308` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-7.135` n `109` status `ready` deltaP `-2.5761` edge `-0.3687` maxDD `-34.9766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
