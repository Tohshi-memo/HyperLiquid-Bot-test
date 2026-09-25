# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T17:07:31.409981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11296`

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

- `market_context_high->unknown_1h` score `63.4043` n `47` status `ready` deltaP `7.4213` edge `5.2413` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.5633` n `47` status `ready` deltaP `30.9434` edge `4.0466` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.02` n `47` status `ready` deltaP `24.782` edge `2.5411` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.321` n `47` status `ready` deltaP `34.7628` edge `1.9139` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7489` n `47` status `ready` deltaP `34.9364` edge `0.4258` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.2479` n `47` status `ready` deltaP `36.2737` edge `0.136` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.681` n `47` status `ready` deltaP `30.9776` edge `0.0323` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6083` n `47` status `ready` deltaP `16.8396` edge `0.1469` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `1.9961` n `60` status `ready` deltaP `22.1528` edge `0.0632` maxDD `-2.5637`
- `market_context_high->crypto_alt_4h` score `1.3893` n `47` status `ready` deltaP `11.2124` edge `0.1078` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9618` n `47` status `ready` deltaP `11.6161` edge `0.043` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8684` n `47` status `ready` deltaP `13.7119` edge `0.0088` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8357` n `111` status `ready` deltaP `8.7299` edge `0.1025` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4338` n `47` status `ready` deltaP `9.6604` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.347` n `47` status `ready` deltaP `4.6899` edge `0.0881` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2103` n `47` status `ready` deltaP `4.4528` edge `0.0696` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0406` n `47` status `ready` deltaP `3.8763` edge `0.011` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0399` n `111` status `ready` deltaP `8.9942` edge `0.0063` maxDD `-0.7016`
- `news_risk_high->index_1h` score `-0.0012` n `111` status `ready` deltaP `3.6104` edge `0.0056` maxDD `-0.3863`
- `news_risk_high->crypto_major_1h` score `-0.0104` n `111` status `ready` deltaP `3.7628` edge `0.0496` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
