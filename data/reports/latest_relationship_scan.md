# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T06:07:26.388995+00:00`
- Price records: `672`
- Market context records: `6788`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11670`

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

- `market_context_high->unknown_24h` score `0.8828` n `176` status `ready` deltaP `-1.1995` edge `0.4964` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0765` n `176` status `ready` deltaP `8.144` edge `0.1389` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2408` n `185` status `ready` deltaP `6.6483` edge `0.0216` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.402` n `185` status `ready` deltaP `-0.4863` edge `0.0002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4117` n `185` status `ready` deltaP `3.6462` edge `0.0178` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.6634` n `185` status `ready` deltaP `-2.0084` edge `-0.0001` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.6878` n `185` status `ready` deltaP `-1.5261` edge `-0.0097` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7234` n `185` status `ready` deltaP `-5.4426` edge `-0.0036` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.2834` n `185` status `ready` deltaP `2.2326` edge `-0.0174` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3292` n `176` status `ready` deltaP `5.7096` edge `-0.0021` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.3564` n `176` status `ready` deltaP `4.7672` edge `-0.0177` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4711` n `176` status `ready` deltaP `-2.6885` edge `-0.0217` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6078` n `185` status `ready` deltaP `-5.5923` edge `-0.0066` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.5502` n `176` status `ready` deltaP `-5.0998` edge `-0.0069` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.9755` n `176` status `ready` deltaP `1.6768` edge `-0.0612` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0` n `176` status `ready` deltaP `1.1502` edge `-0.0521` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2669` n `176` status `ready` deltaP `-14.0383` edge `0.0579` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.3915` n `176` status `ready` deltaP `1.6353` edge `-0.147` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.467` n `176` status `ready` deltaP `-9.4381` edge `-0.0057` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.1187` n `176` status `ready` deltaP `-17.9767` edge `-0.2007` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
