# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T09:07:30.521679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11912`

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

- `news_risk_high->unknown_24h` score `1316.3364` n `125` status `ready` deltaP `1.2153` edge `109.6866` maxDD `0.0`
- `market_context_high->unknown_1h` score `148.2085` n `41` status `ready` deltaP `10.585` edge `12.2848` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `55.6033` n `37` status `ready` deltaP `29.7626` edge `4.4703` maxDD `-2.4756`
- `market_context_high->equity_24h` score `29.9996` n `37` status `ready` deltaP `35.6654` edge `2.2936` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `27.625` n `37` status `ready` deltaP `14.4848` edge `2.2435` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.3629` n `37` status `ready` deltaP `33.0612` edge `0.4853` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.273` n `37` status `ready` deltaP `38.3728` edge `0.1241` maxDD `-0.2401`
- `market_context_high->crypto_alt_4h` score `4.1342` n `41` status `ready` deltaP `16.7683` edge `0.287` maxDD `-3.3417`
- `market_context_high->equity_4h` score `3.9131` n `41` status `ready` deltaP `25.0` edge `0.1929` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1405` n `41` status `ready` deltaP `34.4513` edge `0.0391` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.1859` n `41` status `ready` deltaP `8.5366` edge `0.2157` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.5883` n `41` status `ready` deltaP `17.4821` edge `0.0561` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.2354` n `41` status `ready` deltaP `10.0154` edge `0.1251` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.213` n `41` status `ready` deltaP `10.2709` edge `0.1184` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0618` n `41` status `ready` deltaP `14.7437` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.8194` n `41` status `ready` deltaP `14.3749` edge `0.0081` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.6748` n `125` status `ready` deltaP `14.9639` edge `0.026` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4259` n `125` status `ready` deltaP `14.8917` edge `0.1217` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.2657` n `41` status `ready` deltaP `5.9451` edge `0.0204` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1881` n `139` status `ready` deltaP `1.566` edge `0.0029` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
