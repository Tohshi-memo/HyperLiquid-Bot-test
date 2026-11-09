# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T23:52:28.206023+00:00`
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

- `market_context_high->unknown_4h` score `29.6323` n `88` status `ready` deltaP `7.2201` edge `2.466` maxDD `-0.9153`
- `market_context_high->equity_24h` score `18.3385` n `59` status `ready` deltaP `27.2626` edge `2.4098` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.1679` n `59` status `ready` deltaP `22.4686` edge `0.3026` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `0.9843` n `59` status `ready` deltaP `10.5631` edge `0.5652` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.2108` n `59` status `ready` deltaP `11.741` edge `-0.0054` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3904` n `88` status `ready` deltaP `3.4976` edge `0.0118` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5405` n `88` status `ready` deltaP `-0.0068` edge `-0.001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8477` n `88` status `ready` deltaP `0.0416` edge `-0.0112` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8703` n `88` status `ready` deltaP `-2.2311` edge `0.0139` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0952` n `88` status `ready` deltaP `-9.1521` edge `0.0037` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1459` n `88` status `ready` deltaP `-2.2727` edge `0.0066` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3436` n `88` status `ready` deltaP `-14.657` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7656` n `88` status `ready` deltaP `-8.4036` edge `0.0143` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.935` n `88` status `ready` deltaP `0.6328` edge `-0.0544` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1343` n `88` status `ready` deltaP `-6.9152` edge `-0.0094` maxDD `-2.4506`
- `market_context_high->commodity_24h` score `-2.2305` n `59` status `ready` deltaP `-15.6302` edge `0.0466` maxDD `-9.2687`
- `market_context_high->fx_24h` score `-2.3977` n `59` status `ready` deltaP `-14.9928` edge `-0.0529` maxDD `-3.364`
- `market_context_high->crypto_major_1h` score `-3.2282` n `88` status `ready` deltaP `-5.5593` edge `-0.1145` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4021` n `88` status `ready` deltaP `-2.5915` edge `-0.2184` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1026` n `88` status `ready` deltaP `2.245` edge `-0.2617` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
