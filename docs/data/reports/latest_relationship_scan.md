# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T12:07:24.544415+00:00`
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

- `market_context_high->unknown_4h` score `56.3725` n `88` status `ready` deltaP `7.6774` edge `4.6913` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8626` n `88` status `ready` deltaP `33.0412` edge `2.9254` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4596` n `88` status `ready` deltaP `25.8783` edge `0.3287` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.6546` n `88` status `ready` deltaP `22.6012` edge `0.9555` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.2809` n `88` status `ready` deltaP `17.5969` edge `-0.0386` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3785` n `88` status `ready` deltaP `2.2387` edge `0.0048` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4168` n `88` status `ready` deltaP `3.3479` edge `0.0106` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.4597` n `88` status `ready` deltaP `2.9518` edge `0.032` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.7071` n `88` status `ready` deltaP `2.1757` edge `-0.0074` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0501` n `88` status `ready` deltaP `-8.4036` edge `0.0045` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.129` n `88` status `ready` deltaP `-1.6629` edge `0.0047` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3008` n `88` status `ready` deltaP `-13.9085` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7429` n `88` status `ready` deltaP `-8.8527` edge `0.0202` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8836` n `88` status `ready` deltaP `1.2316` edge `-0.0518` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0093` n `88` status `ready` deltaP `-4.7811` edge `-0.0076` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4093` n `88` status `ready` deltaP `-2.6863` edge `-0.0229` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.0817` n `88` status `ready` deltaP `-4.212` edge `-0.1047` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.997` n `88` status `ready` deltaP `-1.0671` edge `-0.1948` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.6948` n `88` status `ready` deltaP `3.0072` edge `-0.2328` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2392` n `88` status `ready` deltaP `-23.4698` edge `-0.0611` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
