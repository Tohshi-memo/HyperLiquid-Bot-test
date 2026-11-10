# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T13:07:27.293666+00:00`
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

- `market_context_high->unknown_4h` score `45.0133` n `88` status `ready` deltaP `7.6774` edge `3.7447` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8482` n `88` status `ready` deltaP `33.0412` edge `2.9242` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4536` n `88` status `ready` deltaP `25.8783` edge `0.3282` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.8275` n `88` status `ready` deltaP `23.1211` edge `0.9742` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.4395` n `88` status `ready` deltaP `18.2901` edge `-0.03` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3731` n `88` status `ready` deltaP `2.3884` edge `0.0045` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.3964` n `88` status `ready` deltaP `3.4976` edge `0.0113` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.5051` n `88` status `ready` deltaP `2.6469` edge `0.0282` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6644` n `88` status `ready` deltaP `2.7855` edge `-0.006` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0252` n `88` status `ready` deltaP `-7.9545` edge `0.0047` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0763` n `88` status `ready` deltaP `-1.0532` edge `0.0074` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3008` n `88` status `ready` deltaP `-13.9085` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6962` n `88` status `ready` deltaP `-8.4036` edge `0.0232` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8625` n `88` status `ready` deltaP `1.2316` edge `-0.0491` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9753` n `88` status `ready` deltaP `-4.1713` edge `-0.0073` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.3395` n `88` status `ready` deltaP `-1.9931` edge `-0.0217` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.0458` n `88` status `ready` deltaP `-4.0623` edge `-0.1011` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.7874` n `88` status `ready` deltaP `-0.4573` edge `-0.1814` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5824` n `88` status `ready` deltaP `3.617` edge `-0.2275` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2632` n `88` status `ready` deltaP `-23.4698` edge `-0.0631` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
