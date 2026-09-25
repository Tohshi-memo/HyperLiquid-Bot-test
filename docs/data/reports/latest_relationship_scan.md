# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T22:07:32.274526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11890`

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

- `news_risk_high->unknown_24h` score `915.5665` n `77` status `ready` deltaP `-0.9515` edge `76.308` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.3686` n `47` status `ready` deltaP `8.1698` edge `5.9` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.3924` n `47` status `ready` deltaP `29.9017` edge `4.0393` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8724` n `47` status `ready` deltaP `24.782` edge `2.5288` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2466` n `47` status `ready` deltaP `33.5476` edge `1.9158` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6365` n `47` status `ready` deltaP `34.4156` edge `0.4199` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8892` n `47` status `ready` deltaP `32.975` edge `0.1281` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7727` n `47` status `ready` deltaP `17.7542` edge `0.1545` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6006` n `47` status `ready` deltaP `30.0629` edge `0.0317` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3749` n `47` status `ready` deltaP `11.2124` edge `0.1066` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1045` n `47` status `ready` deltaP `12.664` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9604` n `111` status `ready` deltaP `9.3287` edge `0.1089` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8277` n `47` status `ready` deltaP `13.1131` edge `0.0094` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5344` n `47` status `ready` deltaP `10.858` edge `0.0078` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.5298` n `77` status `ready` deltaP `22.1433` edge `0.0864` maxDD `-6.9545`
- `market_context_high->crypto_major_4h` score `0.372` n `47` status `ready` deltaP `4.5375` edge `0.0912` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3099` n `47` status `ready` deltaP `4.9019` edge `0.0749` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.0891` n `111` status `ready` deltaP `4.2119` edge `0.0549` maxDD `-3.3776`
- `news_risk_high->equity_1h` score `0.0628` n `111` status `ready` deltaP `3.4634` edge `0.0357` maxDD `-2.0595`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
