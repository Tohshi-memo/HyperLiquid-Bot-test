# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T21:07:32.075128+00:00`
- Price records: `672`
- Market context records: `8129`
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

- `market_context_high->equity_24h` score `22.6591` n `84` status `ready` deltaP `41.5179` edge `1.7025` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0003` n `85` status `ready` deltaP `35.7335` edge `0.6186` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.551` n `84` status `ready` deltaP `35.9375` edge `0.473` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7266` n `43` status `ready` deltaP `29.988` edge `0.4645` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1395` n `43` status `ready` deltaP `15.7651` edge `0.3004` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.8747` n `85` status `ready` deltaP `34.1661` edge `0.0994` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.7761` n `84` status `ready` deltaP `23.7599` edge `0.2233` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.5257` n `43` status `ready` deltaP `27.8826` edge `0.1388` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0217` n `85` status `ready` deltaP `15.9264` edge `0.1759` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5801` n `85` status `ready` deltaP `23.707` edge `0.1192` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3863` n `43` status `ready` deltaP `20.2673` edge `0.0828` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1219` n `85` status `ready` deltaP `11.4814` edge `0.212` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0946` n `84` status `ready` deltaP `28.6954` edge `0.0536` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.8187` n `85` status `ready` deltaP `13.0291` edge `0.2365` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.5207` n `84` status `ready` deltaP `31.2748` edge `0.275` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4618` n `85` status `ready` deltaP `17.1663` edge `0.027` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1699` n `43` status `ready` deltaP `12.2979` edge `0.0623` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0264` n `85` status `ready` deltaP `13.6157` edge `0.0326` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.9818` n `43` status `ready` deltaP `4.2369` edge `0.0933` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.7063` n `85` status `ready` deltaP `11.925` edge `0.0521` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
