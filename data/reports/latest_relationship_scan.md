# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T23:07:27.644407+00:00`
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

- `market_context_high->unknown_4h` score `29.6781` n `113` status `ready` deltaP `-0.7487` edge `2.5117` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.7157` n `83` status `ready` deltaP `7.4527` edge `0.1125` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0747` n `113` status `ready` deltaP `3.41` edge `0.0026` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1108` n `113` status `ready` deltaP `6.3917` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.2761` n `83` status `ready` deltaP `15.1857` edge `0.0206` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4475` n `113` status `ready` deltaP `0.2663` edge `0.011` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6705` n `113` status `ready` deltaP `-2.1859` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->metal_24h` score `-0.6733` n `83` status `ready` deltaP `11.4918` edge `0.1041` maxDD `-7.3625`
- `market_context_high->metal_1h` score `-0.709` n `113` status `ready` deltaP `3.8856` edge `-0.0058` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7473` n `113` status `ready` deltaP `-1.171` edge `0.0349` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.9714` n `83` status `ready` deltaP `9.4943` edge `-0.0596` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3364` n `113` status `ready` deltaP `3.247` edge `-0.0349` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0278` n `113` status `ready` deltaP `3.3941` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1791` n `113` status `ready` deltaP `-8.2249` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-2.4064` n `83` status `ready` deltaP `-7.1578` edge `-0.0375` maxDD `-7.1966`
- `market_context_high->crypto_alt_1h` score `-3.2135` n `113` status `ready` deltaP `-1.7103` edge `-0.069` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8991` n `113` status `ready` deltaP `-0.6889` edge `-0.093` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.979` n `83` status `ready` deltaP `-3.8697` edge `-0.2233` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-7.8543` n `83` status `ready` deltaP `-1.665` edge `-0.4675` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.0792` n `113` status `ready` deltaP `-13.3526` edge `-0.2511` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
