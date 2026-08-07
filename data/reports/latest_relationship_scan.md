# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T15:06:14.673781+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11756`

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

- `market_context_high->metal_24h` score `1.6188` n `109` status `ready` deltaP `6.0299` edge `0.1648` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7519` n `121` status `ready` deltaP `10.9294` edge `0.0314` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4224` n `109` status `ready` deltaP `19.4009` edge `0.0439` maxDD `-4.1933`
- `market_context_high->commodity_4h` score `0.3768` n `110` status `ready` deltaP `10.6098` edge `0.0622` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.1411` n `121` status `ready` deltaP `9.2047` edge `-0.003` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2909` n `110` status `ready` deltaP `7.306` edge `0.0` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6096` n `121` status `ready` deltaP `-0.8437` edge `-0.0059` maxDD `-1.1422`
- `market_context_high->index_24h` score `-0.6211` n `109` status `ready` deltaP `0.9527` edge `0.0932` maxDD `-5.7715`
- `market_context_high->metal_4h` score `-0.7989` n `110` status `ready` deltaP `1.5993` edge `0.0002` maxDD `-1.8617`
- `market_context_high->crypto_alt_1h` score `-0.8263` n `121` status `ready` deltaP `-4.5331` edge `-0.0128` maxDD `-2.3669`
- `market_context_high->index_1h` score `-1.0533` n `121` status `ready` deltaP `-3.2513` edge `-0.0127` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.4354` n `121` status `ready` deltaP `2.9173` edge `-0.047` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.6966` n `110` status `ready` deltaP `2.4002` edge `-0.0184` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1931` n `110` status `ready` deltaP `-5.0194` edge `-0.0291` maxDD `-4.2825`
- `market_context_high->crypto_major_1h` score `-2.4374` n `121` status `ready` deltaP `-5.3719` edge `-0.0376` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.8491` n `109` status `ready` deltaP `-10.9877` edge `-0.1032` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.7984` n `110` status `ready` deltaP `-6.5105` edge `-0.1782` maxDD `-25.1525`
- `market_context_high->crypto_major_24h` score `-6.0695` n `109` status `ready` deltaP `-5.3867` edge `-0.2812` maxDD `-27.2154`
- `market_context_high->unknown_1h` score `-8.1708` n `121` status `ready` deltaP `0.4974` edge `-0.6395` maxDD `-1.2437`
- `market_context_high->equity_24h` score `-8.7356` n `109` status `ready` deltaP `-10.3996` edge `0.0911` maxDD `-50.3125`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
