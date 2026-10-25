# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T20:37:32.712168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5002`

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

- `market_context_high->unknown_4h` score `29.7621` n `113` status `ready` deltaP `-0.7487` edge `2.5187` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.22` n `73` status `ready` deltaP `2.1713` edge `0.1064` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.0439` n `113` status `ready` deltaP `7.1539` edge `0.0085` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0661` n `113` status `ready` deltaP `3.5597` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4799` n `113` status `ready` deltaP `0.1166` edge `0.0093` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.5884` n `73` status `ready` deltaP `10.155` edge `0.0141` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.6419` n `113` status `ready` deltaP `4.6341` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7095` n `113` status `ready` deltaP `-2.9344` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8008` n `113` status `ready` deltaP `-1.7807` edge `0.0321` maxDD `-1.165`
- `market_context_high->commodity_24h` score `-1.0971` n `73` status `ready` deltaP `-1.0512` edge `0.0048` maxDD `-3.7427`
- `market_context_high->crypto_major_1h` score `-1.3589` n `113` status `ready` deltaP `2.9476` edge `-0.0358` maxDD `-9.3126`
- `market_context_high->metal_24h` score `-1.405` n `73` status `ready` deltaP `2.7445` edge `0.0686` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.4192` n `73` status `ready` deltaP `4.873` edge `-0.0862` maxDD `-4.925`
- `market_context_high->metal_4h` score `-2.0206` n `113` status `ready` deltaP `3.3941` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.206` n `113` status `ready` deltaP `-8.6822` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.2458` n `113` status `ready` deltaP `-1.86` edge `-0.0707` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9853` n `113` status `ready` deltaP `-1.5871` edge `-0.0942` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.4678` n `73` status `ready` deltaP `0.6659` edge `-0.188` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-9.3442` n `73` status `ready` deltaP `-8.2667` edge `-0.6145` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.3403` n `113` status `ready` deltaP `-14.8769` edge `-0.2627` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
