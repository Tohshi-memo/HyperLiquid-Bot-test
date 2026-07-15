# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T10:07:29.534811+00:00`
- Price records: `672`
- Market context records: `6806`
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

- `market_context_high->unknown_24h` score `0.8195` n `176` status `ready` deltaP `-1.5467` edge `0.4906` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.324` n `176` status `ready` deltaP `10.0537` edge `0.1468` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2934` n `188` status `ready` deltaP `6.3798` edge `0.019` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4094` n `188` status `ready` deltaP `3.7202` edge `0.0175` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4384` n `188` status `ready` deltaP `-1.0798` edge `-0.0005` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6442` n `188` status `ready` deltaP `-1.032` edge `-0.0074` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7035` n `188` status `ready` deltaP `-2.5608` edge `-0.0013` maxDD `-0.7461`
- `market_context_high->metal_1h` score `-0.7755` n `188` status `ready` deltaP `-5.816` edge `-0.0046` maxDD `-1.4839`
- `market_context_high->equity_1h` score `-1.3401` n `188` status `ready` deltaP `1.8092` edge `-0.0193` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3817` n `185` status `ready` deltaP `4.7602` edge `-0.0025` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4025` n `185` status `ready` deltaP `-2.5981` edge `-0.0135` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6461` n `185` status `ready` deltaP `1.8375` edge `-0.0273` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.6785` n `188` status `ready` deltaP `-6.1154` edge `-0.009` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.789` n `185` status `ready` deltaP `-5.857` edge `-0.0202` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2745` n `185` status `ready` deltaP `-0.6576` edge `-0.0827` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4652` n `185` status `ready` deltaP `-1.517` edge `-0.0758` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4941` n `185` status `ready` deltaP `-14.1175` edge `0.0395` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4984` n `176` status `ready` deltaP `-9.7853` edge `-0.006` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.9861` n `185` status `ready` deltaP `-0.81` edge `-0.18` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.526` n `176` status `ready` deltaP `-20.7545` edge `-0.2344` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
