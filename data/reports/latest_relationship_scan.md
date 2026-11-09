# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T17:52:26.131773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `4.5494` n `35` status `ready` deltaP `10.4415` edge `0.7541` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.6854` n `35` status `ready` deltaP `2.5496` edge `0.1822` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9075` n `35` status `ready` deltaP `9.4643` edge `0.0995` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.5352` n `35` status `ready` deltaP `9.9703` edge `-0.0051` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.2622` n `88` status `ready` deltaP `4.6952` edge `0.0145` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5787` n `88` status `ready` deltaP `-0.6056` edge `-0.0019` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7042` n `88` status `ready` deltaP `1.8708` edge `-0.005` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.953` n `88` status `ready` deltaP `-3.1458` edge `0.0094` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0018` n `88` status `ready` deltaP `-0.5959` edge `0.0139` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0041` n `88` status `ready` deltaP `-7.6551` edge `0.0054` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6338` n `88` status `ready` deltaP `-7.6551` edge `0.0262` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9514` n `88` status `ready` deltaP `0.4831` edge `-0.0555` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.102` n `88` status `ready` deltaP `-6.4579` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.1385` n `35` status `ready` deltaP `-3.9533` edge `-0.1925` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1916` n `88` status `ready` deltaP `-5.2599` edge `-0.1118` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-6.7011` n `35` status `ready` deltaP `-6.3244` edge `-0.0193` maxDD `-32.7569`
- `market_context_high->equity_4h` score `-6.8476` n `88` status `ready` deltaP `-1.5244` edge `-0.1793` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3492` n `88` status `ready` deltaP `0.8731` edge `-0.2731` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.4755` n `35` status `ready` deltaP `-20.7193` edge `-0.2254` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
