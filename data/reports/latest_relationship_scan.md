# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T19:22:29.297536+00:00`
- Price records: `672`
- Market context records: `8121`
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

- `market_context_high->equity_24h` score `21.9007` n `84` status `ready` deltaP `40.3026` edge `1.6474` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.2052` n `85` status `ready` deltaP `36.4956` edge `0.6306` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.4718` n `84` status `ready` deltaP `35.9375` edge `0.4664` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9316` n `43` status `ready` deltaP `30.7501` edge `0.4765` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1791` n `43` status `ready` deltaP `15.7651` edge `0.3037` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9767` n `85` status `ready` deltaP `35.0807` edge `0.1018` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.6743` n `43` status `ready` deltaP `28.9305` edge `0.1442` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.5445` n `84` status `ready` deltaP `22.5446` edge `0.2121` maxDD `-1.3621`
- `market_context_high->equity_1h` score `3.1703` n `85` status `ready` deltaP `16.9743` edge `0.1813` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6227` n `85` status `ready` deltaP `24.1643` edge `0.1197` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4883` n `43` status `ready` deltaP `21.1819` edge `0.0852` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1993` n `85` status `ready` deltaP `11.9387` edge `0.2154` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.9854` n `84` status `ready` deltaP `27.4801` edge `0.0526` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.8583` n `85` status `ready` deltaP `13.0291` edge `0.2398` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.5313` n `85` status `ready` deltaP `17.9148` edge `0.0278` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.3218` n `84` status `ready` deltaP `30.0595` edge `0.2576` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.2125` n `43` status `ready` deltaP `12.7552` edge `0.0628` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0528` n `85` status `ready` deltaP `13.9151` edge `0.0328` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `1.007` n `43` status `ready` deltaP `4.3866` edge `0.0944` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.7227` n `85` status `ready` deltaP `12.0747` edge `0.0532` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
