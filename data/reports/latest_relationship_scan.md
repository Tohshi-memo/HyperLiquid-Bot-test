# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T15:22:34.281059+00:00`
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

- `market_context_high->metal_24h` score `1.7575` n `108` status `ready` deltaP `6.5681` edge `0.1686` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7483` n `121` status `ready` deltaP `10.9294` edge `0.0311` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.41` n `108` status `ready` deltaP `19.177` edge `0.0438` maxDD `-4.1933`
- `market_context_high->commodity_4h` score `0.3343` n `109` status `ready` deltaP `10.2428` edge `0.0592` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.1351` n `121` status `ready` deltaP `9.2047` edge `-0.0035` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.3098` n `109` status `ready` deltaP `7.0163` edge `-0.0005` maxDD `-1.8797`
- `market_context_high->index_24h` score `-0.5212` n `108` status `ready` deltaP `1.4964` edge `0.0979` maxDD `-5.7715`
- `market_context_high->metal_1h` score `-0.6084` n `121` status `ready` deltaP `-0.8437` edge `-0.0058` maxDD `-1.1422`
- `market_context_high->metal_4h` score `-0.7195` n `109` status `ready` deltaP `2.1748` edge `0.0015` maxDD `-1.7431`
- `market_context_high->crypto_alt_1h` score `-0.8771` n `121` status `ready` deltaP `-5.2098` edge `-0.0148` maxDD `-2.3669`
- `market_context_high->index_1h` score `-0.992` n `121` status `ready` deltaP `-2.5746` edge `-0.0121` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.3729` n `121` status `ready` deltaP `3.5941` edge `-0.0435` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.7417` n `109` status `ready` deltaP `2.1523` edge `-0.0205` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1581` n `109` status `ready` deltaP `-4.7298` edge `-0.0287` maxDD `-4.2354`
- `market_context_high->crypto_major_1h` score `-2.5155` n `121` status `ready` deltaP `-6.0486` edge `-0.0396` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.8845` n `108` status `ready` deltaP `-11.1605` edge `-0.105` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.8529` n `109` status `ready` deltaP `-6.8836` edge `-0.1827` maxDD `-25.1525`
- `market_context_high->crypto_major_24h` score `-5.8661` n `108` status `ready` deltaP `-4.894` edge `-0.2749` maxDD `-26.2292`
- `market_context_high->equity_24h` score `-7.8939` n `108` status `ready` deltaP `-10.0228` edge `0.1204` maxDD `-47.5791`
- `market_context_high->unknown_1h` score `-8.2357` n `121` status `ready` deltaP `-0.1794` edge `-0.6404` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
