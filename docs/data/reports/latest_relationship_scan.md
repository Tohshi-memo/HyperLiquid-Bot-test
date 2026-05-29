# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T13:22:19.824693+00:00`
- Price records: `672`
- Market context records: `2248`
- Flow alert records: `8364`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9227`

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

- `news_risk_high->crypto_alt_24h` score `24.4833` n `43` status `ready` deltaP `55.071` edge `1.732` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.4351` n `43` status `ready` deltaP `44.723` edge `1.1154` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `16.127` n `43` status `ready` deltaP `35.6952` edge `1.1374` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.8956` n `43` status `ready` deltaP `25.6702` edge `1.0449` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `11.0635` n `131` status `ready` deltaP `31.0603` edge `0.8575` maxDD `-7.742`
- `market_context_high->unknown_24h` score `10.5024` n `115` status `ready` deltaP `31.9293` edge `0.7035` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `10.0659` n `43` status `ready` deltaP `35.9738` edge `0.6216` maxDD `-1.4744`
- `market_context_high->crypto_major_4h` score `10.0632` n `131` status `ready` deltaP `36.7145` edge `0.6833` maxDD `-4.8238`
- `market_context_high->crypto_major_24h` score `7.3105` n `115` status `ready` deltaP `19.3811` edge `1.1973` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.35` n `131` status `ready` deltaP `20.2278` edge `0.3671` maxDD `-1.8227`
- `market_context_high->index_4h` score `4.1149` n `131` status `ready` deltaP `31.5409` edge `0.17` maxDD `-0.3228`
- `news_risk_high->index_24h` score `4.0376` n `43` status `ready` deltaP `13.792` edge `0.2864` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8794` n `43` status `ready` deltaP `33.0721` edge `0.344` maxDD `-3.0367`
- `market_context_high->equity_24h` score `3.7658` n `115` status `ready` deltaP `23.2382` edge `0.3116` maxDD `-6.8828`
- `news_risk_high->fx_24h` score `3.6687` n `43` status `ready` deltaP `37.2295` edge `0.076` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.6479` n `115` status `ready` deltaP `15.5918` edge `0.2518` maxDD `-1.4737`
- `market_context_high->equity_4h` score `3.2275` n `131` status `ready` deltaP `21.3159` edge `0.2301` maxDD `-3.5934`
- `news_risk_high->commodity_24h` score `2.985` n `43` status `ready` deltaP `2.0309` edge `0.3169` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1098` n `43` status `ready` deltaP `26.8221` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.0961` n `143` status `ready` deltaP `13.5359` edge `0.1906` maxDD `-5.8265`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
