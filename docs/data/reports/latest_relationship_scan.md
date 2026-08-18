# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T04:07:30.673335+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.6613` n `73` status `ready` deltaP `10.9043` edge `0.3532` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.7619` n `73` status `ready` deltaP `12.6469` edge `0.1625` maxDD `-4.666`
- `market_context_high->metal_24h` score `0.5002` n `73` status `ready` deltaP `4.8384` edge `0.0729` maxDD `-1.7447`
- `market_context_high->commodity_4h` score `0.3557` n `103` status `ready` deltaP `10.2105` edge `0.0466` maxDD `-2.4692`
- `market_context_high->metal_4h` score `0.1058` n `103` status `ready` deltaP `9.5844` edge `0.0081` maxDD `-1.3413`
- `market_context_high->crypto_major_4h` score `0.0551` n `103` status `ready` deltaP `5.8134` edge `0.0704` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.04` n `104` status `ready` deltaP `6.6617` edge `0.0027` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.1205` n `104` status `ready` deltaP `3.1956` edge `0.0235` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.2065` n `103` status `ready` deltaP `4.7863` edge `0.0016` maxDD `-0.3904`
- `market_context_high->unknown_1h` score `-0.2145` n `104` status `ready` deltaP `6.2586` edge `-0.0337` maxDD `-0.7386`
- `market_context_high->metal_1h` score `-0.5817` n `104` status `ready` deltaP `-1.3243` edge `-0.0036` maxDD `-1.3047`
- `market_context_high->commodity_1h` score `-0.6411` n `104` status `ready` deltaP `-3.4834` edge `0.0023` maxDD `-1.5684`
- `market_context_high->fx_1h` score `-0.6448` n `104` status `ready` deltaP `-2.7983` edge `0.0011` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.7271` n `103` status `ready` deltaP `-4.0389` edge `-0.0003` maxDD `-0.613`
- `market_context_high->crypto_major_1h` score `-0.9923` n `104` status `ready` deltaP `-4.2953` edge `-0.003` maxDD `-3.6463`
- `market_context_high->index_24h` score `-1.1492` n `73` status `ready` deltaP `5.7287` edge `-0.0659` maxDD `-2.1112`
- `market_context_high->crypto_alt_4h` score `-1.1896` n `103` status `ready` deltaP `4.0079` edge `0.0477` maxDD `-9.4883`
- `market_context_high->crypto_alt_1h` score `-1.2636` n `104` status `ready` deltaP `-3.2474` edge `0.0052` maxDD `-3.1082`
- `market_context_high->equity_4h` score `-1.3008` n `103` status `ready` deltaP `-6.6704` edge `-0.0109` maxDD `-4.2456`
- `market_context_high->unknown_24h` score `-1.5815` n `73` status `ready` deltaP `2.6186` edge `-0.0846` maxDD `-1.1716`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
