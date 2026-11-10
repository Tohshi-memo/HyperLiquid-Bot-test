# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T01:07:26.454696+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `38.5151` n `88` status `ready` deltaP `7.525` edge `3.2042` maxDD `-0.9153`
- `market_context_high->equity_24h` score `20.3216` n `64` status `ready` deltaP `29.2488` edge `2.6508` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.4275` n `64` status `ready` deltaP `24.0576` edge `0.3253` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `1.9829` n `64` status `ready` deltaP `14.1383` edge `0.6694` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.318` n `64` status `ready` deltaP `13.1255` edge `-0.0057` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3437` n `88` status `ready` deltaP `3.9467` edge `0.0127` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.574` n `88` status `ready` deltaP `-0.6056` edge `-0.0013` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8272` n `88` status `ready` deltaP `0.3464` edge `-0.0106` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8403` n `88` status `ready` deltaP `-1.7738` edge `0.0147` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0765` n `88` status `ready` deltaP `-8.8527` edge `0.0041` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1616` n `88` status `ready` deltaP `-2.4251` edge `0.0056` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3693` n `88` status `ready` deltaP `-15.1061` edge `-0.0064` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7679` n `88` status `ready` deltaP `-8.5533` edge `0.015` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9101` n `88` status `ready` deltaP `0.9322` edge `-0.0532` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1833` n `88` status `ready` deltaP `-7.6774` edge `-0.0106` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4611` n `64` status `ready` deltaP `-16.0474` edge `-0.0493` maxDD `-3.4061`
- `market_context_high->commodity_24h` score `-2.7457` n `64` status `ready` deltaP `-17.2796` edge `0.0341` maxDD `-11.0065`
- `market_context_high->crypto_major_1h` score `-3.1963` n `88` status `ready` deltaP `-5.2599` edge `-0.1124` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3959` n `88` status `ready` deltaP `-2.439` edge `-0.2189` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1086` n `88` status `ready` deltaP `2.245` edge `-0.2622` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
