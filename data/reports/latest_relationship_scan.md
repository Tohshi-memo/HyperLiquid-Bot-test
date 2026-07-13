# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T18:37:27.485251+00:00`
- Price records: `672`
- Market context records: `6630`
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

- `market_context_high->unknown_1h` score `2.2511` n `203` status `ready` deltaP `-5.7904` edge `0.3163` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.9733` n `185` status `ready` deltaP `-0.9623` edge `0.4705` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.4287` n `185` status `ready` deltaP `9.4576` edge `0.1595` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0612` n `203` status `ready` deltaP `8.8139` edge `0.0434` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1985` n `203` status `ready` deltaP `6.0514` edge `0.0362` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2547` n `203` status `ready` deltaP `2.6363` edge `0.0005` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4937` n `203` status `ready` deltaP `0.5214` edge `0.005` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6537` n `203` status `ready` deltaP `-1.1393` edge `-0.0079` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8239` n `203` status `ready` deltaP `10.6264` edge `0.0115` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8418` n `203` status `ready` deltaP `3.202` edge `0.0112` maxDD `-3.8827`
- `market_context_high->unknown_4h` score `-0.8553` n `203` status `ready` deltaP `-16.1863` edge `0.2772` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-1.0981` n `203` status `ready` deltaP `-2.758` edge `0.001` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.2175` n `203` status `ready` deltaP `9.8049` edge `0.11` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.3518` n `203` status `ready` deltaP `-1.1595` edge `-0.0161` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.5299` n `203` status `ready` deltaP `3.7749` edge `-0.0001` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.622` n `203` status `ready` deltaP `6.6502` edge `0.0879` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-1.974` n `203` status `ready` deltaP `0.76` edge `0.0279` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4211` n `203` status `ready` deltaP `8.9834` edge `-0.0014` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.1199` n `185` status `ready` deltaP `-2.1697` edge `0.0316` maxDD `-20.2155`
- `market_context_high->fx_24h` score `-6.0259` n `185` status `ready` deltaP `-9.4145` edge `-0.0044` maxDD `-10.133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
