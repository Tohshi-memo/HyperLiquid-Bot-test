# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T09:07:31.430942+00:00`
- Price records: `672`
- Market context records: `6802`
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

- `market_context_high->unknown_24h` score `0.8297` n `176` status `ready` deltaP `-1.5467` edge `0.4919` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2728` n `176` status `ready` deltaP `9.5329` edge `0.146` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3019` n `185` status `ready` deltaP `6.1992` edge `0.0195` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4261` n `185` status `ready` deltaP `3.4965` edge `0.0176` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4441` n `185` status `ready` deltaP `-1.2348` edge `-0.0002` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6696` n `185` status `ready` deltaP `-2.0084` edge `-0.0009` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.6824` n `185` status `ready` deltaP `-1.5261` edge `-0.009` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7047` n `185` status `ready` deltaP `-5.1432` edge `-0.0032` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.3086` n `185` status `ready` deltaP `2.0829` edge `-0.0185` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3896` n `185` status `ready` deltaP `4.6077` edge `-0.0025` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4227` n `185` status `ready` deltaP `-2.5981` edge `-0.0161` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5599` n `185` status `ready` deltaP `-5.2929` edge `-0.0046` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6305` n `185` status `ready` deltaP `1.8375` edge `-0.0253` maxDD `-6.3458`
- `market_context_high->metal_4h` score `-2.7194` n `185` status `ready` deltaP `-5.5521` edge `-0.0133` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2126` n `185` status `ready` deltaP `-0.3527` edge `-0.0768` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.387` n `185` status `ready` deltaP `-1.2121` edge `-0.0678` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4701` n `185` status `ready` deltaP `-14.1175` edge `0.0415` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5032` n `176` status `ready` deltaP `-9.7853` edge `-0.0064` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.8955` n `185` status `ready` deltaP `-0.6576` edge `-0.1694` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.4306` n `176` status `ready` deltaP `-20.06` edge `-0.2268` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
