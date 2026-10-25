# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T08:37:29.005659+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7912`

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

- `market_context_high->unknown_4h` score `40.9084` n `106` status `ready` deltaP `-0.5752` edge `3.4464` maxDD `-1.016`
- `market_context_high->unknown_1h` score `8.1095` n `114` status `ready` deltaP `4.4831` edge `0.6948` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `3.0232` n `42` status `ready` deltaP `18.4028` edge `0.4206` maxDD `-10.1227`
- `market_context_high->crypto_major_24h` score `1.1943` n `42` status `ready` deltaP `10.119` edge `0.138` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.8972` n `42` status `ready` deltaP `17.6587` edge `0.0882` maxDD `-3.6055`
- `market_context_high->fx_4h` score `-0.0204` n `106` status `ready` deltaP `7.2797` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.065` n `114` status `ready` deltaP `3.5508` edge `0.0029` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.511` n `114` status `ready` deltaP `-0.2127` edge `0.0089` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6071` n `114` status `ready` deltaP `4.9191` edge `-0.0042` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.6078` n `42` status `ready` deltaP `3.125` edge `0.0063` maxDD `-1.0707`
- `market_context_high->index_1h` score `-0.6456` n `114` status `ready` deltaP `-1.8411` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8346` n `106` status `ready` deltaP `-2.4764` edge `0.0324` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3935` n `114` status `ready` deltaP `1.5627` edge `-0.031` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.7671` n `106` status `ready` deltaP `6.3823` edge `-0.0188` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0543` n `106` status `ready` deltaP `-5.8704` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.8458` n `42` status `ready` deltaP `-6.4732` edge `-0.0194` maxDD `-6.6343`
- `market_context_high->crypto_alt_1h` score `-3.1118` n `114` status `ready` deltaP `-2.1195` edge `-0.0578` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7827` n `114` status `ready` deltaP `-0.1944` edge `-0.0866` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.5542` n `42` status `ready` deltaP `-23.0407` edge `-0.1791` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-6.0423` n `106` status `ready` deltaP `-10.4636` edge `-0.2052` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
