# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T18:37:31.905056+00:00`
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

- `market_context_high->equity_24h` score `6.7406` n `38` status `ready` deltaP `13.3859` edge `1.0154` maxDD `-16.9034`
- `market_context_high->index_24h` score `1.2712` n `38` status `ready` deltaP `11.7487` edge `0.1309` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `0.8154` n `38` status `ready` deltaP `-1.4731` edge `0.1731` maxDD `-1.6995`
- `market_context_high->fx_24h` score `-0.1541` n `38` status `ready` deltaP `4.7843` edge `-0.0168` maxDD `-0.7881`
- `market_context_high->metal_1h` score `-0.2826` n `88` status `ready` deltaP `4.4708` edge `0.0143` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.6062` n `88` status `ready` deltaP `-0.9699` edge `-0.003` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7424` n `88` status `ready` deltaP `1.4961` edge `-0.0074` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9863` n `88` status `ready` deltaP `-3.5163` edge `0.0076` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0105` n `88` status `ready` deltaP `-0.6745` edge `0.0133` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0166` n `88` status `ready` deltaP `-7.8798` edge `0.0053` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.306` n `88` status `ready` deltaP `-13.9794` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6354` n `88` status `ready` deltaP `-7.5808` edge `0.0255` maxDD `-8.1039`
- `market_context_high->metal_24h` score `-1.7614` n `38` status `ready` deltaP `-0.5427` edge `-0.1669` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-1.9782` n `88` status `ready` deltaP `0.2531` edge `-0.0574` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0978` n `88` status `ready` deltaP `-6.3771` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1973` n `88` status `ready` deltaP `-5.1892` edge `-0.113` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.1238` n `88` status `ready` deltaP `-1.9026` edge `-0.1998` maxDD `-25.16`
- `market_context_high->crypto_alt_24h` score `-8.7445` n `38` status `ready` deltaP `-14.7268` edge `-0.1211` maxDD `-33.4213`
- `market_context_high->crypto_alt_4h` score `-9.4272` n `88` status `ready` deltaP `0.4826` edge `-0.277` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-9.6546` n `38` status `ready` deltaP `-8.1729` edge `-0.1405` maxDD `-40.7648`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
