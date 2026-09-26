# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T07:23:02.579932+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11848`

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

- `news_risk_high->unknown_24h` score `3360.25` n `102` status `ready` deltaP `-0.6332` edge `280.0295` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8373` n `47` status `ready` deltaP `8.7687` edge `5.7684` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.1555` n `47` status `ready` deltaP `23.8253` edge `3.8934` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.483` n `47` status `ready` deltaP `22.0042` edge `2.3482` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3695` n `47` status `ready` deltaP `33.3739` edge `1.9272` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.2164` n `47` status `ready` deltaP `30.7698` edge `0.4092` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4245` n `47` status `ready` deltaP `28.982` edge `0.116` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7265` n `47` status `ready` deltaP `17.2969` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5176` n `47` status `ready` deltaP `28.9958` edge `0.0319` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3561` n `47` status `ready` deltaP `11.5172` edge `0.103` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2235` n `102` status `ready` deltaP `28.0433` edge `0.136` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0625` n `47` status `ready` deltaP `12.2149` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7571` n `47` status `ready` deltaP `12.2149` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5332` n `47` status `ready` deltaP `10.858` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.5206` n `47` status `ready` deltaP `5.2997` edge `0.0985` maxDD `-5.2359`
- `news_risk_high->index_24h` score `0.3575` n `102` status `ready` deltaP `13.6234` edge `0.0391` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.335` n `47` status `ready` deltaP `5.2013` edge `0.075` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1129` n `134` status `ready` deltaP `5.2127` edge `0.0039` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0737` n `47` status `ready` deltaP `9.7788` edge `0.0077` maxDD `-0.6736`
- `news_risk_high->crypto_alt_1h` score `0.0337` n `134` status `ready` deltaP `5.9501` edge `0.0542` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
