# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T15:37:31.350567+00:00`
- Price records: `672`
- Market context records: `8105`
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

- `market_context_high->equity_24h` score `20.9915` n `87` status `ready` deltaP `38.1183` edge `1.5862` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.8643` n `87` status `ready` deltaP `33.4875` edge `0.5634` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3876` n `87` status `ready` deltaP `35.8752` edge `0.4598` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7436` n `43` status `ready` deltaP `31.055` edge `0.4588` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `3.9097` n `43` status `ready` deltaP `15.3078` edge `0.2843` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7319` n `43` status `ready` deltaP `29.2299` edge `0.147` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.4075` n `87` status `ready` deltaP `32.0455` edge `0.0891` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.291` n `87` status `ready` deltaP `21.1319` edge `0.2004` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.8212` n `43` status `ready` deltaP `4.9053` edge `0.2302` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.6405` n `87` status `ready` deltaP `15.6239` edge `0.1592` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4575` n `43` status `ready` deltaP `21.4868` edge `0.0806` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4212` n `87` status `ready` deltaP `22.2158` edge `0.1159` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9919` n `87` status `ready` deltaP `27.5623` edge `0.0526` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.4039` n `87` status `ready` deltaP `8.0109` edge `0.1753` maxDD `-3.9374`
- `news_risk_high->metal_4h` score `1.3207` n `43` status `ready` deltaP `13.8223` edge `0.0647` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.3063` n `87` status `ready` deltaP `16.6185` edge `0.0248` maxDD `-0.4716`
- `market_context_high->crypto_major_4h` score `1.1355` n `87` status `ready` deltaP `9.9349` edge `0.2002` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.0277` n `87` status `ready` deltaP `28.4388` edge `0.2307` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.9063` n `43` status `ready` deltaP `3.7878` edge `0.09` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.853` n `87` status `ready` deltaP `11.8229` edge `0.0301` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
