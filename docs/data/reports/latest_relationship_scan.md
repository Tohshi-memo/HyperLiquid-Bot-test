# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T09:52:32.831933+00:00`
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

- `market_context_high->unknown_4h` score `37.2865` n `88` status `ready` deltaP `7.6774` edge `3.1008` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.111` n `88` status `ready` deltaP `33.0412` edge `2.9461` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4992` n `88` status `ready` deltaP `25.8783` edge `0.332` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.4081` n `88` status `ready` deltaP `22.6012` edge `0.9239` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0219` n `88` status `ready` deltaP `16.557` edge `-0.0569` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3629` n `88` status `ready` deltaP `2.3884` edge `0.0058` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4182` n `88` status `ready` deltaP `3.1042` edge `0.0363` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.5019` n `88` status `ready` deltaP `2.4497` edge `0.0095` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.7948` n `88` status `ready` deltaP `0.8038` edge `-0.0095` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0688` n `88` status `ready` deltaP `-8.703` edge `0.0041` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2659` n `88` status `ready` deltaP `-3.0349` edge `-0.0037` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3171` n `88` status `ready` deltaP `-14.2079` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8193` n `88` status `ready` deltaP `-9.4515` edge `0.0144` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9849` n `88` status `ready` deltaP `0.3334` edge `-0.0588` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0339` n `88` status `ready` deltaP `-5.2384` edge `-0.0077` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5689` n `88` status `ready` deltaP `-4.2461` edge `-0.0258` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1503` n `88` status `ready` deltaP `-4.8108` edge `-0.1095` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.2961` n `88` status `ready` deltaP `-2.2866` edge `-0.2116` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1058` n `88` status `ready` deltaP `1.6353` edge `-0.2579` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2524` n `88` status `ready` deltaP `-23.4698` edge `-0.0622` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
