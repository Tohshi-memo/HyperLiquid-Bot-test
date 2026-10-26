# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T00:16:05.264412+00:00`
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

- `market_context_high->unknown_4h` score `29.8485` n `113` status `ready` deltaP `-0.7487` edge `2.5259` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.2072` n `88` status `ready` deltaP `5.7923` edge `0.0812` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0832` n `113` status `ready` deltaP `3.2603` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.112` n `113` status `ready` deltaP `6.3917` edge `0.0079` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.1557` n `88` status `ready` deltaP `17.1244` edge `0.0231` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.3941` n `88` status `ready` deltaP `15.1199` edge `0.1157` maxDD `-7.3625`
- `market_context_high->commodity_1h` score `-0.4319` n `113` status `ready` deltaP `0.416` edge `0.0113` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6339` n `113` status `ready` deltaP `-1.5871` edge `-0.0055` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6419` n `113` status `ready` deltaP `4.6341` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.6976` n `113` status `ready` deltaP `-0.5612` edge `0.0372` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.807` n `88` status `ready` deltaP `11.411` edge `-0.0513` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2592` n `113` status `ready` deltaP `3.9955` edge `-0.03` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0034` n `113` status `ready` deltaP `3.699` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-3.0763` n `88` status `ready` deltaP `-9.6906` edge `-0.0588` maxDD `-9.3461`
- `market_context_high->crypto_alt_1h` score `-3.1211` n `113` status `ready` deltaP `-1.2612` edge `-0.0643` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8272` n `113` status `ready` deltaP `-0.2398` edge `-0.09` maxDD `-12.1865`
- `market_context_high->equity_24h` score `-7.3594` n `88` status `ready` deltaP `1.0733` edge `-0.4223` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-7.6131` n `88` status `ready` deltaP `-5.6029` edge `-0.2695` maxDD `-44.2011`
- `market_context_high->crypto_major_4h` score `-9.9524` n `113` status `ready` deltaP `-12.7428` edge `-0.2446` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
