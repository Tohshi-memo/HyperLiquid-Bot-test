# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T05:07:29.666834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7184`

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

- `market_context_high->unknown_4h` score `27.0618` n `113` status `ready` deltaP `-2.8829` edge `2.3079` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.41` n `107` status `ready` deltaP `25.8145` edge `0.1475` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1575` n `107` status `ready` deltaP `22.0989` edge `0.0301` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0243` n `113` status `ready` deltaP `7.4588` edge `0.0081` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0314` n `125` status `ready` deltaP `4.4982` edge `0.0018` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3431` n `125` status `ready` deltaP `-0.4982` edge `0.0094` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3622` n `125` status `ready` deltaP `5.0922` edge `-0.0012` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.5107` n `113` status `ready` deltaP `1.8778` edge `0.0449` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6199` n `125` status `ready` deltaP `-1.4527` edge `-0.0046` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.7336` n `107` status `ready` deltaP `10.2123` edge `-0.0339` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3809` n `125` status `ready` deltaP `2.2994` edge `-0.0343` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.1337` n `113` status `ready` deltaP `2.1746` edge `-0.0213` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1727` n `113` status `ready` deltaP `-8.0725` edge `-0.0373` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.42` n `125` status `ready` deltaP `-0.3066` edge `-0.0796` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.5545` n `125` status `ready` deltaP `-2.3605` edge `-0.0633` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.3622` n `107` status `ready` deltaP `-1.7491` edge `-0.1304` maxDD `-25.7089`
- `market_context_high->commodity_24h` score `-5.7939` n `107` status `ready` deltaP `-17.1567` edge `-0.1377` maxDD `-20.5917`
- `market_context_high->equity_24h` score `-7.4075` n `107` status `ready` deltaP `-4.5528` edge `-0.3868` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.195` n `113` status `ready` deltaP `-12.8952` edge `-0.2638` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-12.6063` n `107` status `ready` deltaP `-12.5763` edge `-0.4732` maxDD `-73.0649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
