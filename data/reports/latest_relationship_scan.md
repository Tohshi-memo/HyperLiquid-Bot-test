# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T19:37:32.823626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11764`

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

- `market_context_high->unknown_4h` score `52.7349` n `88` status `ready` deltaP `7.3725` edge `4.3902` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.1452` n `88` status `ready` deltaP `33.6489` edge `2.9449` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.1551` n `88` status `ready` deltaP `27.3832` edge `1.116` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.7478` n `88` status `ready` deltaP `28.5511` edge `0.3349` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.5072` n `88` status `ready` deltaP `22.6957` edge `0.0296` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3389` n `88` status `ready` deltaP `3.9467` edge `0.0131` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3918` n `88` status `ready` deltaP `2.6878` edge `0.0001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.5005` n `88` status `ready` deltaP `3.5615` edge `0.0227` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5334` n `88` status `ready` deltaP `4.6147` edge `-0.0014` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9753` n `88` status `ready` deltaP `-7.206` edge `0.0061` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0071` n `88` status `ready` deltaP `-0.4434` edge `0.0122` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2478` n `88` status `ready` deltaP `-13.0103` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5387` n `88` status `ready` deltaP `-7.206` edge `0.0354` maxDD `-8.1039`
- `market_context_high->fx_4h` score `-1.7815` n `88` status `ready` deltaP `-0.9701` edge `-0.0038` maxDD `-2.4506`
- `market_context_high->crypto_alt_1h` score `-1.7955` n `88` status `ready` deltaP `1.3813` edge `-0.0415` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-1.8776` n `88` status `ready` deltaP `2.4306` edge `-0.0127` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9094` n `88` status `ready` deltaP `-3.3138` edge `-0.0886` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.9309` n `88` status `ready` deltaP `2.1341` edge `-0.1273` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.1071` n `88` status `ready` deltaP `4.6841` edge `-0.195` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-8.404` n `88` status `ready` deltaP `4.1983` edge `0.4342` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
