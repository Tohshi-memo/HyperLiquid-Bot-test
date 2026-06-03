# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T17:52:28.173096+00:00`
- Price records: `672`
- Market context records: `2786`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.2374` n `142` status `ready` deltaP `6.2475` edge `0.2746` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.6861` n `142` status `ready` deltaP `3.9173` edge `0.5894` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8544` n `142` status `ready` deltaP `6.1856` edge `0.1353` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5545` n `142` status `ready` deltaP `11.0377` edge `0.282` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2845` n `142` status `ready` deltaP `12.8435` edge `0.035` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0901` n `142` status `ready` deltaP `3.732` edge `0.0407` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0906` n `142` status `ready` deltaP `4.198` edge `0.0098` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.549` n `142` status `ready` deltaP `-0.6873` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6396` n `142` status `ready` deltaP `0.4322` edge `-0.0003` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7005` n `142` status `ready` deltaP `-1.031` edge `-0.0076` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7311` n `142` status `ready` deltaP `4.7968` edge `0.0503` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9451` n `142` status `ready` deltaP `3.6266` edge `0.0416` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0214` n `142` status `ready` deltaP `-3.1985` edge `0.0195` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.0947` n `142` status `ready` deltaP `-3.1432` edge `0.0076` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.3022` n `142` status `ready` deltaP `1.6575` edge `0.0184` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.3249` n `142` status `ready` deltaP `14.1854` edge `0.2291` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4285` n `142` status `ready` deltaP `-1.538` edge `-0.0216` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6365` n `142` status `ready` deltaP `-0.4488` edge `-0.0148` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.1511` n `142` status `ready` deltaP `-0.7708` edge `-0.0156` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4223` n `142` status `ready` deltaP `5.7347` edge `0.1418` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
