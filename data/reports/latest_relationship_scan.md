# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T09:37:25.397871+00:00`
- Price records: `672`
- Market context records: `6804`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8226` n `176` status `ready` deltaP `-1.5467` edge `0.491` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3065` n `176` status `ready` deltaP `9.8801` edge `0.1465` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3125` n `186` status `ready` deltaP `6.112` edge `0.0192` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4367` n `186` status `ready` deltaP `3.4238` edge `0.0172` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4589` n `186` status `ready` deltaP `-1.4906` edge `-0.0004` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6653` n `186` status `ready` deltaP `-1.2588` edge `-0.0086` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6718` n `186` status `ready` deltaP `-2.0346` edge `-0.001` maxDD `-0.7249`
- `market_context_high->metal_1h` score `-0.7217` n `186` status `ready` deltaP `-5.3699` edge `-0.0034` maxDD `-1.2663`
- `market_context_high->equity_1h` score `-1.3135` n `186` status `ready` deltaP `2.0218` edge `-0.0185` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3738` n `185` status `ready` deltaP `4.9126` edge `-0.0025` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.411` n `185` status `ready` deltaP `-2.5981` edge `-0.0146` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6104` n `186` status `ready` deltaP `-5.6693` edge `-0.0063` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6383` n `185` status `ready` deltaP `1.8375` edge `-0.0263` maxDD `-6.3458`
- `market_context_high->metal_4h` score `-2.7633` n `185` status `ready` deltaP `-5.857` edge `-0.0169` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2581` n `185` status `ready` deltaP `-0.6576` edge `-0.0806` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4379` n `185` status `ready` deltaP `-1.517` edge `-0.0723` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4845` n `185` status `ready` deltaP `-14.1175` edge `0.0403` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5008` n `176` status `ready` deltaP `-9.7853` edge `-0.0062` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.9471` n `185` status `ready` deltaP `-0.81` edge `-0.175` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.4814` n `176` status `ready` deltaP `-20.4072` edge `-0.231` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
