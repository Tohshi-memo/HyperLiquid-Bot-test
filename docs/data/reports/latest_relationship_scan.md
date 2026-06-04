# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T04:37:23.591111+00:00`
- Price records: `672`
- Market context records: `2832`
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

- `market_context_high->unknown_24h` score `2.3135` n `142` status `ready` deltaP `2.9489` edge `0.2196` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9016` n `142` status `ready` deltaP `6.4904` edge `0.1372` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7617` n `142` status `ready` deltaP `11.5586` edge `0.2958` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.4472` n `142` status `ready` deltaP `-0.2494` edge `0.4306` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.2979` n `142` status `ready` deltaP `12.996` edge `0.0357` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0217` n `142` status `ready` deltaP `4.0314` edge `0.0444` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1443` n `142` status `ready` deltaP `3.4495` edge `0.0079` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5735` n `142` status `ready` deltaP `0.1666` edge `0.0007` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->index_24h` score `-0.6098` n `142` status `ready` deltaP `3.2937` edge `0.0253` maxDD `-2.5127`
- `market_context_high->metal_1h` score `-0.7869` n `142` status `ready` deltaP `-0.6157` edge `-0.0122` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.8371` n `142` status `ready` deltaP `4.3477` edge `0.0397` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-1.0519` n `142` status `ready` deltaP `3.3272` edge `0.0299` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0837` n `142` status `ready` deltaP `-3.4979` edge `0.0163` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.0858` n `142` status `ready` deltaP `1.9624` edge `0.0344` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1701` n `142` status `ready` deltaP `-3.9054` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3004` n `142` status `ready` deltaP `2.2951` edge `0.01` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.5746` n `142` status `ready` deltaP `-3.2741` edge `-0.0222` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.6511` n `142` status `ready` deltaP `13.4232` edge `0.207` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.4288` n `142` status `ready` deltaP `-1.6854` edge `-0.0451` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
