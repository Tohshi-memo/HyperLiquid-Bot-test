# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T11:22:27.332259+00:00`
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

- `market_context_high->unknown_24h` score `10.8409` n `98` status `ready` deltaP `3.8407` edge `0.8821` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.4992` n `98` status `ready` deltaP `4.8256` edge `0.2096` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0116` n `109` status `ready` deltaP `12.3798` edge `0.0864` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4907` n `98` status `ready` deltaP `20.5321` edge `0.0466` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4036` n `111` status `ready` deltaP `7.655` edge `0.0242` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0499` n `111` status `ready` deltaP `6.3104` edge `-0.0029` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3135` n `109` status `ready` deltaP `6.5703` edge `0.002` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5566` n `111` status `ready` deltaP `-2.0863` edge `-0.008` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.737` n `111` status `ready` deltaP `-3.2839` edge `-0.0192` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7493` n `109` status `ready` deltaP `3.2418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3322` n `98` status `ready` deltaP `-4.5316` edge `0.0789` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4501` n `111` status `ready` deltaP `-4.6475` edge `-0.0188` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8314` n `111` status `ready` deltaP `1.226` edge `-0.0865` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.9185` n `109` status `ready` deltaP `-10.5337` edge `-0.0503` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.0111` n `109` status `ready` deltaP `1.9943` edge `-0.0419` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.3903` n `98` status `ready` deltaP `-2.5333` edge `-0.038` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.15` n `111` status `ready` deltaP `-10.3604` edge `-0.0561` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.7731` n `98` status `ready` deltaP `5.7256` edge `-0.03` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-7.0748` n `109` status `ready` deltaP `-2.4236` edge `-0.362` maxDD `-34.9766`
- `market_context_high->unknown_4h` score `-7.5193` n `109` status `ready` deltaP `-0.7356` edge `-0.5221` maxDD `-3.6349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
