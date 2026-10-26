# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T03:52:29.860698+00:00`
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

- `market_context_high->unknown_4h` score `27.2643` n `113` status `ready` deltaP `-2.1207` edge `2.3197` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.2174` n `102` status `ready` deltaP `23.3864` edge `0.139` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.0964` n `102` status `ready` deltaP `21.0886` edge `0.029` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0645` n `113` status `ready` deltaP `7.0014` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1179` n `120` status `ready` deltaP `2.8643` edge `0.0016` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.3224` n `120` status `ready` deltaP `5.8583` edge `-0.0012` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4088` n `120` status `ready` deltaP `-1.7315` edge `0.0092` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5613` n `113` status `ready` deltaP `1.1156` edge `0.0435` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.704` n `120` status `ready` deltaP `-2.9042` edge `-0.0057` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.8227` n `102` status `ready` deltaP `9.324` edge `-0.0394` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.469` n `120` status `ready` deltaP `1.7315` edge `-0.0418` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0608` n `113` status `ready` deltaP `2.9368` edge `-0.0203` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1514` n `113` status `ready` deltaP `-7.7676` edge `-0.0366` maxDD `-4.3282`
- `market_context_high->crypto_major_24h` score `-3.123` n `102` status `ready` deltaP `-0.2349` edge `-0.0846` maxDD `-19.1376`
- `market_context_high->crypto_alt_1h` score `-3.8294` n `120` status `ready` deltaP `-2.6447` edge `-0.07` maxDD `-12.5187`
- `market_context_high->equity_1h` score `-3.888` n `120` status `ready` deltaP `-1.1078` edge `-0.088` maxDD `-12.2891`
- `market_context_high->commodity_24h` score `-5.0912` n `102` status `ready` deltaP `-15.4616` edge `-0.1184` maxDD `-17.4995`
- `market_context_high->equity_24h` score `-7.4259` n `102` status `ready` deltaP `-3.1761` edge `-0.4025` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1168` n `113` status `ready` deltaP `-12.7428` edge `-0.2583` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-11.3338` n `102` status `ready` deltaP `-11.1826` edge `-0.4327` maxDD `-65.6642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
