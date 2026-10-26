# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T00:07:27.508343+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.7897` n `113` status `ready` deltaP `-0.7487` edge `2.521` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.3209` n `87` status `ready` deltaP `6.2979` edge `0.0873` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0832` n `113` status `ready` deltaP `3.2603` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.112` n `113` status `ready` deltaP `6.3917` edge `0.0079` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.1792` n `87` status `ready` deltaP `16.7625` edge `0.0225` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.4457` n `87` status `ready` deltaP `14.4277` edge `0.1137` maxDD `-7.3625`
- `market_context_high->commodity_1h` score `-0.4475` n `113` status `ready` deltaP `0.2663` edge `0.011` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6425` n `113` status `ready` deltaP `-1.7368` edge `-0.0056` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6551` n `113` status `ready` deltaP `4.4844` edge `-0.0053` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7102` n `113` status `ready` deltaP `-0.7137` edge `0.0366` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.8385` n `87` status `ready` deltaP `11.0453` edge `-0.0529` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2701` n `113` status `ready` deltaP `3.8458` edge `-0.0304` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0168` n `113` status `ready` deltaP `3.5466` edge `-0.0207` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-2.9348` n `87` status `ready` deltaP `-9.2074` edge `-0.0543` maxDD `-8.8461`
- `market_context_high->crypto_alt_1h` score `-3.1223` n `113` status `ready` deltaP `-1.2612` edge `-0.0644` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8308` n `113` status `ready` deltaP `-0.2398` edge `-0.0903` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.4333` n `87` status `ready` deltaP `-5.2801` edge `-0.2613` maxDD `-43.1856`
- `market_context_high->equity_24h` score `-7.4505` n `87` status `ready` deltaP `0.5508` edge `-0.4305` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-9.9584` n `113` status `ready` deltaP `-12.7428` edge `-0.2451` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
