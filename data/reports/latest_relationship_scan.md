# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T23:51:04.580811+00:00`
- Price records: `672`
- Market context records: `8142`
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

- `market_context_high->equity_24h` score `24.1907` n `84` status `ready` deltaP `43.4276` edge `1.8174` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0598` n `85` status `ready` deltaP `36.3432` edge `0.6195` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.815` n `84` status `ready` deltaP `37.1528` edge `0.4869` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7862` n `43` status `ready` deltaP `30.5977` edge `0.4654` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.4919` n `43` status `ready` deltaP `17.2895` edge `0.3196` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1857` n `84` status `ready` deltaP `25.6696` edge `0.2447` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9221` n `85` status `ready` deltaP `34.6234` edge `0.1003` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.636` n `43` status `ready` deltaP `28.6311` edge `0.143` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.132` n `85` status `ready` deltaP `16.6749` edge `0.1801` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6589` n `85` status `ready` deltaP `24.3167` edge `0.1217` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4337` n `43` status `ready` deltaP `20.7246` edge `0.0837` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.4321` n `85` status `ready` deltaP `12.8533` edge `0.2287` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.269` n `84` status `ready` deltaP `30.6051` edge `0.0554` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.171` n `85` status `ready` deltaP `14.5535` edge `0.2557` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.7994` n `84` status `ready` deltaP `33.1845` edge `0.298` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.5265` n `85` status `ready` deltaP `17.9148` edge `0.0274` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.2487` n `43` status `ready` deltaP `12.9076` edge `0.0648` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.1737` n `43` status `ready` deltaP `5.1351` edge `0.1033` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0516` n `85` status `ready` deltaP `13.9151` edge `0.0327` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.831` n `85` status `ready` deltaP `12.8232` edge `0.0621` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
