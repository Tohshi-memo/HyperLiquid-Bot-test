# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T08:07:32.467419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8620`

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

- `market_context_high->unknown_4h` score `18.1309` n `125` status `ready` deltaP `-2.8134` edge `1.5632` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6061` n `113` status `ready` deltaP `28.4445` edge `0.1551` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1628` n `113` status `ready` deltaP `22.0501` edge `0.0311` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0565` n `125` status `ready` deltaP `8.439` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0153` n `135` status `ready` deltaP `4.8226` edge `0.0017` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3476` n `135` status `ready` deltaP `1.395` edge `0.0118` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3591` n `135` status `ready` deltaP `5.153` edge `-0.0012` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.472` n `125` status `ready` deltaP `2.5329` edge `0.0455` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.5888` n `113` status `ready` deltaP `10.956` edge `-0.0203` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.6601` n `135` status `ready` deltaP `-2.1357` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2732` n `125` status `ready` deltaP `3.7171` edge `-0.017` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.4446` n `135` status `ready` deltaP `0.8195` edge `-0.0326` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2663` n `125` status `ready` deltaP `-10.0378` edge `-0.0362` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4613` n `135` status `ready` deltaP `-1.6711` edge `-0.0758` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.9578` n `135` status `ready` deltaP `-3.1293` edge `-0.0605` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.8406` n `113` status `ready` deltaP `-2.2462` edge `-0.1199` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.1577` n `125` status `ready` deltaP `-9.0854` edge `-0.2249` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5438` n `113` status `ready` deltaP `-18.9927` edge `-0.1534` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.0661` n `113` status `ready` deltaP `-4.9011` edge `-0.3157` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.8871` n `125` status `ready` deltaP `-8.5512` edge `-0.3562` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
