# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T05:01:05.340363+00:00`
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

- `market_context_high->unknown_4h` score `27.0594` n `113` status `ready` deltaP `-2.8829` edge `2.3077` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.4092` n `107` status `ready` deltaP `25.8145` edge `0.1474` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1575` n `107` status `ready` deltaP `22.0989` edge `0.0301` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0243` n `113` status `ready` deltaP `7.4588` edge `0.0081` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0314` n `125` status `ready` deltaP `4.4982` edge `0.0018` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3431` n `125` status `ready` deltaP `-0.4982` edge `0.0094` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3622` n `125` status `ready` deltaP `5.0922` edge `-0.0012` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.5107` n `113` status `ready` deltaP `1.8778` edge `0.0449` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6192` n `125` status `ready` deltaP `-1.4527` edge `-0.0045` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.7328` n `107` status `ready` deltaP `10.2123` edge `-0.0338` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.377` n `125` status `ready` deltaP `2.2994` edge `-0.0338` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.1337` n `113` status `ready` deltaP `2.1746` edge `-0.0213` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1727` n `113` status `ready` deltaP `-8.0725` edge `-0.0373` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4192` n `125` status `ready` deltaP `-0.3066` edge `-0.0795` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.5482` n `125` status `ready` deltaP `-2.3605` edge `-0.0625` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.3496` n `107` status `ready` deltaP `-1.7491` edge `-0.1298` maxDD `-25.6278`
- `market_context_high->commodity_24h` score `-5.7972` n `107` status `ready` deltaP `-17.1567` edge `-0.1379` maxDD `-20.6099`
- `market_context_high->equity_24h` score `-7.4067` n `107` status `ready` deltaP `-4.5528` edge `-0.3867` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1962` n `113` status `ready` deltaP `-12.8952` edge `-0.2639` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-12.5841` n `107` status `ready` deltaP `-12.5763` edge `-0.4721` maxDD `-72.9257`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
