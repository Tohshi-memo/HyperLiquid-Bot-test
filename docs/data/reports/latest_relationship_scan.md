# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T21:37:24.614663+00:00`
- Price records: `672`
- Market context records: `2802`
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

- `market_context_high->unknown_24h` score `2.8014` n `142` status `ready` deltaP `4.3378` edge `0.251` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.2731` n `142` status `ready` deltaP `1.6604` edge `0.4867` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.138` n `142` status `ready` deltaP `7.4051` edge `0.1508` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6259` n `142` status `ready` deltaP `11.2114` edge `0.2868` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3215` n `142` status `ready` deltaP `13.3009` edge `0.0367` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0658` n `142` status `ready` deltaP `4.9296` edge `0.0457` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0485` n `142` status `ready` deltaP `4.6471` edge `0.0122` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5383` n `142` status `ready` deltaP `-0.5376` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5741` n `142` status `ready` deltaP `1.1807` edge `0.0031` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7075` n `142` status `ready` deltaP `-1.031` edge `-0.0085` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7459` n `142` status `ready` deltaP `4.9465` edge `0.0474` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8619` n `142` status `ready` deltaP `-2.3003` edge `0.0268` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9334` n `142` status `ready` deltaP `3.7763` edge `0.0421` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.1406` n `142` status `ready` deltaP `2.2673` edge `0.0278` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1715` n `142` status `ready` deltaP `-4.0579` edge `0.0073` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.6342` n `142` status `ready` deltaP `-0.4488` edge `-0.0145` maxDD `-10.0279`
- `market_context_high->crypto_alt_4h` score `-1.6407` n `142` status `ready` deltaP `14.0329` edge `0.2038` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.6434` n `142` status `ready` deltaP `-3.9686` edge `-0.0233` maxDD `-0.6418`
- `market_context_high->metal_4h` score `-2.0341` n `142` status `ready` deltaP `0.1439` edge `-0.0067` maxDD `-11.4038`
- `market_context_high->index_24h` score `-2.1927` n `142` status `ready` deltaP `-1.5674` edge `-0.0742` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
