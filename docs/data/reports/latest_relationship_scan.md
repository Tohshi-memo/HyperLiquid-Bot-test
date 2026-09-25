# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T13:02:08.054442+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11258`

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

- `market_context_high->unknown_1h` score `84.3166` n `47` status `ready` deltaP `8.1698` edge `6.979` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.3077` n `47` status `ready` deltaP `30.9434` edge `4.0253` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.7584` n `47` status `ready` deltaP `24.782` edge `2.5193` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2603` n `47` status `ready` deltaP `34.5892` edge `1.91` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.9065` n `111` status `ready` deltaP `3.4161` edge `0.9` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.7681` n `47` status `ready` deltaP `34.9364` edge `0.4274` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3219` n `47` status `ready` deltaP `36.7945` edge `0.1387` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.0666` n `56` status `ready` deltaP `26.7857` edge `0.1118` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5462` n `47` status `ready` deltaP `29.758` edge `0.0292` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.0268` n `47` status `ready` deltaP `14.4006` edge `0.1147` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9024` n `47` status `ready` deltaP `9.5355` edge `0.0784` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8744` n `47` status `ready` deltaP `13.7119` edge `0.0093` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8599` n `47` status `ready` deltaP `11.0173` edge `0.0385` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.711` n `111` status `ready` deltaP `8.1311` edge `0.0961` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4326` n `47` status `ready` deltaP `9.6604` edge `0.0073` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0027` n `111` status `ready` deltaP `3.6104` edge `0.0061` maxDD `-0.3863`
- `market_context_high->metal_1h` score `-0.0061` n `47` status `ready` deltaP `3.1278` edge `0.01` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.032` n `111` status `ready` deltaP `8.2457` edge `0.0053` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0427` n `47` status `ready` deltaP `3.4049` edge `0.0555` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0962` n `111` status `ready` deltaP `1.8167` edge `0.0263` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
