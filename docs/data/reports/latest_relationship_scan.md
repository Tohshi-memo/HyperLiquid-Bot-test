# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T01:52:28.748050+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8004`

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

- `market_context_high->unknown_4h` score `87.5227` n `153` status `ready` deltaP `1.3221` edge `7.3183` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8872` n `153` status `ready` deltaP `1.6242` edge `1.7787` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.3153` n `153` status `ready` deltaP `8.8636` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.2833` n `153` status `ready` deltaP `11.1539` edge `0.0091` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.1628` n `115` status `ready` deltaP `22.8905` edge `0.1309` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.0857` n `115` status `ready` deltaP `15.6537` edge `0.0085` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1221` n `153` status `ready` deltaP `8.4801` edge `0.007` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.1635` n `153` status `ready` deltaP `3.0508` edge `0.0161` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1953` n `115` status `ready` deltaP `15.9882` edge `0.0256` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3473` n `153` status `ready` deltaP `6.6684` edge `0.0495` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6203` n `153` status `ready` deltaP `-0.5861` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.9052` n `153` status `ready` deltaP `4.5331` edge `0.0118` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9352` n `153` status `ready` deltaP `7.8172` edge `-0.001` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8385` n `153` status `ready` deltaP `1.0058` edge `-0.0148` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0186` n `153` status `ready` deltaP `-0.4256` edge `-0.0075` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4237` n `153` status `ready` deltaP `-6.3845` edge `-0.0251` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.6192` n `115` status `ready` deltaP `-2.9538` edge `-0.0868` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.6869` n `153` status `ready` deltaP `-0.9156` edge `-0.0908` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-5.8325` n `115` status `ready` deltaP `-12.0202` edge `-0.1086` maxDD `-24.0547`
- `market_context_high->equity_24h` score `-6.791` n `115` status `ready` deltaP `-7.2956` edge `-0.2787` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
