# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T02:37:31.354683+00:00`
- Price records: `672`
- Market context records: `6773`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `market_context_high->unknown_24h` score `1.0296` n `176` status `ready` deltaP `0.363` edge `0.5048` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0093` n `176` status `ready` deltaP `8.144` edge `0.1333` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0029` n `176` status `ready` deltaP `7.9512` edge `0.0326` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2167` n `176` status `ready` deltaP `4.8993` edge `0.0257` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3968` n `176` status `ready` deltaP `-0.4151` edge `0.0004` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5892` n `176` status `ready` deltaP `0.1463` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6512` n `176` status `ready` deltaP `-1.7658` edge `-0.0003` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7253` n `176` status `ready` deltaP `-5.4403` edge `-0.0042` maxDD `-1.2017`
- `market_context_high->fx_4h` score `-1.2161` n `176` status `ready` deltaP `7.5388` edge `0.0002` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2515` n `176` status `ready` deltaP `6.1391` edge `-0.0134` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2814` n `176` status `ready` deltaP `2.5075` edge `-0.0208` maxDD `-3.8827`
- `market_context_high->commodity_4h` score `-1.4836` n `176` status `ready` deltaP `-2.6885` edge `-0.0233` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7297` n `176` status `ready` deltaP `-6.7263` edge `-0.0092` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.6865` n `176` status `ready` deltaP `3.0488` edge `-0.0333` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.7007` n `176` status `ready` deltaP `-6.9291` edge `-0.014` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.861` n `176` status `ready` deltaP `1.3026` edge `-0.0353` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.5121` n `176` status `ready` deltaP `-15.2578` edge `0.0456` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2268` n `176` status `ready` deltaP `2.7023` edge `-0.133` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2837` n `176` status `ready` deltaP `-7.702` edge `-0.002` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.7918` n `176` status `ready` deltaP `-15.5461` edge `-0.175` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
