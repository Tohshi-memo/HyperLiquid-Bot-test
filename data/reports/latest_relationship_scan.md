# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T07:52:31.633775+00:00`
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

- `market_context_high->unknown_4h` score `38.0953` n `88` status `ready` deltaP `7.6774` edge `3.1682` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.4974` n `88` status `ready` deltaP `33.0412` edge `2.9783` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.564` n `88` status `ready` deltaP `25.8783` edge `0.3374` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.2583` n `88` status `ready` deltaP `22.6012` edge `0.9047` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1371` n `88` status `ready` deltaP `16.557` edge `-0.0665` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.4276` n `88` status `ready` deltaP `1.4902` edge `0.0035` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4863` n `88` status `ready` deltaP `2.5994` edge `0.0098` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.5158` n `88` status `ready` deltaP `2.0371` edge `0.0309` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8233` n `88` status `ready` deltaP `0.3464` edge `-0.0101` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.1038` n `88` status `ready` deltaP `-9.3018` edge `0.0036` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.295` n `88` status `ready` deltaP `-3.3398` edge `-0.0054` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3514` n `88` status `ready` deltaP `-14.8067` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8489` n `88` status `ready` deltaP `-9.6012` edge `0.0116` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0441` n `88` status `ready` deltaP `-0.2654` edge `-0.0624` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1074` n `88` status `ready` deltaP `-6.4579` edge `-0.009` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.7122` n `88` status `ready` deltaP `-5.6326` edge `-0.0285` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2352` n `88` status `ready` deltaP `-5.5593` edge `-0.1154` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4151` n `88` status `ready` deltaP `-2.439` edge `-0.2205` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3248` n `88` status `ready` deltaP `1.178` edge `-0.2731` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.334` n `88` status `ready` deltaP `-23.4698` edge `-0.069` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
