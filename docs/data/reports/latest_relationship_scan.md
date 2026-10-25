# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T21:37:28.436206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5054`

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

- `market_context_high->unknown_4h` score `29.6565` n `113` status `ready` deltaP `-0.7487` edge `2.5099` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.4741` n `77` status `ready` deltaP `4.4485` edge `0.1124` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.084` n `113` status `ready` deltaP `6.6966` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0988` n `113` status `ready` deltaP `2.9609` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.4494` n `77` status `ready` deltaP `12.3782` edge `0.0171` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.505` n `113` status `ready` deltaP `-0.1828` edge `0.0092` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6539` n `113` status `ready` deltaP `4.4844` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6768` n `113` status `ready` deltaP `-2.3356` edge `-0.006` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7826` n `113` status `ready` deltaP `-1.4759` edge `0.0324` maxDD `-1.165`
- `market_context_high->metal_24h` score `-1.1052` n `77` status `ready` deltaP `6.516` edge `0.0819` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.2329` n `77` status `ready` deltaP `6.8656` edge `-0.0756` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3122` n `113` status `ready` deltaP `3.5464` edge `-0.0338` maxDD `-9.3126`
- `market_context_high->commodity_24h` score `-1.5117` n `77` status `ready` deltaP `-3.6842` edge `-0.0055` maxDD `-4.4329`
- `market_context_high->metal_4h` score `-2.0206` n `113` status `ready` deltaP `3.3941` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1878` n `113` status `ready` deltaP `-8.3774` edge `-0.0372` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1535` n `113` status `ready` deltaP `-1.2612` edge `-0.067` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9242` n `113` status `ready` deltaP `-0.9883` edge `-0.0931` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.6456` n `77` status `ready` deltaP `-1.3438` edge `-0.1974` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-8.7001` n `77` status `ready` deltaP `-5.4203` edge `-0.5509` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.2279` n `113` status `ready` deltaP `-14.2672` edge `-0.2574` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
