# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T01:52:30.711815+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11662`

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

- `news_risk_high->unknown_24h` score `2258.0423` n `88` status `ready` deltaP `-0.7892` edge `188.1799` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.527` n `47` status `ready` deltaP `8.3196` edge `5.9122` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.7558` n `47` status `ready` deltaP `27.6448` edge `4.0013` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.3024` n `47` status `ready` deltaP `24.782` edge `2.4813` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2007` n `47` status `ready` deltaP `32.8531` edge `1.9166` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5439` n `47` status `ready` deltaP `34.0684` edge `0.4145` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6999` n `47` status `ready` deltaP `31.2389` edge `0.1239` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7217` n `47` status `ready` deltaP `17.2969` edge `0.1533` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5262` n `47` status `ready` deltaP `29.1483` edge `0.0316` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.2435` n `47` status `ready` deltaP `10.755` edge `0.0987` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1212` n `47` status `ready` deltaP `12.8137` edge `0.0483` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8491` n `88` status `ready` deltaP `24.9526` edge `0.1086` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.8313` n `47` status `ready` deltaP `13.1131` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3416` n `47` status `ready` deltaP `4.2326` edge `0.0907` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3147` n `47` status `ready` deltaP `5.0516` edge `0.0743` maxDD `-4.5405`
- `news_risk_high->crypto_alt_1h` score `0.2452` n `117` status `ready` deltaP `7.8152` edge `0.0704` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0713` n `47` status `ready` deltaP `9.7788` edge `0.0075` maxDD `-0.6736`
- `news_risk_high->equity_4h` score `0.0654` n `107` status `ready` deltaP `15.4676` edge `0.0662` maxDD `-9.2079`
- `news_risk_high->index_1h` score `0.0567` n `117` status `ready` deltaP `4.4207` edge `0.0045` maxDD `-0.3395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
