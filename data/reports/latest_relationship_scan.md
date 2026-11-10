# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T06:52:25.166407+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11430`

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

- `market_context_high->unknown_4h` score `37.8769` n `88` status `ready` deltaP `7.6774` edge `3.15` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.3965` n `87` status `ready` deltaP `32.8453` edge `2.9712` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5587` n `87` status `ready` deltaP `25.7216` edge `0.338` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.0552` n `87` status `ready` deltaP `22.2355` edge `0.8811` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1861` n `87` status `ready` deltaP `16.335` edge `-0.0691` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.4657` n `88` status `ready` deltaP `1.0411` edge `0.0016` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4875` n `88` status `ready` deltaP `2.5994` edge `0.0097` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.5623` n `88` status `ready` deltaP `1.4274` edge `0.029` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8256` n `88` status `ready` deltaP `0.3464` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.1038` n `88` status `ready` deltaP `-9.3018` edge `0.0036` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2903` n `88` status `ready` deltaP `-3.3398` edge `-0.0048` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.335` n `88` status `ready` deltaP `-14.5073` edge `-0.006` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8528` n `88` status `ready` deltaP `-9.6012` edge `0.0111` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0137` n `88` status `ready` deltaP `0.034` edge `-0.0605` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1462` n `88` status `ready` deltaP `-7.0676` edge `-0.0099` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.7774` n `87` status `ready` deltaP `-6.2073` edge `-0.0301` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2196` n `88` status `ready` deltaP `-5.4096` edge `-0.1144` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.9694` n `87` status `ready` deltaP `-23.3949` edge `-0.0683` maxDD `-24.9502`
- `market_context_high->equity_4h` score `-7.4957` n `88` status `ready` deltaP `-2.5915` edge `-0.2262` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3068` n `88` status `ready` deltaP `1.178` edge `-0.2716` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
