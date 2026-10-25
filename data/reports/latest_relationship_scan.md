# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T15:22:31.966626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5252`

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

- `market_context_high->unknown_4h` score `37.4029` n `113` status `ready` deltaP `-0.4439` edge `3.1534` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.0977` n `62` status `ready` deltaP `7.9413` edge `0.0461` maxDD `-3.6055`
- `market_context_high->fx_4h` score `-0.0171` n `113` status `ready` deltaP `7.4588` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0498` n `113` status `ready` deltaP `3.8591` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5445` n `113` status `ready` deltaP `-0.6319` edge `0.0089` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6515` n `113` status `ready` deltaP `4.4844` edge `-0.005` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6775` n `113` status `ready` deltaP `-2.3356` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8419` n `113` status `ready` deltaP `-2.3905` edge `0.0309` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.33` n `62` status `ready` deltaP `-5.606` edge `-0.0306` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3605` n `113` status `ready` deltaP `2.6482` edge `-0.034` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.5583` n `62` status `ready` deltaP `2.621` edge `0.0099` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8904` n `113` status `ready` deltaP `4.7661` edge `-0.0183` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1147` n `62` status `ready` deltaP `-1.9321` edge `-0.13` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.187` n `113` status `ready` deltaP `-8.3774` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1426` n `113` status `ready` deltaP `-1.86` edge `-0.0621` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7477` n `62` status `ready` deltaP `-10.1367` edge `0.0223` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.8955` n `113` status `ready` deltaP `-0.6889` edge `-0.0927` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.433` n `62` status `ready` deltaP `-3.4498` edge `-0.2843` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9596` n `113` status `ready` deltaP `-12.7428` edge `-0.2452` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.9144` n `62` status `ready` deltaP `-17.9883` edge `-0.8792` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
