# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T19:37:31.189812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.6624` n `50` status `ready` deltaP `14.3847` edge `4.4593` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.2507` n `50` status `ready` deltaP `45.0468` edge `2.5147` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.4872` n `61` status `ready` deltaP `23.548` edge `0.8145` maxDD `-0.1374`
- `news_risk_high->crypto_major_24h` score `6.5623` n `50` status `ready` deltaP `24.208` edge `0.4348` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `5.9959` n `50` status `ready` deltaP `30.1005` edge `0.3918` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3578` n `50` status `ready` deltaP `43.4073` edge `0.078` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `3.9711` n `120` status `ready` deltaP `7.718` edge `0.3527` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `3.5125` n `71` status `ready` deltaP `9.5556` edge `0.2647` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `3.4966` n `61` status `ready` deltaP `41.9157` edge `0.0295` maxDD `-0.0711`
- `market_context_high->metal_24h` score `3.175` n `120` status `ready` deltaP `28.7406` edge `0.1749` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.3818` n `50` status `ready` deltaP `26.9948` edge `0.0336` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2885` n `120` status `ready` deltaP `17.5508` edge `0.1144` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9251` n `120` status `ready` deltaP `9.3913` edge `0.0595` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5818` n `71` status `ready` deltaP `12.2101` edge `0.0058` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3922` n `71` status `ready` deltaP `11.761` edge `0.0039` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0565` n `120` status `ready` deltaP `13.1504` edge `0.0113` maxDD `-3.3377`
- `news_risk_high->index_4h` score `-0.3825` n `61` status `ready` deltaP `3.1838` edge `-0.0165` maxDD `-1.3012`
- `market_context_high->fx_1h` score `-0.4044` n `120` status `ready` deltaP `3.3134` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4678` n `71` status `ready` deltaP `-1.031` edge `-0.0097` maxDD `-0.8054`
- `news_risk_high->metal_4h` score `-0.5701` n `61` status `ready` deltaP `8.7515` edge `-0.0342` maxDD `-3.7783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
