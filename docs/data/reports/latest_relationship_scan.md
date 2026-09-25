# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T19:07:29.081176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11312`

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

- `market_context_high->unknown_1h` score `73.6606` n `47` status `ready` deltaP `7.8704` edge `6.093` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.6365` n `47` status `ready` deltaP `30.9434` edge `4.0527` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0788` n `47` status `ready` deltaP `24.782` edge `2.546` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3817` n `47` status `ready` deltaP `34.9364` edge `1.9178` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7333` n `47` status `ready` deltaP `34.9364` edge `0.4245` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.0912` n `47` status `ready` deltaP `34.8848` edge `0.1322` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7169` n `47` status `ready` deltaP `17.2969` edge `0.1529` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6822` n `47` status `ready` deltaP `30.9776` edge `0.0324` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4809` n `47` status `ready` deltaP `11.5172` edge `0.1134` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0733` n `47` status `ready` deltaP `12.5143` edge `0.0463` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.8968` n `111` status `ready` deltaP `9.179` edge `0.1046` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8876` n `47` status `ready` deltaP `13.8616` edge `0.0094` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4949` n `47` status `ready` deltaP `10.4089` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4858` n `47` status `ready` deltaP `5.2997` edge `0.0956` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3051` n `47` status `ready` deltaP `5.0516` edge `0.0735` maxDD `-4.5405`
- `news_risk_high->unknown_1h` score `0.2506` n `111` status `ready` deltaP `3.1167` edge `0.014` maxDD `-0.4452`
- `news_risk_high->crypto_major_1h` score `0.0843` n `111` status `ready` deltaP `4.3616` edge `0.0535` maxDD `-3.3776`
- `news_risk_high->metal_24h` score `0.0816` n `65` status `ready` deltaP `17.3398` edge `0.0573` maxDD `-6.9545`
- `news_risk_high->equity_1h` score `0.0425` n `111` status `ready` deltaP `3.3137` edge `0.0341` maxDD `-2.0595`
- `market_context_high->metal_1h` score `0.0126` n `47` status `ready` deltaP `3.4272` edge `0.0104` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
