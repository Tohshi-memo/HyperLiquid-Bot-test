# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T13:52:28.646413+00:00`
- Price records: `672`
- Market context records: `8097`
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

- `market_context_high->equity_24h` score `20.3773` n `87` status `ready` deltaP `36.9051` edge `1.5431` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4615` n `87` status `ready` deltaP `32.8778` edge `0.5339` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3324` n `87` status `ready` deltaP `35.8752` edge `0.4552` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.3408` n `43` status `ready` deltaP `30.4453` edge `0.4293` maxDD `-0.6428`
- `news_risk_high->equity_1h` score `3.5903` n `43` status `ready` deltaP `29.0802` edge `0.1362` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.4824` n `43` status `ready` deltaP `14.2407` edge `0.2558` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.3377` n `87` status `ready` deltaP `31.893` edge `0.0843` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.1088` n `87` status `ready` deltaP `19.9187` edge `0.1933` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7768` n `43` status `ready` deltaP `4.6059` edge `0.2285` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.4989` n `87` status `ready` deltaP `15.4742` edge `0.1484` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.3877` n `43` status `ready` deltaP `21.3343` edge `0.0758` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3338` n `87` status `ready` deltaP `21.4536` edge `0.1137` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.1046` n `87` status `ready` deltaP `28.7754` edge `0.0539` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.244` n `87` status `ready` deltaP `16.1694` edge `0.0226` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.2333` n `43` status `ready` deltaP `13.0601` edge `0.0625` maxDD `-0.7433`
- `market_context_high->crypto_alt_4h` score `0.9933` n `87` status `ready` deltaP `6.9439` edge `0.1482` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `0.8624` n `87` status `ready` deltaP `27.2256` edge `0.2176` maxDD `-15.7497`
- `market_context_high->metal_1h` score `0.8111` n `87` status `ready` deltaP `11.3738` edge `0.0296` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.7552` n `43` status `ready` deltaP `3.3387` edge `0.0804` maxDD `-1.1783`
- `market_context_high->crypto_major_4h` score `0.7082` n `87` status `ready` deltaP `8.8678` edge `0.1717` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
