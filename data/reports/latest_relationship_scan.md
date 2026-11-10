# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T09:37:27.142929+00:00`
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

- `market_context_high->unknown_4h` score `37.6357` n `88` status `ready` deltaP `7.6774` edge `3.1299` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.1506` n `88` status `ready` deltaP `33.0412` edge `2.9494` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5052` n `88` status `ready` deltaP `25.8783` edge `0.3325` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.3746` n `88` status `ready` deltaP `22.6012` edge `0.9196` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0411` n `88` status `ready` deltaP `16.557` edge `-0.0585` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3723` n `88` status `ready` deltaP `2.2387` edge `0.0056` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4221` n `88` status `ready` deltaP `3.1042` edge `0.0358` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.5162` n `88` status `ready` deltaP `2.3` edge `0.0093` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.8043` n `88` status `ready` deltaP `0.6513` edge `-0.0097` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0773` n `88` status `ready` deltaP `-8.8527` edge `0.004` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2793` n `88` status `ready` deltaP `-3.1873` edge `-0.0044` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3257` n `88` status `ready` deltaP `-14.3576` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8263` n `88` status `ready` deltaP `-9.4515` edge `0.0135` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9997` n `88` status `ready` deltaP `0.1837` edge `-0.0597` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0418` n `88` status `ready` deltaP `-5.3908` edge `-0.0077` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5864` n `88` status `ready` deltaP `-4.4194` edge `-0.0261` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1666` n `88` status `ready` deltaP `-4.9605` edge `-0.1106` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3177` n `88` status `ready` deltaP `-2.2866` edge `-0.2134` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1624` n `88` status `ready` deltaP `1.4828` edge `-0.2616` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.268` n `88` status `ready` deltaP `-23.4698` edge `-0.0635` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
