# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T16:52:53.116177+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5374`

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

- `market_context_high->unknown_4h` score `31.2491` n `113` status `ready` deltaP `-0.5963` edge `2.6416` maxDD `-1.016`
- `market_context_high->fx_1h` score `-0.042` n `113` status `ready` deltaP `4.0088` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0427` n `113` status `ready` deltaP `7.1539` edge `0.0086` maxDD `-0.4545`
- `market_context_high->commodity_24h` score `-0.2708` n `65` status `ready` deltaP `5.187` edge `0.0341` maxDD `-3.6055`
- `market_context_high->commodity_1h` score `-0.4775` n `113` status `ready` deltaP `0.1166` edge `0.0095` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6515` n `113` status `ready` deltaP `4.4844` edge `-0.005` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7017` n `113` status `ready` deltaP `-2.7847` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.785` n `113` status `ready` deltaP `-1.4759` edge `0.0321` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.2172` n `65` status `ready` deltaP `-3.2239` edge `0.0226` maxDD `-4.5369`
- `market_context_high->fx_24h` score `-1.3275` n `65` status `ready` deltaP `5.3259` edge `0.0111` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-1.3581` n `113` status `ready` deltaP `2.6482` edge `-0.0337` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8952` n `113` status `ready` deltaP `4.7661` edge `-0.0187` maxDD `-5.3474`
- `market_context_high->index_24h` score `-1.908` n `65` status `ready` deltaP `0.1523` edge `-0.1174` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1973` n `113` status `ready` deltaP `-8.5298` edge `-0.0374` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1894` n `113` status `ready` deltaP `-2.0097` edge `-0.065` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.2713` n `65` status `ready` deltaP `-6.1913` edge `0.0357` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.941` n `113` status `ready` deltaP `-1.138` edge `-0.0935` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.0958` n `65` status `ready` deltaP `-1.9605` edge `-0.251` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9874` n `113` status `ready` deltaP `-12.8952` edge `-0.2465` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.1449` n `65` status `ready` deltaP `-15.0107` edge `-0.8004` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
