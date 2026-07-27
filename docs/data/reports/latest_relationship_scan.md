# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T17:37:34.944505+00:00`
- Price records: `672`
- Market context records: `8114`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11825`

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

- `market_context_high->equity_24h` score `21.8764` n `87` status `ready` deltaP `39.5048` edge `1.6507` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.1561` n `87` status `ready` deltaP `33.64` edge `0.5867` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4524` n `87` status `ready` deltaP `35.8752` edge `0.4652` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.0354` n `43` status `ready` deltaP `31.2075` edge `0.4821` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1589` n `43` status `ready` deltaP `15.9175` edge `0.301` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7667` n `43` status `ready` deltaP `29.3796` edge `0.1489` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.5544` n `87` status `ready` deltaP `22.5184` edge `0.2131` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.4675` n `87` status `ready` deltaP `32.0455` edge `0.0941` maxDD `-0.5022`
- `news_risk_high->unknown_1h` score `2.8487` n `43` status `ready` deltaP `5.2047` edge `0.2305` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5755` n `88` status `ready` deltaP `14.9769` edge `0.1581` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.5175` n `43` status `ready` deltaP `21.4868` edge `0.0856` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3836` n `87` status `ready` deltaP `21.9109` edge `0.1148` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0185` n `87` status `ready` deltaP `27.9089` edge `0.0525` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.7618` n `87` status `ready` deltaP `9.2305` edge `0.197` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.3847` n `87` status `ready` deltaP `10.5446` edge `0.2169` maxDD `-6.7444`
- `news_risk_high->metal_4h` score `1.2831` n `43` status `ready` deltaP `13.5174` edge `0.0636` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2602` n `88` status `ready` deltaP `16.1473` edge `0.0241` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `1.2293` n `87` status `ready` deltaP `29.8253` edge `0.2473` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.9495` n `43` status `ready` deltaP `3.9375` edge `0.0926` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.877` n `88` status `ready` deltaP `12.0781` edge `0.0304` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
