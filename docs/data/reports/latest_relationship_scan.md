# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T12:37:32.556796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `38.4423` n `113` status `ready` deltaP `-0.2914` edge `3.239` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.557` n `56` status `ready` deltaP `14.1617` edge `0.0679` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0475` n `113` status `ready` deltaP `8.221` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0817` n `113` status `ready` deltaP `3.2603` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5182` n `113` status `ready` deltaP `-0.3325` edge `0.0091` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6628` n `113` status `ready` deltaP `-2.0362` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6754` n `113` status `ready` deltaP `4.185` edge `-0.005` maxDD `-1.6682`
- `market_context_high->crypto_major_24h` score `-0.8236` n `56` status `ready` deltaP `-1.1161` edge `0.0044` maxDD `-4.5369`
- `market_context_high->commodity_4h` score `-0.9154` n `113` status `ready` deltaP `-3.61` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4407` n `113` status `ready` deltaP `1.6003` edge `-0.0373` maxDD `-9.3126`
- `market_context_high->unknown_1h` score `-1.6607` n `113` status `ready` deltaP `4.1704` edge `-0.1173` maxDD `-1.5781`
- `market_context_high->metal_4h` score `-1.8868` n `113` status `ready` deltaP `4.7661` edge `-0.018` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-1.8951` n `56` status `ready` deltaP `-1.2897` edge `0.0079` maxDD `-1.2451`
- `market_context_high->index_4h` score `-2.187` n `113` status `ready` deltaP `-8.3774` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->index_24h` score `-2.4856` n `56` status `ready` deltaP `-6.7708` edge `-0.1453` maxDD `-4.925`
- `market_context_high->crypto_alt_1h` score `-3.2409` n `113` status `ready` deltaP `-2.6085` edge `-0.0653` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7373` n `56` status `ready` deltaP `-11.2351` edge `0.0084` maxDD `-7.2618`
- `market_context_high->equity_1h` score `-3.8991` n `113` status `ready` deltaP `-0.5392` edge `-0.094` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-5.1528` n `56` status `ready` deltaP `1.7361` edge `-0.1436` maxDD `-34.954`
- `market_context_high->crypto_major_4h` score `-10.0472` n `113` status `ready` deltaP `-12.7428` edge `-0.2525` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
