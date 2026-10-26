# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T02:37:38.672838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5104`

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

- `market_context_high->unknown_4h` score `27.6767` n `113` status `ready` deltaP `-1.5109` edge `2.35` maxDD `-1.016`
- `market_context_high->fx_24h` score `0.0252` n `97` status `ready` deltaP `19.8848` edge `0.0279` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.0022` n `97` status `ready` deltaP `20.708` edge `0.1287` maxDD `-7.3625`
- `market_context_high->fx_4h` score `-0.0888` n `113` status `ready` deltaP `6.6966` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1297` n `115` status `ready` deltaP `2.5019` edge `0.0018` maxDD `-0.1424`
- `market_context_high->commodity_1h` score `-0.4399` n `115` status `ready` deltaP `0.2564` edge `0.0117` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6165` n `113` status `ready` deltaP `0.3534` edge `0.0415` maxDD `-1.165`
- `market_context_high->metal_1h` score `-0.6786` n `115` status `ready` deltaP `4.2059` edge `-0.0054` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.7655` n `97` status `ready` deltaP `10.9339` edge `-0.0428` maxDD `-4.925`
- `market_context_high->index_1h` score `-1.0429` n `115` status `ready` deltaP `-2.3874` edge `-0.0058` maxDD `-1.2155`
- `market_context_high->crypto_major_1h` score `-1.3369` n `115` status `ready` deltaP `3.2218` edge `-0.0348` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0084` n `113` status `ready` deltaP `3.5466` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1506` n `113` status `ready` deltaP `-7.7676` edge `-0.0365` maxDD `-4.3282`
- `market_context_high->crypto_major_24h` score `-2.3704` n `97` status `ready` deltaP `1.5249` edge `-0.0144` maxDD `-11.1307`
- `market_context_high->crypto_alt_1h` score `-3.3602` n `115` status `ready` deltaP `-1.4319` edge `-0.0687` maxDD `-11.8082`
- `market_context_high->equity_1h` score `-3.8804` n `115` status `ready` deltaP `-0.8904` edge `-0.0901` maxDD `-12.1865`
- `market_context_high->commodity_24h` score `-4.3515` n `97` status `ready` deltaP `-13.5918` edge `-0.0968` maxDD `-14.3041`
- `market_context_high->equity_24h` score `-7.3657` n `97` status `ready` deltaP `-1.5678` edge `-0.4055` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-9.8636` n `97` status `ready` deltaP `-9.2622` edge `-0.3723` maxDD `-57.1077`
- `market_context_high->crypto_major_4h` score `-10.0508` n `113` status `ready` deltaP `-12.7428` edge `-0.2528` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
