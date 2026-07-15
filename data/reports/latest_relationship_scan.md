# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T09:22:25.353074+00:00`
- Price records: `672`
- Market context records: `6803`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11656`

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

- `market_context_high->unknown_24h` score `0.8258` n `176` status `ready` deltaP `-1.5467` edge `0.4914` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2903` n `176` status `ready` deltaP `9.7065` edge `0.1463` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3319` n `185` status `ready` deltaP `6.0495` edge `0.018` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4449` n `185` status `ready` deltaP `-1.2348` edge `-0.0003` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4525` n `185` status `ready` deltaP `3.3468` edge `0.0164` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6738` n `185` status `ready` deltaP `-1.3764` edge `-0.0089` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6782` n `185` status `ready` deltaP `-2.1581` edge `-0.001` maxDD `-0.7249`
- `market_context_high->metal_1h` score `-0.7132` n `185` status `ready` deltaP `-5.2929` edge `-0.0033` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.3265` n `185` status `ready` deltaP `1.9332` edge `-0.019` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3817` n `185` status `ready` deltaP `4.7602` edge `-0.0025` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4173` n `185` status `ready` deltaP `-2.5981` edge `-0.0154` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5767` n `185` status `ready` deltaP `-5.4426` edge `-0.005` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6344` n `185` status `ready` deltaP `1.8375` edge `-0.0258` maxDD `-6.3458`
- `market_context_high->metal_4h` score `-2.7421` n `185` status `ready` deltaP `-5.7045` edge `-0.0152` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2377` n `185` status `ready` deltaP `-0.5051` edge `-0.079` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4144` n `185` status `ready` deltaP `-1.3645` edge `-0.0703` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4785` n `185` status `ready` deltaP `-14.1175` edge `0.0408` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.502` n `176` status `ready` deltaP `-9.7853` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.9261` n `185` status `ready` deltaP `-0.81` edge `-0.1723` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.4576` n `176` status `ready` deltaP `-20.2336` edge `-0.2291` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
