# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T01:37:22.550533+00:00`
- Price records: `672`
- Market context records: `2820`
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

- `market_context_high->unknown_24h` score `2.3771` n `142` status `ready` deltaP `2.9489` edge `0.2249` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.8894` n `142` status `ready` deltaP `6.338` edge `0.1372` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7509` n `142` status `ready` deltaP `11.5586` edge `0.2949` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2972` n `142` status `ready` deltaP `13.1484` edge `0.0346` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1701` n `142` status `ready` deltaP `5.229` edge `0.0524` maxDD `-3.1801`
- `market_context_high->crypto_alt_24h` score `0.1302` n `142` status `ready` deltaP `-0.5966` edge `0.4065` maxDD `-22.6673`
- `market_context_high->index_1h` score `-0.0781` n `142` status `ready` deltaP `4.198` edge `0.0114` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5239` n `142` status `ready` deltaP `-0.3879` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6234` n `142` status `ready` deltaP `-0.1328` edge `-0.0037` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6952` n `142` status `ready` deltaP `5.0962` edge `0.0529` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7043` n `142` status `ready` deltaP `0.1328` edge `-0.0066` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8975` n `142` status `ready` deltaP `3.7763` edge `0.0467` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9075` n `142` status `ready` deltaP `-2.7494` edge `0.026` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.1168` n `142` status `ready` deltaP `2.1148` edge `0.0308` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1775` n `142` status `ready` deltaP `-4.0579` edge `0.0068` maxDD `-0.5631`
- `market_context_high->index_24h` score `-1.3717` n `142` status `ready` deltaP `1.2104` edge `-0.0243` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `-1.3789` n `142` status `ready` deltaP `1.6854` edge `0.004` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.7061` n `142` status `ready` deltaP `-4.663` edge `-0.0239` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-2.0739` n `142` status `ready` deltaP `13.1183` edge `0.1738` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.3807` n `142` status `ready` deltaP `-1.0756` edge `-0.043` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
