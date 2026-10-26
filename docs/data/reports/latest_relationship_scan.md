# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T11:52:30.711346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8298`

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

- `market_context_high->unknown_4h` score `17.2932` n `138` status `ready` deltaP `-0.8505` edge `1.4803` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5905` n `113` status `ready` deltaP `28.4445` edge `0.1531` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.1179` n `138` status `ready` deltaP `9.1905` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1132` n `150` status `ready` deltaP `6.517` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0306` n `113` status `ready` deltaP `19.7932` edge `0.0292` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2632` n `150` status `ready` deltaP `2.2854` edge `0.0129` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3097` n `150` status `ready` deltaP `5.8922` edge `0.0002` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.4541` n `113` status `ready` deltaP `11.4768` edge `-0.0065` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5336` n `138` status `ready` deltaP `5.0747` edge `0.0446` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6095` n `150` status `ready` deltaP `-1.4012` edge `-0.0036` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0872` n `138` status `ready` deltaP `5.8678` edge `-0.0075` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3158` n `150` status `ready` deltaP `1.483` edge `-0.0205` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.0662` n `138` status `ready` deltaP `-7.6286` edge `-0.0266` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3647` n `150` status `ready` deltaP `-1.8224` edge `-0.0624` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4722` n `150` status `ready` deltaP `-3.2096` edge `-0.0471` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.5398` n `113` status `ready` deltaP `-2.0726` edge `-0.0825` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.3941` n `138` status `ready` deltaP `-4.6152` edge `-0.1568` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.3552` n `113` status `ready` deltaP `-2.9914` edge `-0.2373` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4786` n `113` status `ready` deltaP `-18.8191` edge `-0.1462` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-8.3158` n `138` status `ready` deltaP `-6.6388` edge `-0.2957` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
