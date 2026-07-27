# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T19:37:26.843185+00:00`
- Price records: `672`
- Market context records: `8122`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11841`

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

- `market_context_high->equity_24h` score `22.0022` n `84` status `ready` deltaP `40.4762` edge `1.6547` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.1558` n `85` status `ready` deltaP `36.3432` edge `0.6275` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.4826` n `84` status `ready` deltaP `35.9375` edge `0.4673` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8822` n `43` status `ready` deltaP `30.5977` edge `0.4734` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1453` n `43` status `ready` deltaP `15.6126` edge `0.3019` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9585` n `85` status `ready` deltaP `34.9282` edge `0.1013` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.636` n `43` status `ready` deltaP `28.7808` edge `0.142` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.5763` n `84` status `ready` deltaP `22.7182` edge `0.2136` maxDD `-1.3621`
- `market_context_high->equity_1h` score `3.132` n `85` status `ready` deltaP `16.8246` edge `0.1791` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6069` n `85` status `ready` deltaP `24.0119` edge `0.1194` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4701` n `43` status `ready` deltaP `21.0294` edge `0.0847` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1715` n `85` status `ready` deltaP `11.7863` edge `0.2141` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0005` n `84` status `ready` deltaP `27.6538` edge `0.0527` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.8245` n `85` status `ready` deltaP `12.8766` edge `0.238` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.5157` n `85` status `ready` deltaP `17.7651` edge `0.0275` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.348` n `84` status `ready` deltaP `30.2331` edge `0.2598` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.1967` n `43` status `ready` deltaP `12.6028` edge `0.0625` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0384` n `85` status `ready` deltaP `13.7654` edge `0.0326` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.9746` n `43` status `ready` deltaP `4.2369` edge `0.0927` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.7016` n `85` status `ready` deltaP `11.925` edge `0.0515` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
