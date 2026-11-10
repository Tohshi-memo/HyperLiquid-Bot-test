# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T18:22:30.696502+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_4h` score `52.3339` n `88` status `ready` deltaP `7.2201` edge `4.3578` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.0252` n `88` status `ready` deltaP `33.6489` edge `2.9349` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.862` n `88` status `ready` deltaP `26.5151` edge `1.0842` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.6436` n `88` status `ready` deltaP `27.683` edge `0.332` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.2613` n `88` status `ready` deltaP `21.8276` edge `0.0149` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3065` n `88` status `ready` deltaP `4.2461` edge `0.0138` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4004` n `88` status `ready` deltaP `2.5381` edge `0.0` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.488` n `88` status `ready` deltaP `3.5615` edge `0.0243` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5856` n `88` status `ready` deltaP `3.8525` edge `-0.003` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9488` n `88` status `ready` deltaP `-6.7569` edge `0.0065` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0205` n `88` status `ready` deltaP `-0.5959` edge `0.0115` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2478` n `88` status `ready` deltaP `-13.0103` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.4787` n `88` status `ready` deltaP `-6.6072` edge `0.0391` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7744` n `88` status `ready` deltaP `1.531` edge `-0.0398` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8084` n `88` status `ready` deltaP `-1.4274` edge `-0.0042` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-1.9626` n `88` status `ready` deltaP `1.5625` edge `-0.014` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8471` n `88` status `ready` deltaP `-2.8647` edge `-0.0836` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.197` n `88` status `ready` deltaP `1.372` edge `-0.1444` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.3385` n `88` status `ready` deltaP `3.9219` edge `-0.2092` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-8.9738` n `88` status `ready` deltaP `3.3302` edge `0.3925` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
