# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T23:37:39.052197+00:00`
- Price records: `672`
- Market context records: `8141`
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

- `market_context_high->equity_24h` score `24.04` n `84` status `ready` deltaP `43.254` edge `1.806` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.032` n `85` status `ready` deltaP `36.1908` edge `0.6182` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.7831` n `84` status `ready` deltaP `36.9792` edge `0.4854` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7584` n `43` status `ready` deltaP `30.4453` edge `0.4641` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.4353` n `43` status `ready` deltaP `17.137` edge `0.3159` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1454` n `84` status `ready` deltaP `25.496` edge `0.2425` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9051` n `85` status `ready` deltaP `34.4709` edge `0.0999` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.6192` n `43` status `ready` deltaP `28.4814` edge `0.1426` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.1152` n `85` status `ready` deltaP `16.5252` edge `0.1797` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6395` n `85` status `ready` deltaP `24.1643` edge `0.1211` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4167` n `43` status `ready` deltaP `20.5721` edge `0.0833` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.3767` n `85` status `ready` deltaP `12.7009` edge `0.2251` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.2539` n `84` status `ready` deltaP `30.4315` edge `0.0553` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.1144` n `85` status `ready` deltaP `14.401` edge `0.252` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.7756` n `84` status `ready` deltaP `33.0109` edge `0.2961` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.5265` n `85` status `ready` deltaP `17.9148` edge `0.0274` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.2293` n `43` status `ready` deltaP `12.7552` edge `0.0642` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.1509` n `43` status `ready` deltaP `4.9854` edge `0.1024` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0384` n `85` status `ready` deltaP `13.7654` edge `0.0326` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.8162` n `85` status `ready` deltaP `12.6735` edge `0.0612` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
