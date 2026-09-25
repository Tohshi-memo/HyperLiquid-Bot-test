# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T11:52:32.129219+00:00`
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

- `market_context_high->unknown_1h` score `84.613` n `47` status `ready` deltaP `8.1698` edge `7.0037` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2537` n `47` status `ready` deltaP `30.9434` edge `4.0208` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8712` n `47` status `ready` deltaP `24.782` edge `2.5287` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3719` n `47` status `ready` deltaP `34.5892` edge `1.9193` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.2029` n `111` status `ready` deltaP `3.4161` edge `0.9247` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.7897` n `47` status `ready` deltaP `34.9364` edge `0.4292` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.419` n `47` status `ready` deltaP `37.6625` edge `0.141` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.2738` n `51` status `ready` deltaP `27.6961` edge `0.123` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5912` n `47` status `ready` deltaP `30.2154` edge `0.0299` maxDD `-0.2323`
- `market_context_high->equity_4h` score `1.9854` n `47` status `ready` deltaP `13.9433` edge `0.1143` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.864` n `47` status `ready` deltaP `9.5355` edge `0.0752` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8613` n `47` status `ready` deltaP `13.5622` edge `0.0092` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8108` n `47` status `ready` deltaP `10.5682` edge `0.0374` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.5994` n `111` status `ready` deltaP `7.5323` edge `0.0908` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.459` n `47` status `ready` deltaP `9.9598` edge `0.0075` maxDD `-0.1854`
- `market_context_high->metal_1h` score `-0.003` n `47` status `ready` deltaP `3.1278` edge `0.0104` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0059` n `111` status `ready` deltaP `3.4607` edge `0.006` maxDD `-0.3863`
- `news_risk_high->metal_1h` score `-0.0272` n `111` status `ready` deltaP `8.2457` edge `0.0057` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.1281` n `111` status `ready` deltaP `1.3676` edge `0.0252` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.1734` n `47` status `ready` deltaP `2.9558` edge `0.0476` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
