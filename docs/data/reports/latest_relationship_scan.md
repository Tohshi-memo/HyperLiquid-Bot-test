# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T04:22:33.407234+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `3044.2297` n `45` status `ready` deltaP `21.493` edge `253.5846` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.7163` n `40` status `ready` deltaP `51.4583` edge `0.8397` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1054` n `40` status `ready` deltaP `51.3194` edge `0.5961` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `2.4489` n `45` status `ready` deltaP `2.8117` edge `0.2617` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.0219` n `45` status `ready` deltaP `9.7832` edge `0.058` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3658` n `47` status `ready` deltaP `7.5646` edge `0.0339` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3349` n `47` status `ready` deltaP `5.0338` edge `0.094` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.1728` n `45` status `ready` deltaP `6.8632` edge `0.0115` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.1472` n `45` status `ready` deltaP `6.1311` edge `0.01` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0451` n `47` status `ready` deltaP `14.0277` edge `-0.0041` maxDD `-1.8531`
- `news_risk_high->commodity_1h` score `0.0349` n `45` status `ready` deltaP `10.0233` edge `-0.0144` maxDD `-1.5022`
- `market_context_high->fx_1h` score `-0.0084` n `47` status `ready` deltaP `6.9658` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.0424` n `45` status `ready` deltaP `3.3101` edge `0.0048` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1233` n `45` status `ready` deltaP `2.7578` edge `0.0036` maxDD `-0.2475`
- `news_risk_high->equity_1h` score `-0.2039` n `45` status `ready` deltaP `1.5137` edge `0.0552` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `-0.2079` n `47` status `ready` deltaP `2.2963` edge `0.0486` maxDD `-4.9116`
- `news_risk_high->crypto_alt_1h` score `-0.2621` n `45` status `ready` deltaP `4.6806` edge `0.0034` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.3933` n `45` status `ready` deltaP `2.8693` edge `0.0262` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.6681` n `45` status `ready` deltaP `0.835` edge `-0.0192` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6959` n `40` status `ready` deltaP `0.6597` edge `0.0356` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
