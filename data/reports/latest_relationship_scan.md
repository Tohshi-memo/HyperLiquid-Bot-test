# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T08:37:28.960126+00:00`
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

- `market_context_high->unknown_4h` score `18.3319` n `127` status `ready` deltaP `-2.5362` edge `1.5781` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6037` n `113` status `ready` deltaP `28.4445` edge `0.1548` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1424` n `113` status `ready` deltaP `21.7029` edge `0.0308` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0876` n `127` status `ready` deltaP `8.827` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0211` n `137` status `ready` deltaP `5.493` edge `0.0019` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3114` n `137` status `ready` deltaP `1.7877` edge `0.0122` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3149` n `137` status `ready` deltaP `5.8667` edge `-0.0003` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.5642` n `113` status `ready` deltaP `11.1296` edge `-0.0183` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.6473` n `127` status `ready` deltaP `3.2636` edge `0.0472` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6638` n `137` status `ready` deltaP `-2.2368` edge `-0.005` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.275` n `127` status `ready` deltaP `3.6213` edge `-0.0166` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.4278` n `137` status `ready` deltaP `0.8141` edge `-0.0304` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.3023` n `127` status `ready` deltaP `-10.6551` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-3.8538` n `137` status `ready` deltaP `-2.3308` edge `-0.077` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.9227` n `137` status `ready` deltaP `-3.1547` edge `-0.0574` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.7824` n `113` status `ready` deltaP `-2.0726` edge `-0.1136` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.0932` n `127` status `ready` deltaP `-8.4453` edge `-0.2209` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5313` n `113` status `ready` deltaP `-18.9927` edge `-0.1518` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.9528` n `113` status `ready` deltaP `-4.5539` edge `-0.3035` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9139` n `127` status `ready` deltaP `-9.1559` edge `-0.3556` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
