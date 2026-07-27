# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T20:07:33.026333+00:00`
- Price records: `672`
- Market context records: `8124`
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

- `market_context_high->equity_24h` score `22.2075` n `84` status `ready` deltaP `40.8234` edge `1.6695` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0846` n `85` status `ready` deltaP `36.0383` edge `0.6236` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.5042` n `84` status `ready` deltaP `35.9375` edge `0.4691` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.811` n `43` status `ready` deltaP `30.2928` edge `0.4695` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.0969` n `43` status `ready` deltaP `15.3078` edge `0.2999` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9269` n `85` status `ready` deltaP `34.6234` edge `0.1007` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.6425` n `84` status `ready` deltaP `23.0654` edge `0.2168` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.5904` n `43` status `ready` deltaP `28.4814` edge `0.1402` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0864` n `85` status `ready` deltaP `16.5252` edge `0.1773` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5923` n `85` status `ready` deltaP `23.8594` edge `0.1192` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4385` n `43` status `ready` deltaP `20.7246` edge `0.0841` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1267` n `85` status `ready` deltaP `11.4814` edge `0.2124` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0306` n `84` status `ready` deltaP `28.001` edge `0.0529` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.7761` n `85` status `ready` deltaP `12.5718` edge `0.236` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.4881` n `85` status `ready` deltaP `17.4657` edge `0.0272` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.4027` n `84` status `ready` deltaP `30.5803` edge `0.2645` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.1821` n `43` status `ready` deltaP `12.4503` edge `0.0623` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.012` n `85` status `ready` deltaP `13.466` edge `0.0324` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.9387` n `43` status `ready` deltaP `3.9375` edge `0.0917` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.6783` n `85` status `ready` deltaP `11.6256` edge `0.0505` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
