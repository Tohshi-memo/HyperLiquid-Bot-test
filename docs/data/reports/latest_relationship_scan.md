# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T00:37:27.206204+00:00`
- Price records: `672`
- Market context records: `8145`
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

- `market_context_high->equity_24h` score `23.7278` n `82` status `ready` deltaP `43.7161` edge `1.7769` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0587` n `83` status `ready` deltaP `36.6588` edge `0.6173` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8375` n `82` status `ready` deltaP `37.6736` edge `0.4853` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.92` n `43` status `ready` deltaP `31.055` edge `0.4735` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.6724` n `43` status `ready` deltaP `17.7468` edge `0.3316` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1082` n `82` status `ready` deltaP `25.4065` edge `0.24` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9352` n `83` status `ready` deltaP `34.9673` edge `0.0991` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.66` n `43` status `ready` deltaP `28.7808` edge `0.144` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.2483` n `83` status `ready` deltaP `17.3491` edge `0.1853` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.628` n `83` status `ready` deltaP `24.3205` edge `0.1191` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4931` n `43` status `ready` deltaP `21.1819` edge `0.0856` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.4262` n `83` status `ready` deltaP `12.3751` edge `0.2314` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.2072` n `82` status `ready` deltaP `29.9077` edge `0.0549` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.178` n `83` status `ready` deltaP `14.1603` edge `0.2589` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.7995` n `82` status `ready` deltaP `33.0665` edge `0.2988` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6879` n `83` status `ready` deltaP `19.5873` edge `0.0297` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.3105` n `43` status `ready` deltaP `13.365` edge `0.0669` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.2276` n `43` status `ready` deltaP `5.5842` edge `0.1048` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0108` n `83` status `ready` deltaP `13.4208` edge `0.0326` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.7925` n `83` status `ready` deltaP `12.3368` edge `0.0604` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
