# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T23:22:31.425107+00:00`
- Price records: `672`
- Market context records: `8140`
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

- `market_context_high->equity_24h` score `23.8941` n `84` status `ready` deltaP `43.0804` edge `1.795` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0042` n `85` status `ready` deltaP `36.0383` edge `0.6169` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.7663` n `84` status `ready` deltaP `36.9792` edge `0.484` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7306` n `43` status `ready` deltaP `30.2928` edge `0.4628` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.3799` n `43` status `ready` deltaP `16.9846` edge `0.3123` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1063` n `84` status `ready` deltaP `25.3224` edge `0.2404` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.8881` n `85` status `ready` deltaP `34.3185` edge `0.0995` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.6012` n `43` status `ready` deltaP `28.3317` edge `0.1421` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0972` n `85` status `ready` deltaP `16.3755` edge `0.1792` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6201` n `85` status `ready` deltaP `24.0119` edge `0.1205` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3997` n `43` status `ready` deltaP `20.4197` edge `0.0829` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.3237` n `85` status `ready` deltaP `12.5485` edge `0.2217` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.2376` n `84` status `ready` deltaP `30.2579` edge `0.0551` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.059` n `85` status `ready` deltaP `14.2486` edge `0.2484` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.7509` n `84` status `ready` deltaP `32.8373` edge `0.2941` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.5121` n `85` status `ready` deltaP `17.7651` edge `0.0272` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.2099` n `43` status `ready` deltaP `12.6028` edge `0.0636` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.1173` n `43` status `ready` deltaP `4.8357` edge `0.1006` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0264` n `85` status `ready` deltaP `13.6157` edge `0.0326` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.7944` n `85` status `ready` deltaP `12.5238` edge `0.0594` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
