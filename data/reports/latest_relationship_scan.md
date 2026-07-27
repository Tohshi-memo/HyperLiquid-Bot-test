# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T14:37:32.900692+00:00`
- Price records: `672`
- Market context records: `8100`
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

- `market_context_high->equity_24h` score `20.5821` n `87` status `ready` deltaP `37.4251` edge `1.5567` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5827` n `87` status `ready` deltaP `32.8778` edge `0.544` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3576` n `87` status `ready` deltaP `35.8752` edge `0.4573` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.462` n `43` status `ready` deltaP `30.4453` edge `0.4394` maxDD `-0.6428`
- `news_risk_high->equity_1h` score `3.6623` n `43` status `ready` deltaP `29.0802` edge `0.1422` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.6221` n `43` status `ready` deltaP `14.698` edge `0.2644` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.3581` n `87` status `ready` deltaP `31.893` edge `0.086` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.1804` n `87` status `ready` deltaP `20.4386` edge `0.1958` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.8128` n `43` status `ready` deltaP `4.9053` edge `0.2295` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5709` n `87` status `ready` deltaP `15.4742` edge `0.1544` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4081` n `43` status `ready` deltaP `21.3343` edge `0.0775` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3848` n `87` status `ready` deltaP `21.9109` edge `0.1149` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0534` n `87` status `ready` deltaP `28.2555` edge `0.0531` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.2843` n `43` status `ready` deltaP `13.5174` edge `0.0637` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2728` n `87` status `ready` deltaP `16.3191` edge `0.024` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `1.1295` n `87` status `ready` deltaP `7.4012` edge `0.1565` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `0.9308` n `87` status `ready` deltaP `27.7455` edge `0.2229` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `0.8479` n `87` status `ready` deltaP `9.3251` edge `0.1803` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.8386` n `87` status `ready` deltaP `11.6732` edge `0.0299` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.766` n `43` status `ready` deltaP `3.3387` edge `0.0813` maxDD `-1.1783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
