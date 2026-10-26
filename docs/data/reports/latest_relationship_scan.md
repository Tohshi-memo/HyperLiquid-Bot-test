# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T09:37:31.271495+00:00`
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

- `market_context_high->unknown_4h` score `18.2681` n `130` status `ready` deltaP `-1.9841` edge `1.5691` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.599` n `113` status `ready` deltaP `28.4445` edge `0.1542` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1256` n `141` status `ready` deltaP `6.6272` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1188` n `130` status `ready` deltaP `9.2167` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_24h` score `0.1024` n `113` status `ready` deltaP `21.0085` edge `0.0303` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2644` n `141` status `ready` deltaP `6.6739` edge `0.0008` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.378` n `141` status `ready` deltaP `1.135` edge `0.011` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5377` n `113` status `ready` deltaP `11.1296` edge `-0.0149` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.593` n `141` status `ready` deltaP `-1.1742` edge `-0.003` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.6007` n `130` status `ready` deltaP `3.8602` edge `0.0471` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.289` n `141` status `ready` deltaP `1.9227` edge `-0.02` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.3166` n `130` status `ready` deltaP `2.7017` edge `-0.0158` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.3242` n `130` status `ready` deltaP `-11.2406` edge `-0.0356` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3451` n `141` status `ready` deltaP `-1.0564` edge `-0.065` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3598` n `141` status `ready` deltaP `-2.0969` edge `-0.0401` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.7309` n `113` status `ready` deltaP `-2.0726` edge `-0.107` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.0079` n `130` status `ready` deltaP `-8.0042` edge `-0.2129` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.4973` n `113` status `ready` deltaP `-18.8191` edge `-0.1486` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.7752` n `113` status `ready` deltaP `-4.033` edge `-0.2842` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-13.6691` n `130` status `ready` deltaP `-9.7232` edge `-0.3481` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
