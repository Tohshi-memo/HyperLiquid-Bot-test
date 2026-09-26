# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T00:07:30.219815+00:00`
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

- `news_risk_high->unknown_24h` score `1540.7823` n `85` status `ready` deltaP `-0.8293` edge `128.4085` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.4982` n `47` status `ready` deltaP `8.3196` edge `5.9098` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.0607` n `47` status `ready` deltaP `28.8601` edge `4.0186` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.5292` n `47` status `ready` deltaP `24.782` edge `2.5002` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1218` n `47` status `ready` deltaP `32.3323` edge `1.9135` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5957` n `47` status `ready` deltaP `34.4156` edge `0.4165` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7469` n `47` status `ready` deltaP `31.5862` edge `0.1255` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7351` n `47` status `ready` deltaP `17.4494` edge `0.1534` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5226` n `47` status `ready` deltaP `29.1483` edge `0.0313` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3749` n `47` status `ready` deltaP `11.2124` edge `0.1066` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1164` n `47` status `ready` deltaP `12.8137` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.952` n `114` status `ready` deltaP `10.2296` edge `0.1022` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8289` n `47` status `ready` deltaP `13.1131` edge `0.0095` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.7463` n `85` status `ready` deltaP `24.1769` edge `0.1006` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4202` n `47` status `ready` deltaP `4.6899` edge `0.0942` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2535` n `47` status `ready` deltaP `4.6025` edge `0.0722` maxDD `-4.5405`
- `market_context_high->fx_4h` score `0.0469` n `47` status `ready` deltaP `9.4739` edge `0.0075` maxDD `-0.6736`
- `news_risk_high->index_1h` score `0.0327` n `114` status `ready` deltaP `4.1732` edge `0.0062` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
