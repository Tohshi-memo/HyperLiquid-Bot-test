# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T07:22:28.608518+00:00`
- Price records: `672`
- Market context records: `8069`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.0508` n `79` status `ready` deltaP `35.9739` edge `1.5221` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3506` n `87` status `ready` deltaP `32.4205` edge `0.5277` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.282` n `79` status `ready` deltaP `35.8752` edge `0.451` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.8555` n `38` status `ready` deltaP `31.4529` edge `0.1432` maxDD `-1.1944`
- `market_context_high->commodity_24h` score `3.8487` n `79` status `ready` deltaP `31.4986` edge `0.2857` maxDD `-9.3304`
- `news_risk_high->unknown_1h` score `3.5402` n `38` status `ready` deltaP `4.8771` edge `0.2902` maxDD `-0.8826`
- `market_context_high->index_4h` score `3.2809` n `87` status `ready` deltaP `31.5881` edge `0.0816` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7715` n `79` status `ready` deltaP `16.6027` edge `0.1873` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4092` n `87` status `ready` deltaP `22.2158` edge `0.1149` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3322` n `87` status `ready` deltaP `14.7257` edge `0.1395` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.1773` n `79` status `ready` deltaP `29.7896` edge `0.0532` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.4509` n `38` status `ready` deltaP `6.6971` edge `0.0996` maxDD `-0.5338`
- `news_risk_high->crypto_alt_1h` score `1.194` n `38` status `ready` deltaP `8.1941` edge `0.0659` maxDD `-0.3487`
- `market_context_high->index_1h` score `1.0883` n `87` status `ready` deltaP `14.5227` edge `0.0206` maxDD `-0.4716`
- `news_risk_high->index_1h` score `0.8044` n `38` status `ready` deltaP `9.8645` edge `0.0218` maxDD `-0.3089`
- `market_context_high->metal_1h` score `0.7464` n `87` status `ready` deltaP `10.775` edge `0.0282` maxDD `-0.6936`
- `news_risk_high->fx_1h` score `0.5525` n `38` status `ready` deltaP `9.5414` edge `0.0082` maxDD `-0.0611`
- `market_context_high->crypto_major_1h` score `0.4188` n `87` status `ready` deltaP `8.5725` edge `0.0188` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.3146` n `87` status `ready` deltaP `3.5902` edge `0.114` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.1892` n `87` status `ready` deltaP `6.5812` edge `0.1437` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
