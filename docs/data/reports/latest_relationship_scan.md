# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T17:22:31.894672+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10174`

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

- `market_context_high->equity_24h` score `5.7199` n `34` status `ready` deltaP `9.5282` edge `0.6536` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9404` n `34` status `ready` deltaP `4.1463` edge `0.1928` maxDD `-1.6995`
- `market_context_high->fx_24h` score `0.7995` n `34` status `ready` deltaP `11.7238` edge `-0.0009` maxDD `-0.1843`
- `market_context_high->index_24h` score `0.7834` n `34` status `ready` deltaP `8.8031` edge `0.088` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.2598` n `88` status `ready` deltaP `4.6952` edge `0.0147` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5662` n `88` status `ready` deltaP `-0.4559` edge `-0.0013` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6728` n `88` status `ready` deltaP `2.1757` edge `-0.003` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9262` n `88` status `ready` deltaP `-2.8409` edge `0.0108` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9854` n `88` status `ready` deltaP `-7.3557` edge `0.0058` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9971` n `88` status `ready` deltaP `-0.5959` edge `0.0145` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6073` n `88` status `ready` deltaP `-7.5054` edge `0.0286` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.935` n `88` status `ready` deltaP `0.4831` edge `-0.0534` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0941` n `88` status `ready` deltaP `-6.3054` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.2407` n `34` status `ready` deltaP `-5.0347` edge `-0.1984` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1775` n `88` status `ready` deltaP `-5.2599` edge `-0.11` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-5.8637` n `34` status `ready` deltaP `-5.8313` edge `0.0133` maxDD `-30.3789`
- `market_context_high->equity_4h` score `-6.6036` n `88` status `ready` deltaP `-1.2195` edge `-0.161` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2806` n `88` status `ready` deltaP `1.0255` edge `-0.2684` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-11.1873` n `34` status `ready` deltaP `-22.641` edge `-0.2719` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
