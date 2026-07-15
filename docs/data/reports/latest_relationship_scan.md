# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T07:07:29.409990+00:00`
- Price records: `672`
- Market context records: `6793`
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

- `market_context_high->unknown_24h` score `0.8703` n `176` status `ready` deltaP `-1.1995` edge `0.4948` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1481` n `176` status `ready` deltaP `8.6648` edge `0.1414` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2923` n `185` status `ready` deltaP `6.3489` edge `0.0193` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3943` n `185` status `ready` deltaP `-0.3366` edge `0.0002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4513` n `185` status `ready` deltaP `3.3468` edge `0.0165` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.6556` n `185` status `ready` deltaP `-1.8587` edge `-0.0001` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.6956` n `185` status `ready` deltaP `-1.6758` edge `-0.0097` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7117` n `185` status `ready` deltaP `-5.2929` edge `-0.0031` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.275` n `185` status `ready` deltaP `2.2326` edge `-0.0167` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3614` n `178` status `ready` deltaP `5.135` edge `-0.0024` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.398` n `178` status `ready` deltaP `4.1758` edge `-0.0191` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4675` n `178` status `ready` deltaP `-2.6788` edge `-0.0213` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5479` n `185` status `ready` deltaP `-5.1432` edge `-0.0046` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6249` n `178` status `ready` deltaP `-5.2034` edge `-0.0064` maxDD `-5.3013`
- `market_context_high->crypto_major_4h` score `-2.9972` n `178` status `ready` deltaP `1.5587` edge `-0.0632` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0039` n `178` status `ready` deltaP `1.0448` edge `-0.0519` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2899` n `178` status `ready` deltaP `-13.8308` edge `0.0546` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.4151` n `178` status `ready` deltaP `1.5107` edge `-0.1492` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4833` n `176` status `ready` deltaP `-9.6117` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.2195` n `176` status `ready` deltaP `-18.6711` edge `-0.209` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
