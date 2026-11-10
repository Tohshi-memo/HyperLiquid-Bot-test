# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T12:22:31.852642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11136`

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

- `market_context_high->unknown_4h` score `56.1241` n `88` status `ready` deltaP `7.6774` edge `4.6706` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8458` n `88` status `ready` deltaP `33.0412` edge `2.924` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4572` n `88` status `ready` deltaP `25.8783` edge `0.3285` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.6873` n `88` status `ready` deltaP `22.6012` edge `0.9597` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3199` n `88` status `ready` deltaP `17.7702` edge `-0.0365` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3676` n `88` status `ready` deltaP `2.3884` edge `0.0052` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.43` n `88` status `ready` deltaP `3.1982` edge `0.0105` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.4754` n `88` status `ready` deltaP `2.7993` edge `0.031` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6968` n `88` status `ready` deltaP `2.3281` edge `-0.0071` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0509` n `88` status `ready` deltaP `-8.4036` edge `0.0044` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1156` n `88` status `ready` deltaP `-1.5105` edge `0.0054` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3008` n `88` status `ready` deltaP `-13.9085` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.746` n `88` status `ready` deltaP `-8.8527` edge `0.0198` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8867` n `88` status `ready` deltaP `1.2316` edge `-0.0522` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0006` n `88` status `ready` deltaP `-4.6286` edge `-0.0075` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.3919` n `88` status `ready` deltaP `-2.513` edge `-0.0226` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.0934` n `88` status `ready` deltaP `-4.3617` edge `-0.1052` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.9548` n `88` status `ready` deltaP `-0.9146` edge `-0.1923` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.6646` n `88` status `ready` deltaP `3.1597` edge `-0.2313` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2464` n `88` status `ready` deltaP `-23.4698` edge `-0.0617` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
