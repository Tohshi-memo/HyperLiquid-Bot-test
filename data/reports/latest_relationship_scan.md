# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T04:37:29.223861+00:00`
- Price records: `672`
- Market context records: `6782`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `market_context_high->unknown_24h` score `0.916` n `176` status `ready` deltaP `-1.0259` edge `0.4995` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0429` n `176` status `ready` deltaP `8.144` edge `0.1361` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.041` n `180` status `ready` deltaP `7.7745` edge `0.0289` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1992` n `180` status `ready` deltaP `5.1031` edge `0.0258` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3724` n `180` status `ready` deltaP `0.0233` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5889` n `180` status `ready` deltaP `-0.7917` edge `0.0012` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6541` n `180` status `ready` deltaP `-0.8782` edge `-0.0097` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7574` n `180` status `ready` deltaP `-5.9814` edge `-0.0047` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1256` n `180` status `ready` deltaP `3.33` edge `-0.0133` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.287` n `176` status `ready` deltaP `5.6818` edge `-0.0149` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2912` n `176` status `ready` deltaP `6.3193` edge `-0.0013` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5271` n `176` status `ready` deltaP `-3.4507` edge `-0.0238` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5573` n `180` status `ready` deltaP `-5.4258` edge `-0.0035` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.625` n `176` status `ready` deltaP `-6.0144` edge `-0.0104` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.8468` n `176` status `ready` deltaP `2.5915` edge `-0.0508` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9735` n `176` status `ready` deltaP `1.1502` edge `-0.0487` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.3031` n `176` status `ready` deltaP `-14.1907` edge `0.0559` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2722` n `176` status `ready` deltaP `2.5499` edge `-0.1378` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4121` n `176` status `ready` deltaP `-8.9173` edge `-0.0046` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.9865` n `176` status `ready` deltaP `-16.935` edge `-0.1907` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
