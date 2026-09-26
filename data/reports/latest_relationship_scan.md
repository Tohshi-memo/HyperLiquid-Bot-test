# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T13:22:27.935060+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11822`

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

- `news_risk_high->unknown_24h` score `4431.5167` n `85` status `ready` deltaP `0.1736` edge `369.2919` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.3058` n `47` status `ready` deltaP `8.0201` edge `5.7291` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.1444` n `47` status `ready` deltaP `22.4364` edge `3.8184` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.2044` n `47` status `ready` deltaP `17.8376` edge `2.1861` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6611` n `47` status `ready` deltaP `33.3739` edge `1.9515` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.9908` n `47` status `ready` deltaP `28.3392` edge `0.4066` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3908` n `47` status `ready` deltaP `28.6348` edge `0.1155` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `2.9654` n `85` status `ready` deltaP `11.73` edge `0.5641` maxDD `-29.2814`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.7309` n `47` status `ready` deltaP `31.5873` edge `0.0324` maxDD `-0.2323`
- `news_risk_high->index_24h` score `2.2854` n `85` status `ready` deltaP `26.4869` edge `0.0709` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.5079` n `85` status `ready` deltaP `31.8138` edge `0.146` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.3073` n `47` status `ready` deltaP `10.9075` edge `0.103` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0506` n `47` status `ready` deltaP `12.0652` edge `0.0474` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8651` n `47` status `ready` deltaP `7.2814` edge `0.114` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8313` n `47` status `ready` deltaP `13.1131` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4817` n `47` status `ready` deltaP `10.2592` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4261` n `47` status `ready` deltaP `5.8001` edge `0.0786` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0445` n `47` status `ready` deltaP `4.026` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0471` n `139` status `ready` deltaP `3.2708` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
