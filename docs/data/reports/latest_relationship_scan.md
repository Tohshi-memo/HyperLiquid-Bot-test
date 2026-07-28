# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T00:22:31.426904+00:00`
- Price records: `672`
- Market context records: `8144`
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

- `market_context_high->equity_24h` score `24.0365` n `83` status `ready` deltaP `43.66` edge `1.803` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0978` n `84` status `ready` deltaP `36.5781` edge `0.6211` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.844` n `83` status `ready` deltaP `37.5` edge `0.487` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8682` n `43` status `ready` deltaP `30.9026` edge `0.4702` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.6122` n `43` status `ready` deltaP `17.5943` edge `0.3276` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1681` n `83` status `ready` deltaP `25.6296` edge `0.2435` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9396` n `84` status `ready` deltaP `34.8722` edge `0.1001` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.6372` n `43` status `ready` deltaP `28.6311` edge `0.1431` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.2447` n `84` status `ready` deltaP `17.5292` edge `0.1838` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6557` n `84` status `ready` deltaP `24.3975` edge `0.1209` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4725` n `43` status `ready` deltaP `21.0294` edge `0.0849` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.4603` n `84` status `ready` deltaP `12.696` edge `0.2321` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.2321` n `83` status `ready` deltaP `30.1748` edge `0.0552` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.2074` n `84` status `ready` deltaP `14.4381` edge `0.2595` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.812` n `83` status `ready` deltaP `33.2162` edge `0.2994` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6094` n `84` status `ready` deltaP `18.7411` edge `0.0288` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.2899` n `43` status `ready` deltaP `13.2125` edge `0.0662` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.2084` n `43` status `ready` deltaP `5.4345` edge `0.1042` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0346` n `84` status `ready` deltaP `13.6727` edge `0.0329` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.8249` n `84` status `ready` deltaP `12.6604` edge `0.0624` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
