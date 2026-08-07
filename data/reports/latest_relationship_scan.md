# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T21:51:52.324087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `7.5685` n `83` status `ready` deltaP `5.7439` edge `0.8984` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.9227` n `83` status `ready` deltaP `14.188` edge `0.2899` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.6006` n `83` status `ready` deltaP `31.8482` edge `0.0647` maxDD `-2.0783`
- `market_context_high->index_24h` score `1.5647` n `83` status `ready` deltaP `11.5357` edge `0.2048` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.4696` n `105` status `ready` deltaP `15.7143` edge `0.085` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.1185` n `105` status `ready` deltaP `13.4559` edge `0.0378` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.0257` n `105` status `ready` deltaP `6.9775` edge `0.0342` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.409` n `105` status `ready` deltaP `2.9798` edge `-0.0044` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4253` n `105` status `ready` deltaP `-2.2597` edge `-0.0047` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.5023` n `105` status `ready` deltaP `0.5125` edge `-0.0073` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.627` n `105` status `ready` deltaP `3.7166` edge `-0.0017` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.8614` n `105` status `ready` deltaP `-0.0232` edge `-0.0094` maxDD `-2.7373`
- `market_context_high->metal_1h` score `-0.9052` n `105` status `ready` deltaP `-3.0082` edge `-0.0058` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.2534` n `105` status `ready` deltaP `6.4924` edge `-0.014` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.5451` n `105` status `ready` deltaP `-6.9803` edge `-0.0193` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.925` n `83` status `ready` deltaP `9.7996` edge `-0.0627` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.2286` n `105` status `ready` deltaP `-6.1905` edge `-0.0448` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5165` n `83` status `ready` deltaP `-21.1095` edge `-0.1658` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.6337` n `105` status `ready` deltaP `-7.0674` edge `-0.0905` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1462` n `105` status `ready` deltaP `-8.9329` edge `-0.1904` maxDD `-18.6454`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
