# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T03:37:26.623256+00:00`
- Price records: `672`
- Market context records: `8158`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `20.7524` n `72` status `ready` deltaP `44.4445` edge `1.5241` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.6866` n `73` status `ready` deltaP `37.6629` edge `0.5796` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.6903` n `43` status `ready` deltaP `32.8843` edge `0.5255` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.5422` n `72` status `ready` deltaP `39.7569` edge `0.4468` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.318` n `43` status `ready` deltaP `19.576` edge `0.3732` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9567` n `73` status `ready` deltaP `36.1364` edge `0.0931` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.8962` n `43` status `ready` deltaP `29.8287` edge `0.1567` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.6282` n `73` status `ready` deltaP `20.0804` edge `0.1888` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.4686` n `72` status `ready` deltaP `22.9167` edge `0.2033` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.7618` n `43` status `ready` deltaP `23.0112` edge `0.0958` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3615` n `73` status `ready` deltaP `23.509` edge `0.1023` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0081` n `72` status `ready` deltaP `26.9097` edge `0.0583` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.8008` n `73` status `ready` deltaP `8.7579` edge `0.2034` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.7422` n `73` status `ready` deltaP `11.0382` edge `0.2434` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.6511` n `73` status `ready` deltaP `19.7133` edge `0.0258` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.5996` n `43` status `ready` deltaP `15.1942` edge `0.0788` maxDD `-0.7433`
- `market_context_high->commodity_24h` score `1.5729` n `72` status `ready` deltaP `31.4236` edge `0.2807` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `1.3535` n `43` status `ready` deltaP `6.3327` edge `0.1103` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `1.2457` n `73` status `ready` deltaP `13.1183` edge `0.0574` maxDD `-1.6171`
- `news_risk_high->crypto_alt_4h` score `1.0975` n `43` status `ready` deltaP `12.1029` edge `0.1992` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
