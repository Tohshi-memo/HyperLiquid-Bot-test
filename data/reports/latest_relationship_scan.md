# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T12:37:30.340649+00:00`
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

- `market_context_high->unknown_4h` score `56.0929` n `88` status `ready` deltaP `7.6774` edge `4.668` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8398` n `88` status `ready` deltaP `33.0412` edge `2.9235` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4548` n `88` status `ready` deltaP `25.8783` edge `0.3283` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.7322` n `88` status `ready` deltaP `22.7745` edge `0.9643` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3602` n `88` status `ready` deltaP `17.9435` edge `-0.0343` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3676` n `88` status `ready` deltaP `2.3884` edge `0.0052` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.3479` edge `0.0107` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.4816` n `88` status `ready` deltaP `2.7993` edge `0.0302` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6865` n `88` status `ready` deltaP `2.4806` edge `-0.0068` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0423` n `88` status `ready` deltaP `-8.2539` edge `0.0045` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1022` n `88` status `ready` deltaP `-1.3581` edge `0.0061` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3008` n `88` status `ready` deltaP `-13.9085` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7336` n `88` status `ready` deltaP `-8.703` edge `0.0204` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8805` n `88` status `ready` deltaP `1.2316` edge `-0.0514` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9927` n `88` status `ready` deltaP `-4.4762` edge `-0.0075` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.3744` n `88` status `ready` deltaP `-2.3397` edge `-0.0223` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.0747` n `88` status `ready` deltaP `-4.212` edge `-0.1038` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.903` n `88` status `ready` deltaP `-0.7622` edge `-0.189` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.638` n `88` status `ready` deltaP `3.3121` edge `-0.2301` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.25` n `88` status `ready` deltaP `-23.4698` edge `-0.062` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
