# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T16:22:33.252859+00:00`
- Price records: `672`
- Market context records: `8108`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->equity_24h` score `21.3463` n `87` status `ready` deltaP `38.6382` edge `1.6123` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.0217` n `87` status `ready` deltaP `33.64` edge `0.5755` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4092` n `87` status `ready` deltaP `35.8752` edge `0.4616` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.901` n `43` status `ready` deltaP `31.2075` edge `0.4709` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.0735` n `43` status `ready` deltaP `15.7651` edge `0.2949` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.8182` n `43` status `ready` deltaP `29.679` edge `0.1512` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.4339` n `87` status `ready` deltaP `32.0455` edge `0.0913` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.3914` n `87` status `ready` deltaP `21.6518` edge `0.2053` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.8655` n `43` status `ready` deltaP `5.2047` edge `0.2319` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.6271` n `88` status `ready` deltaP `15.2763` edge `0.1604` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4839` n `43` status `ready` deltaP `21.4868` edge `0.0828` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4078` n `87` status `ready` deltaP `22.0633` edge `0.1158` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9757` n `87` status `ready` deltaP `27.389` edge `0.0524` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.5797` n `87` status `ready` deltaP `8.4683` edge `0.1869` maxDD `-3.9374`
- `news_risk_high->metal_4h` score `1.3073` n `43` status `ready` deltaP `13.6698` edge `0.0646` maxDD `-0.7433`
- `market_context_high->crypto_major_4h` score `1.2993` n `87` status `ready` deltaP `10.3922` edge `0.2108` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.2758` n `88` status `ready` deltaP `16.297` edge `0.0244` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `1.0976` n `87` status `ready` deltaP `28.9587` edge `0.2362` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `1.007` n `43` status `ready` deltaP `4.2369` edge `0.0954` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8902` n `88` status `ready` deltaP `12.2278` edge `0.0305` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
