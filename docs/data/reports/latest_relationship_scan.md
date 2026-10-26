# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T05:22:33.512622+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7254`

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

- `market_context_high->unknown_4h` score `26.1458` n `114` status `ready` deltaP `-2.8723` edge `2.2315` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.4456` n `108` status `ready` deltaP `26.2731` edge `0.149` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1685` n `108` status `ready` deltaP `22.2801` edge `0.0303` maxDD `-1.2451`
- `market_context_high->fx_1h` score `-0.0193` n `126` status `ready` deltaP `4.7168` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0506` n `114` status `ready` deltaP `7.1299` edge `0.0081` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3289` n `126` status `ready` deltaP `-0.2542` edge `0.0096` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3397` n `126` status `ready` deltaP `5.4795` edge `-0.0009` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.5388` n `114` status `ready` deltaP `1.4121` edge `0.0444` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6044` n `126` status `ready` deltaP `-1.1834` edge `-0.0044` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.706` n `108` status `ready` deltaP `10.5324` edge `-0.0325` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3393` n `126` status `ready` deltaP `2.5307` edge `-0.0305` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.3632` n `114` status `ready` deltaP `2.5112` edge `-0.0205` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1473` n `114` status `ready` deltaP `-7.7048` edge `-0.0365` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3815` n `126` status `ready` deltaP `-0.0309` edge `-0.0765` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.487` n `126` status `ready` deltaP `-1.9034` edge `-0.0577` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.5396` n `108` status `ready` deltaP `-2.0255` edge `-0.1359` maxDD `-26.608`
- `market_context_high->commodity_24h` score `-5.9211` n `108` status `ready` deltaP `-17.4768` edge `-0.141` maxDD `-21.1286`
- `market_context_high->crypto_major_4h` score `-6.6617` n `114` status `ready` deltaP `-13.198` edge `-0.2621` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-7.4187` n `108` status `ready` deltaP `-4.8032` edge `-0.3824` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-9.2305` n `114` status `ready` deltaP `-9.9192` edge `-0.3911` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
