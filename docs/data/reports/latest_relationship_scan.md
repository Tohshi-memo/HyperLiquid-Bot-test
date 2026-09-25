# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T17:22:30.186512+00:00`
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

- `market_context_high->unknown_1h` score `63.3407` n `47` status `ready` deltaP `7.4213` edge `5.236` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.5873` n `47` status `ready` deltaP `30.9434` edge `4.0486` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0512` n `47` status `ready` deltaP `24.782` edge `2.5437` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3306` n `47` status `ready` deltaP `34.7628` edge `1.9147` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7477` n `47` status `ready` deltaP `34.9364` edge `0.4257` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.228` n `47` status `ready` deltaP `36.1` edge `0.1355` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.6822` n `47` status `ready` deltaP `30.9776` edge `0.0324` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6433` n `47` status `ready` deltaP `16.992` edge `0.1488` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.0165` n `60` status `ready` deltaP `22.1528` edge `0.0649` maxDD `-2.5637`
- `market_context_high->crypto_alt_4h` score `1.4291` n `47` status `ready` deltaP `11.3648` edge `0.1101` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9642` n `47` status `ready` deltaP `11.6161` edge `0.0432` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8696` n `47` status `ready` deltaP `13.7119` edge `0.0089` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8405` n `111` status `ready` deltaP `8.7299` edge `0.1029` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4326` n `47` status `ready` deltaP `9.6604` edge `0.0073` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3832` n `47` status `ready` deltaP `4.8423` edge `0.0901` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2295` n `47` status `ready` deltaP `4.6025` edge `0.0702` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0414` n `47` status `ready` deltaP `3.8763` edge `0.0111` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0411` n `111` status `ready` deltaP `8.9942` edge `0.0064` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `0.0088` n `111` status `ready` deltaP `3.9125` edge `0.0502` maxDD `-3.3776`
- `news_risk_high->index_1h` score `-0.0005` n `111` status `ready` deltaP `3.6104` edge `0.0057` maxDD `-0.3863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
