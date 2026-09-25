# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T21:07:29.523108+00:00`
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

- `news_risk_high->unknown_24h` score `517.4752` n `73` status `ready` deltaP `-1.0227` edge `43.1342` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.2862` n `47` status `ready` deltaP `7.8704` edge `5.8118` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.5248` n `47` status `ready` deltaP `30.5962` edge `4.0457` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9744` n `47` status `ready` deltaP `24.782` edge `2.5373` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3154` n `47` status `ready` deltaP `34.242` edge `1.9169` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6557` n `47` status `ready` deltaP `34.4156` edge `0.4215` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9465` n `47` status `ready` deltaP `33.4959` edge `0.1294` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7775` n `47` status `ready` deltaP `17.7542` edge `0.1549` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6396` n `47` status `ready` deltaP `30.5202` edge `0.0319` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4233` n `47` status `ready` deltaP `11.5172` edge `0.1086` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1452` n `47` status `ready` deltaP `13.1131` edge `0.0483` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9232` n `111` status `ready` deltaP `9.3287` edge `0.1058` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.878` n `47` status `ready` deltaP `13.7119` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3854` n `47` status `ready` deltaP `4.6899` edge `0.0913` maxDD `-5.2359`
- `news_risk_high->metal_24h` score `0.3839` n `73` status `ready` deltaP `20.6716` edge `0.0775` maxDD `-6.9545`
- `market_context_high->crypto_major_1h` score `0.2919` n `47` status `ready` deltaP `4.9019` edge `0.0734` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `0.0892` n `111` status `ready` deltaP `3.9125` edge `0.0361` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `0.0711` n `111` status `ready` deltaP `4.2119` edge `0.0534` maxDD `-3.3776`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
