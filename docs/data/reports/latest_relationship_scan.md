# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T09:52:34.280489+00:00`
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

- `market_context_high->unknown_4h` score `18.4531` n `130` status `ready` deltaP `-1.8316` edge `1.5835` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5967` n `113` status `ready` deltaP `28.4445` edge `0.1539` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1384` n `142` status `ready` deltaP `6.7871` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1054` n `130` status `ready` deltaP `9.0643` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_24h` score `0.0918` n `113` status `ready` deltaP `20.8349` edge `0.0301` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2524` n `142` status `ready` deltaP `6.8588` edge `0.0011` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.35` n `142` status `ready` deltaP `1.4696` edge `0.0111` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5322` n `113` status `ready` deltaP `11.1296` edge `-0.0142` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.5787` n `142` status `ready` deltaP `-0.9594` edge `-0.0026` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.6213` n `130` status `ready` deltaP `3.7078` edge `0.0464` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.2783` n `142` status `ready` deltaP `2.1127` edge `-0.0199` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.3158` n `130` status `ready` deltaP `2.7017` edge `-0.0157` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-2.3121` n `142` status `ready` deltaP `-0.8265` edge `-0.0623` maxDD `-12.2891`
- `market_context_high->index_4h` score `-2.3211` n `130` status `ready` deltaP `-11.2406` edge `-0.0352` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-2.3889` n `142` status `ready` deltaP `-2.4016` edge `-0.0418` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.7192` n `113` status `ready` deltaP `-2.0726` edge `-0.1055` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.997` n `130` status `ready` deltaP `-8.0042` edge `-0.2115` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.495` n `113` status `ready` deltaP `-18.8191` edge `-0.1483` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.7432` n `113` status `ready` deltaP `-4.033` edge `-0.2801` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-13.6499` n `130` status `ready` deltaP `-9.7232` edge `-0.3465` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
