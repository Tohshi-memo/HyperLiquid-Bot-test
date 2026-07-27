# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T08:37:27.496921+00:00`
- Price records: `672`
- Market context records: `8074`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.133` n `83` status `ready` deltaP `36.4619` edge `1.5257` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.7816` n `31` status `ready` deltaP `35.1643` edge `0.502` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3734` n `87` status `ready` deltaP `32.4205` edge `0.5296` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2676` n `83` status `ready` deltaP `35.8752` edge `0.4498` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.4444` n `31` status `ready` deltaP `35.2921` edge `0.4001` maxDD `-0.201`
- `news_risk_high->crypto_alt_4h` score `4.624` n `31` status `ready` deltaP `26.2245` edge `0.2392` maxDD `-0.9625`
- `news_risk_high->equity_1h` score `3.4331` n `42` status `ready` deltaP `28.0938` edge `0.1304` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2881` n `87` status `ready` deltaP `31.5881` edge `0.0822` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.9225` n `83` status `ready` deltaP `18.2498` edge `0.1889` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7404` n `42` status `ready` deltaP `2.6946` edge `0.2381` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.4617` n `31` status `ready` deltaP `20.2793` edge `0.089` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.414` n `87` status `ready` deltaP `22.2158` edge `0.1153` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3682` n `87` status `ready` deltaP `14.8754` edge `0.1415` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2892` n `83` status `ready` deltaP `30.7531` edge `0.0561` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `2.2453` n `83` status `ready` deltaP `27.5334` edge `0.2344` maxDD `-12.468`
- `news_risk_high->fx_4h` score `1.7077` n `31` status `ready` deltaP `22.7478` edge `0.0213` maxDD `-0.1179`
- `market_context_high->index_1h` score `1.129` n `87` status `ready` deltaP `14.9718` edge `0.021` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `0.8586` n `31` status `ready` deltaP `8.571` edge `0.0612` maxDD `-0.7433`
- `market_context_high->metal_1h` score `0.8015` n `87` status `ready` deltaP `11.2241` edge `0.0298` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.5142` n `42` status `ready` deltaP `1.7822` edge `0.0707` maxDD `-1.1783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
