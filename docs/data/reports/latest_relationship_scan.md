# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T23:41:51.892001+00:00`
- Price records: `672`
- Market context records: `2508`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.2299` n `121` status `ready` deltaP `19.6869` edge `0.3374` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.6128` n `150` status `ready` deltaP `21.3902` edge `0.5097` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8473` n `150` status `ready` deltaP `17.6565` edge `0.3839` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1557` n `121` status `ready` deltaP `11.9003` edge `0.5863` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.9891` n `150` status `ready` deltaP `11.315` edge `0.1953` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.8167` n `158` status `ready` deltaP `7.7996` edge `0.1348` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5575` n `158` status `ready` deltaP `7.6158` edge `0.1151` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1213` n `121` status `ready` deltaP `1.7533` edge `0.6996` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0168` n `121` status `ready` deltaP `3.6716` edge `0.075` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1553` n `121` status `ready` deltaP `18.0685` edge `0.0193` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1726` n `150` status `ready` deltaP `6.3394` edge `0.0275` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2936` n `158` status `ready` deltaP `1.7149` edge `0.0044` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.3684` n `158` status `ready` deltaP `2.4843` edge `0.0247` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4133` n `158` status `ready` deltaP `3.3825` edge `0.0123` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5092` n `158` status `ready` deltaP `0.5647` edge `0.0069` maxDD `-3.0759`
- `market_context_high->index_1h` score `-0.5478` n `158` status `ready` deltaP `-0.1421` edge `0.0047` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6646` n `150` status `ready` deltaP `-1.2947` edge `0.0094` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8125` n `158` status `ready` deltaP `0.3828` edge `0.0136` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.815` n `121` status `ready` deltaP `4.0103` edge `0.0052` maxDD `-2.5804`
- `market_context_high->commodity_4h` score `-1.1282` n `150` status `ready` deltaP `2.7033` edge `0.0316` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
