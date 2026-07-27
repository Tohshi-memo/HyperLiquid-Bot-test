# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T15:22:28.058780+00:00`
- Price records: `672`
- Market context records: `8104`
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

- `market_context_high->equity_24h` score `20.8709` n `87` status `ready` deltaP `37.945` edge `1.5773` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.7921` n `87` status `ready` deltaP `33.3351` edge `0.5584` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3792` n `87` status `ready` deltaP `35.8752` edge `0.4591` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.6714` n `43` status `ready` deltaP `30.9026` edge `0.4538` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `3.8363` n `43` status `ready` deltaP `15.1553` edge `0.2792` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7283` n `43` status `ready` deltaP `29.2299` edge `0.1467` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.3967` n `87` status `ready` deltaP `32.0455` edge `0.0882` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.2604` n `87` status `ready` deltaP `20.9586` edge `0.199` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.82` n `43` status `ready` deltaP `4.9053` edge `0.2301` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.6369` n `87` status `ready` deltaP `15.6239` edge `0.1589` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4467` n `43` status `ready` deltaP `21.4868` edge `0.0797` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.42` n `87` status `ready` deltaP `22.2158` edge `0.1158` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.007` n `87` status `ready` deltaP `27.7356` edge `0.0527` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.3317` n `87` status `ready` deltaP `7.8585` edge `0.1703` maxDD `-3.9374`
- `news_risk_high->metal_4h` score `1.3195` n `43` status `ready` deltaP `13.8223` edge `0.0646` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.292` n `87` status `ready` deltaP `16.4688` edge `0.0246` maxDD `-0.4716`
- `market_context_high->crypto_major_4h` score `1.0621` n `87` status `ready` deltaP `9.7824` edge `0.1951` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.0007` n `87` status `ready` deltaP `28.2655` edge `0.2284` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.8811` n `43` status `ready` deltaP `3.6381` edge `0.0889` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8542` n `87` status `ready` deltaP `11.8229` edge `0.0302` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
