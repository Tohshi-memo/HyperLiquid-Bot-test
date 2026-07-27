# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T18:51:26.622401+00:00`
- Price records: `672`
- Market context records: `8119`
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

- `market_context_high->equity_24h` score `22.1786` n `86` status `ready` deltaP `40.1769` edge `1.6714` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5105` n `86` status `ready` deltaP `34.5434` edge `0.6007` maxDD `-1.7427`
- `market_context_high->metal_24h` score `8.491` n `86` status `ready` deltaP `35.9375` edge `0.468` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.0112` n `43` status `ready` deltaP `31.055` edge `0.4811` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.2275` n `43` status `ready` deltaP `16.0699` edge `0.3057` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7487` n `43` status `ready` deltaP `29.2299` edge `0.1484` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.6549` n `86` status `ready` deltaP `33.1148` edge `0.0968` maxDD `-0.3723`
- `market_context_high->index_24h` score `3.6353` n `86` status `ready` deltaP `22.945` edge `0.217` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.9099` n `43` status `ready` deltaP `5.6538` edge `0.2326` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.7672` n `87` status `ready` deltaP `15.6239` edge `0.1643` maxDD `-1.6954`
- `news_risk_high->index_4h` score `2.5211` n `43` status `ready` deltaP `21.4868` edge `0.0859` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4353` n `86` status `ready` deltaP `22.3625` edge `0.1161` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0379` n `86` status `ready` deltaP `28.1371` edge `0.0526` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.9549` n `86` status `ready` deltaP `10.3694` edge `0.2055` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5614` n `86` status `ready` deltaP `11.4187` edge `0.2258` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.3698` n `87` status `ready` deltaP `16.6185` edge `0.0249` maxDD `-0.39`
- `market_context_high->commodity_24h` score `1.319` n `86` status `ready` deltaP `30.3214` edge `0.2555` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.2405` n `43` status `ready` deltaP `13.0601` edge `0.0631` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.037` n `43` status `ready` deltaP `4.5363` edge `0.0959` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.9318` n `87` status `ready` deltaP `12.6729` edge `0.031` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
