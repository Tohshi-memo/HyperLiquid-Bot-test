# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T08:52:32.242187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11206`

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

- `market_context_high->unknown_1h` score `84.8673` n `47` status `ready` deltaP `8.4693` edge `7.0229` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.1553` n `47` status `ready` deltaP `30.9434` edge `4.0126` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.3008` n `47` status `ready` deltaP `24.782` edge `2.5645` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.7991` n `47` status `ready` deltaP `34.5892` edge `1.9549` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.4573` n `111` status `ready` deltaP `3.7156` edge `0.9439` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.9987` n `47` status `ready` deltaP `36.4989` edge `0.4362` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6997` n `47` status `ready` deltaP `39.7459` edge `0.1505` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6159` n `47` status `ready` deltaP `29.9017` edge `0.1368` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7807` n `47` status `ready` deltaP `32.0446` edge `0.0335` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3045` n `47` status `ready` deltaP `15.7725` edge `0.1287` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1066` n `47` status `ready` deltaP `9.688` edge `0.0944` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9343` n `47` status `ready` deltaP `11.4664` edge `0.0417` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9188` n `47` status `ready` deltaP `14.161` edge `0.01` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.747` n `111` status `ready` deltaP `7.9814` edge `0.1001` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `news_risk_high->metal_1h` score `0.0435` n `111` status `ready` deltaP `8.8445` edge `0.0076` maxDD `-0.7016`
- `market_context_high->metal_1h` score `0.043` n `47` status `ready` deltaP `3.7266` edge `0.0123` maxDD `-0.1976`
- `news_risk_high->index_1h` score `0.0315` n `111` status `ready` deltaP `4.0595` edge `0.0068` maxDD `-0.3863`
- `market_context_high->crypto_major_1h` score `-0.0379` n `47` status `ready` deltaP `3.2552` edge `0.0569` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0479` n `111` status `ready` deltaP `2.2658` edge `0.0295` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
