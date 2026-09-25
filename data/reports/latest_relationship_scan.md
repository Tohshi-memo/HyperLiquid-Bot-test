# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T21:37:30.689447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12010`

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

- `news_risk_high->unknown_24h` score `720.6957` n `75` status `ready` deltaP `-0.9861` edge `60.069` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.071` n `47` status `ready` deltaP `8.1698` edge `5.8752` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.4694` n `47` status `ready` deltaP `30.2489` edge `4.0434` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9312` n `47` status `ready` deltaP `24.782` edge `2.5337` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2816` n `47` status `ready` deltaP `33.8948` edge `1.9164` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6461` n `47` status `ready` deltaP `34.4156` edge `0.4207` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9242` n `47` status `ready` deltaP `33.3223` edge `0.1287` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7775` n `47` status `ready` deltaP `17.7542` edge `0.1549` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6274` n `47` status `ready` deltaP `30.3678` edge `0.0319` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3773` n `47` status `ready` deltaP `11.2124` edge `0.1068` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1332` n `47` status `ready` deltaP `12.9634` edge `0.0483` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9663` n `111` status `ready` deltaP `9.4784` edge `0.1084` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8529` n `47` status `ready` deltaP `13.4125` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5225` n `47` status `ready` deltaP `10.7083` edge `0.0078` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.4631` n `75` status `ready` deltaP `21.5209` edge `0.082` maxDD `-6.9545`
- `market_context_high->crypto_major_4h` score `0.3684` n `47` status `ready` deltaP `4.5375` edge `0.0909` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3255` n `47` status `ready` deltaP `5.0516` edge `0.0752` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.1047` n `111` status `ready` deltaP `4.3616` edge `0.0552` maxDD `-3.3776`
- `news_risk_high->equity_1h` score `0.0814` n `111` status `ready` deltaP `3.7628` edge `0.0361` maxDD `-2.0595`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
