# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T10:52:28.219719+00:00`
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

- `market_context_high->unknown_4h` score `42.9169` n `88` status `ready` deltaP `7.6774` edge `3.57` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9622` n `88` status `ready` deltaP `33.0412` edge `2.9337` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4776` n `88` status `ready` deltaP `25.8783` edge `0.3302` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.5072` n `88` status `ready` deltaP `22.6012` edge `0.9366` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0831` n `88` status `ready` deltaP `16.7303` edge `-0.0493` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3855` n `88` status `ready` deltaP `2.089` edge `0.0049` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4221` n `88` status `ready` deltaP `3.1042` edge `0.0358` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.4575` n `88` status `ready` deltaP `2.8988` edge `0.0102` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.7561` n `88` status `ready` deltaP `1.4135` edge `-0.0086` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0423` n `88` status `ready` deltaP `-8.2539` edge `0.0045` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2038` n `88` status `ready` deltaP `-2.4251` edge `0.0002` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3163` n `88` status `ready` deltaP `-14.2079` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7663` n `88` status `ready` deltaP `-9.0024` edge `0.0182` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9273` n `88` status `ready` deltaP `0.9322` edge `-0.0554` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.018` n `88` status `ready` deltaP `-4.9335` edge `-0.0077` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4955` n `88` status `ready` deltaP `-3.5529` edge `-0.0243` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.102` n `88` status `ready` deltaP `-4.3617` edge `-0.1063` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.1803` n `88` status `ready` deltaP `-1.8293` edge `-0.205` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.9142` n `88` status `ready` deltaP `2.245` edge `-0.246` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2164` n `88` status `ready` deltaP `-23.4698` edge `-0.0592` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
