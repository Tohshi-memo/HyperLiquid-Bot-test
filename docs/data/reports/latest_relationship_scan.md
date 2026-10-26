# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T10:37:42.339565+00:00`
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

- `market_context_high->unknown_4h` score `19.0956` n `133` status `ready` deltaP `-1.4499` edge `1.6345` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5928` n `113` status `ready` deltaP `28.4445` edge `0.1534` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1291` n `145` status `ready` deltaP `6.7014` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0616` n `113` status `ready` deltaP `20.314` edge `0.0297` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0456` n `133` status `ready` deltaP `8.3624` edge `0.0079` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.2523` n `145` status `ready` deltaP `6.8459` edge `0.0012` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3055` n `145` status `ready` deltaP `1.9058` edge `0.0119` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5104` n `113` status `ready` deltaP `11.1296` edge `-0.0114` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5738` n `133` status `ready` deltaP `4.2569` edge `0.0467` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.606` n `145` status `ready` deltaP `-1.4247` edge `-0.003` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2268` n `133` status `ready` deltaP `3.9336` edge `-0.0125` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.2884` n `145` status `ready` deltaP `2.1144` edge `-0.0212` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2254` n `133` status `ready` deltaP `-9.8352` edge `-0.0323` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3262` n `145` status `ready` deltaP `-1.2482` edge `-0.0613` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4484` n `145` status `ready` deltaP `-2.7504` edge `-0.0471` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.6779` n `113` status `ready` deltaP `-2.0726` edge `-0.1002` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.7989` n `133` status `ready` deltaP `-6.6856` edge `-0.1949` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.4887` n `113` status `ready` deltaP `-18.8191` edge `-0.1475` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.6097` n `113` status `ready` deltaP `-3.6858` edge `-0.2653` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.6643` n `133` status `ready` deltaP `-8.3004` edge `-0.3293` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
