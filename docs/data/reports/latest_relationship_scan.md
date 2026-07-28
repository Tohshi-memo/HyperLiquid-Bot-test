# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T05:22:29.540408+00:00`
- Price records: `672`
- Market context records: `8165`
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

- `news_risk_high->unknown_24h` score `8065.0042` n `34` status `ready` deltaP `37.1528` edge `671.836` maxDD `0.0`
- `market_context_high->equity_24h` score `19.2983` n `65` status `ready` deltaP `44.4631` edge `1.4028` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5122` n `66` status `ready` deltaP `38.0035` edge `0.5628` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.9965` n `43` status `ready` deltaP `33.9514` edge `0.5439` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.2386` n `65` status `ready` deltaP `40.9722` edge `0.4134` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4618` n `43` status `ready` deltaP `20.3382` edge `0.3801` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0232` n `66` status `ready` deltaP `36.6223` edge `0.0954` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.6798` n `66` status `ready` deltaP `22.1648` edge `0.1792` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.5937` n `46` status `ready` deltaP `26.842` edge `0.1514` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.0568` n `65` status `ready` deltaP `20.0934` edge `0.1878` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8784` n `43` status `ready` deltaP `24.0782` edge `0.0984` maxDD `-0.191`
- `market_context_high->metal_4h` score `1.9381` n `66` status `ready` deltaP `22.2515` edge `0.0754` maxDD `-0.979`
- `market_context_high->index_1h` score `1.8489` n `66` status `ready` deltaP `21.3618` edge `0.0255` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.7582` n `43` status `ready` deltaP `16.2613` edge `0.0849` maxDD `-0.7433`
- `market_context_high->fx_24h` score `1.708` n `65` status `ready` deltaP `23.6379` edge `0.0551` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.4114` n `46` status `ready` deltaP `7.3418` edge `0.1084` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `1.2684` n `65` status `ready` deltaP `29.3482` edge `0.2555` maxDD `-15.7497`
- `news_risk_high->crypto_alt_4h` score `1.1761` n `43` status `ready` deltaP `12.8651` edge `0.2042` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `0.9698` n `66` status `ready` deltaP `10.5698` edge `0.0514` maxDD `-1.6171`
- `market_context_high->metal_1h` score `0.8735` n `66` status `ready` deltaP `12.2891` edge `0.0287` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
