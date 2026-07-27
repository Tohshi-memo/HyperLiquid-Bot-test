# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T22:22:31.335302+00:00`
- Price records: `672`
- Market context records: `8135`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `23.3093` n `84` status `ready` deltaP `42.3859` edge `1.7509` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9655` n `85` status `ready` deltaP `35.7335` edge `0.6157` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.646` n `84` status `ready` deltaP `36.2847` edge `0.4786` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.6918` n `43` status `ready` deltaP `29.988` edge `0.4616` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.2315` n `43` status `ready` deltaP `16.3748` edge `0.304` maxDD `-2.1767`
- `market_context_high->index_24h` score `3.9523` n `84` status `ready` deltaP `24.6279` edge `0.2322` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.8541` n `85` status `ready` deltaP `34.0136` edge `0.0987` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5497` n `43` status `ready` deltaP `28.0323` edge `0.1398` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0457` n `85` status `ready` deltaP `16.0761` edge `0.1769` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5861` n `85` status `ready` deltaP `23.707` edge `0.1197` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3657` n `43` status `ready` deltaP `20.1148` edge `0.0821` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1923` n `85` status `ready` deltaP `12.0911` edge `0.2138` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.1748` n `84` status `ready` deltaP `29.5635` edge `0.0545` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.9106` n `85` status `ready` deltaP `13.6388` edge `0.2401` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.6524` n `84` status `ready` deltaP `32.1428` edge `0.2861` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4869` n `85` status `ready` deltaP `17.4657` edge `0.0271` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1759` n `43` status `ready` deltaP `12.2979` edge `0.0628` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.0405` n `43` status `ready` deltaP `4.686` edge `0.0952` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0144` n `85` status `ready` deltaP `13.466` edge `0.0326` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.7445` n `85` status `ready` deltaP `12.3741` edge `0.054` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
