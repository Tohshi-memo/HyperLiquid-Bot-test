# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T22:39:54.630816+00:00`
- Price records: `672`
- Market context records: `8137`
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

- `market_context_high->equity_24h` score `23.4528` n `84` status `ready` deltaP `42.5595` edge `1.7617` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9606` n `85` status `ready` deltaP `35.7335` edge `0.6153` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.6767` n `84` status `ready` deltaP `36.4583` edge `0.48` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.687` n `43` status `ready` deltaP `29.988` edge `0.4612` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.2533` n `43` status `ready` deltaP `16.5273` edge `0.3048` maxDD `-2.1767`
- `market_context_high->index_24h` score `3.9902` n `84` status `ready` deltaP `24.8015` edge `0.2342` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.8565` n `85` status `ready` deltaP `34.0136` edge `0.0989` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5533` n `43` status `ready` deltaP `28.0323` edge `0.1401` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0493` n `85` status `ready` deltaP `16.0761` edge `0.1772` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5873` n `85` status `ready` deltaP `23.707` edge `0.1198` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3681` n `43` status `ready` deltaP `20.1148` edge `0.0823` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1971` n `85` status `ready` deltaP `12.0911` edge `0.2142` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.1899` n `84` status `ready` deltaP `29.7371` edge `0.0546` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.9324` n `85` status `ready` deltaP `13.7913` edge `0.2409` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.6763` n `84` status `ready` deltaP `32.3164` edge `0.288` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4869` n `85` status `ready` deltaP `17.4657` edge `0.0271` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1771` n `43` status `ready` deltaP `12.2979` edge `0.0629` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.0429` n `43` status `ready` deltaP `4.686` edge `0.0954` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0132` n `85` status `ready` deltaP `13.466` edge `0.0325` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.746` n `85` status `ready` deltaP `12.3741` edge `0.0542` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
