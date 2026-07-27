# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T14:22:29.292946+00:00`
- Price records: `672`
- Market context records: `8099`
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

- `market_context_high->equity_24h` score `20.495` n `87` status `ready` deltaP `37.2517` edge `1.5506` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5311` n `87` status `ready` deltaP `32.8778` edge `0.5397` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3492` n `87` status `ready` deltaP `35.8752` edge `0.4566` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.4104` n `43` status `ready` deltaP `30.4453` edge `0.4351` maxDD `-0.6428`
- `news_risk_high->equity_1h` score `3.6251` n `43` status `ready` deltaP `29.0802` edge `0.1391` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.5631` n `43` status `ready` deltaP `14.5456` edge `0.2605` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.3509` n `87` status `ready` deltaP `31.893` edge `0.0854` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.1545` n `87` status `ready` deltaP `20.2653` edge `0.1948` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7984` n `43` status `ready` deltaP `4.7556` edge `0.2293` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5337` n `87` status `ready` deltaP `15.4742` edge `0.1513` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4009` n `43` status `ready` deltaP `21.3343` edge `0.0769` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3666` n `87` status `ready` deltaP `21.7585` edge `0.1144` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0709` n `87` status `ready` deltaP `28.4288` edge `0.0534` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.2668` n `87` status `ready` deltaP `16.3191` edge `0.0235` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.2661` n `43` status `ready` deltaP `13.365` edge `0.0632` maxDD `-0.7433`
- `market_context_high->crypto_alt_4h` score `1.0717` n `87` status `ready` deltaP `7.2487` edge `0.1527` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `0.9062` n `87` status `ready` deltaP `27.5722` edge `0.2209` maxDD `-15.7497`
- `market_context_high->metal_1h` score `0.823` n `87` status `ready` deltaP `11.5235` edge `0.0296` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.789` n `87` status `ready` deltaP `9.1727` edge `0.1764` maxDD `-6.7444`
- `news_risk_high->crypto_major_1h` score `0.742` n `43` status `ready` deltaP `3.3387` edge `0.0793` maxDD `-1.1783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
