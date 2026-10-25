# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T21:22:36.923741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5046`

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

- `market_context_high->unknown_4h` score `29.6709` n `113` status `ready` deltaP `-0.7487` edge `2.5111` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.4172` n `76` status `ready` deltaP `3.9016` edge `0.1113` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.0707` n `113` status `ready` deltaP `6.849` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.091` n `113` status `ready` deltaP `3.1106` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.483` n `76` status `ready` deltaP `11.8512` edge `0.0163` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.505` n `113` status `ready` deltaP `-0.1828` edge `0.0092` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6539` n `113` status `ready` deltaP `4.4844` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6853` n `113` status `ready` deltaP `-2.4853` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7913` n `113` status `ready` deltaP `-1.6283` edge `0.0323` maxDD `-1.165`
- `market_context_high->metal_24h` score `-1.178` n `76` status `ready` deltaP `5.6104` edge `0.0786` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.278` n `76` status `ready` deltaP `6.3871` edge `-0.0782` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3231` n `113` status `ready` deltaP `3.3967` edge `-0.0342` maxDD `-9.3126`
- `market_context_high->commodity_24h` score `-1.4101` n `76` status `ready` deltaP `-3.0519` edge `-0.003` maxDD `-4.2614`
- `market_context_high->metal_4h` score `-2.0206` n `113` status `ready` deltaP `3.3941` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1878` n `113` status `ready` deltaP `-8.3774` edge `-0.0372` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1727` n `113` status `ready` deltaP `-1.4109` edge `-0.0676` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9398` n `113` status `ready` deltaP `-1.138` edge `-0.0934` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.6068` n `76` status `ready` deltaP `-0.8681` edge `-0.1956` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-8.8542` n `76` status `ready` deltaP `-6.1038` edge `-0.5661` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.2557` n `113` status `ready` deltaP `-14.4196` edge `-0.2587` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
