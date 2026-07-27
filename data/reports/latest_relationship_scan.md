# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T15:52:30.967125+00:00`
- Price records: `672`
- Market context records: `8106`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11793`

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

- `market_context_high->equity_24h` score `21.1134` n `87` status `ready` deltaP `38.2916` edge `1.5952` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.9353` n `87` status `ready` deltaP `33.64` edge `0.5683` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3948` n `87` status `ready` deltaP `35.8752` edge `0.4604` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8146` n `43` status `ready` deltaP `31.2075` edge `0.4637` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `3.9723` n `43` status `ready` deltaP `15.4602` edge `0.2885` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7631` n `43` status `ready` deltaP `29.3796` edge `0.1486` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.4171` n `87` status `ready` deltaP `32.0455` edge `0.0899` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.3241` n `87` status `ready` deltaP `21.3052` edge `0.202` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.8404` n `43` status `ready` deltaP `5.055` edge `0.2308` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.6717` n `87` status `ready` deltaP `15.7736` edge `0.1608` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4671` n `43` status `ready` deltaP `21.4868` edge `0.0814` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4224` n `87` status `ready` deltaP `22.2158` edge `0.116` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9769` n `87` status `ready` deltaP `27.389` edge `0.0525` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.4701` n `87` status `ready` deltaP `8.1634` edge `0.1798` maxDD `-3.9374`
- `market_context_high->index_1h` score `1.3219` n `87` status `ready` deltaP `16.7682` edge `0.0251` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.3219` n `43` status `ready` deltaP `13.8223` edge `0.0648` maxDD `-0.7433`
- `market_context_high->crypto_major_4h` score `1.1981` n `87` status `ready` deltaP `10.0873` edge `0.2044` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.0507` n `87` status `ready` deltaP `28.6121` edge `0.2325` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.9459` n `43` status `ready` deltaP `3.9375` edge `0.0923` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8518` n `87` status `ready` deltaP `11.8229` edge `0.03` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
