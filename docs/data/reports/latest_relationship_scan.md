# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T09:22:24.933508+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11130`

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

- `market_context_high->unknown_4h` score `38.0077` n `88` status `ready` deltaP `7.6774` edge `3.1609` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.189` n `88` status `ready` deltaP `33.0412` edge `2.9526` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5124` n `88` status `ready` deltaP `25.8783` edge `0.3331` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.3426` n `88` status `ready` deltaP `22.6012` edge `0.9155` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0591` n `88` status `ready` deltaP `16.557` edge `-0.06` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3832` n `88` status `ready` deltaP `2.089` edge `0.0052` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4378` n `88` status `ready` deltaP `2.9518` edge `0.0348` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.5174` n `88` status `ready` deltaP `2.3` edge `0.0092` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.8138` n `88` status `ready` deltaP `0.4989` edge `-0.0099` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0859` n `88` status `ready` deltaP `-9.0024` edge `0.0039` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2911` n `88` status `ready` deltaP `-3.3398` edge `-0.0049` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3335` n `88` status `ready` deltaP `-14.5073` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8325` n `88` status `ready` deltaP `-9.4515` edge `0.0127` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0145` n `88` status `ready` deltaP `0.034` edge `-0.0606` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0505` n `88` status `ready` deltaP `-5.5432` edge `-0.0078` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.605` n `88` status `ready` deltaP `-4.5927` edge `-0.0265` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1814` n `88` status `ready` deltaP `-5.1102` edge `-0.1115` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3479` n `88` status `ready` deltaP `-2.439` edge `-0.2149` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2082` n `88` status `ready` deltaP `1.3304` edge `-0.2644` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2812` n `88` status `ready` deltaP `-23.4698` edge `-0.0646` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
