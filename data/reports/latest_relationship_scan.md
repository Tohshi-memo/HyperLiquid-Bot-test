# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T15:07:29.445712+00:00`
- Price records: `672`
- Market context records: `8102`
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

- `market_context_high->equity_24h` score `20.7622` n `87` status `ready` deltaP `37.7717` edge `1.5694` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.7139` n `87` status `ready` deltaP `33.1826` edge `0.5529` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3696` n `87` status `ready` deltaP `35.8752` edge `0.4583` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.5932` n `43` status `ready` deltaP `30.7501` edge `0.4483` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `3.7581` n `43` status `ready` deltaP `15.0029` edge `0.2737` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.6971` n `43` status `ready` deltaP `29.0802` edge `0.1451` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.3749` n `87` status `ready` deltaP `31.893` edge `0.0874` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.2309` n `87` status `ready` deltaP `20.7853` edge `0.1977` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7972` n `43` status `ready` deltaP `4.7556` edge `0.2292` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.6057` n `87` status `ready` deltaP `15.4742` edge `0.1573` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4249` n `43` status `ready` deltaP `21.3343` edge `0.0789` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4042` n `87` status `ready` deltaP `22.0633` edge `0.1155` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0221` n `87` status `ready` deltaP `27.9089` edge `0.0528` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3037` n `43` status `ready` deltaP `13.6698` edge `0.0643` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2776` n `87` status `ready` deltaP `16.3191` edge `0.0244` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `1.2583` n `87` status `ready` deltaP `7.7061` edge `0.1652` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.9839` n `87` status `ready` deltaP `9.63` edge `0.1896` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `0.9761` n `87` status `ready` deltaP `28.0921` edge `0.2264` maxDD `-15.7497`
- `market_context_high->metal_1h` score `0.853` n `87` status `ready` deltaP `11.8229` edge `0.0301` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.8343` n `43` status `ready` deltaP `3.4884` edge `0.086` maxDD `-1.1783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
