# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T19:22:25.363220+00:00`
- Price records: `672`
- Market context records: `6633`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.3231` n `203` status `ready` deltaP `-5.6407` edge `0.3213` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.5974` n `188` status `ready` deltaP `-1.2368` edge `0.4535` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5343` n `188` status `ready` deltaP `9.9665` edge `0.1649` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1025` n `203` status `ready` deltaP `8.8139` edge `0.0487` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1158` n `203` status `ready` deltaP `6.2011` edge `0.0421` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2306` n `203` status `ready` deltaP `3.0854` edge `0.0006` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4844` n `203` status `ready` deltaP `0.6711` edge `0.0052` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6537` n `203` status `ready` deltaP `-1.1393` edge `-0.0079` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7577` n `203` status `ready` deltaP `-15.8814` edge `0.2833` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-0.8023` n `203` status `ready` deltaP `3.5014` edge `0.0125` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.809` n `203` status `ready` deltaP `10.7788` edge `0.0124` maxDD `-5.7046`
- `market_context_high->crypto_major_4h` score `-1.1024` n `203` status `ready` deltaP `10.2622` edge `0.1217` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1401` n `203` status `ready` deltaP `-3.2071` edge `0.0005` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.3823` n `203` status `ready` deltaP `-1.3119` edge `-0.019` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4984` n `203` status `ready` deltaP `7.1075` edge `0.1007` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.5054` n `203` status `ready` deltaP `4.2322` edge `0.0` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9386` n `203` status `ready` deltaP `1.2173` edge `0.0294` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3671` n `203` status `ready` deltaP `8.9834` edge `0.0031` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.4428` n `188` status `ready` deltaP `-2.6872` edge `0.0268` maxDD `-21.8682`
- `market_context_high->fx_24h` score `-6.1191` n `188` status `ready` deltaP `-9.9407` edge `-0.0054` maxDD `-10.3939`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
