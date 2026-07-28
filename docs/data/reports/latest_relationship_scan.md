# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T00:07:31.361157+00:00`
- Price records: `672`
- Market context records: `8143`
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

- `market_context_high->equity_24h` score `24.333` n `84` status `ready` deltaP `43.6012` edge `1.8281` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0972` n `85` status `ready` deltaP `36.4956` edge `0.6216` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8493` n `84` status `ready` deltaP `37.3264` edge `0.4886` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8236` n `43` status `ready` deltaP `30.7501` edge `0.4675` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.5544` n `43` status `ready` deltaP `17.4419` edge `0.3238` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.2235` n `84` status `ready` deltaP `25.8432` edge `0.2467` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9415` n `85` status `ready` deltaP `34.7758` edge `0.1009` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.6312` n `43` status `ready` deltaP `28.6311` edge `0.1426` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.1272` n `85` status `ready` deltaP `16.6749` edge `0.1797` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6795` n `85` status `ready` deltaP `24.4692` edge `0.1224` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.4923` n `85` status `ready` deltaP `13.0058` edge `0.2327` maxDD `-3.9374`
- `news_risk_high->index_4h` score `2.4531` n `43` status `ready` deltaP `20.877` edge `0.0843` maxDD `-0.191`
- `market_context_high->fx_24h` score `2.2702` n `84` status `ready` deltaP `30.6051` edge `0.0555` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.2336` n `85` status `ready` deltaP `14.7059` edge `0.2599` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.824` n `84` status `ready` deltaP `33.3581` edge `0.3` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.5253` n `85` status `ready` deltaP `17.9148` edge `0.0273` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.2693` n `43` status `ready` deltaP `13.0601` edge `0.0655` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.188` n `43` status `ready` deltaP `5.2848` edge `0.1035` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0528` n `85` status `ready` deltaP `13.9151` edge `0.0328` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.8404` n `85` status `ready` deltaP `12.9729` edge `0.0623` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
