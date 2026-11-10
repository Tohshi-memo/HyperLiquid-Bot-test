# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T12:52:25.534391+00:00`
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

- `market_context_high->unknown_4h` score `50.3917` n `88` status `ready` deltaP `7.6774` edge `4.1929` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8434` n `88` status `ready` deltaP `33.0412` edge `2.9238` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4536` n `88` status `ready` deltaP `25.8783` edge `0.3282` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.7826` n `88` status `ready` deltaP `22.9478` edge `0.9696` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.4005` n `88` status `ready` deltaP `18.1168` edge `-0.0321` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3699` n `88` status `ready` deltaP `2.3884` edge `0.0049` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4132` n `88` status `ready` deltaP `3.3479` edge `0.0109` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.4973` n `88` status `ready` deltaP `2.6469` edge `0.0292` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6755` n `88` status `ready` deltaP `2.633` edge `-0.0064` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0337` n `88` status `ready` deltaP `-8.1042` edge `0.0046` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0881` n `88` status `ready` deltaP `-1.2056` edge `0.0069` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3008` n `88` status `ready` deltaP `-13.9085` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7156` n `88` status `ready` deltaP `-8.5533` edge `0.0217` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8703` n `88` status `ready` deltaP `1.2316` edge `-0.0501` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.984` n `88` status `ready` deltaP `-4.3237` edge `-0.0074` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.3569` n `88` status `ready` deltaP `-2.1664` edge `-0.022` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.056` n `88` status `ready` deltaP `-4.0623` edge `-0.1024` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.844` n `88` status `ready` deltaP `-0.6098` edge `-0.1851` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.609` n `88` status `ready` deltaP `3.4645` edge `-0.2287` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.256` n `88` status `ready` deltaP `-23.4698` edge `-0.0625` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
