# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T01:07:18.181392+00:00`
- Price records: `672`
- Market context records: `2408`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.4628` n `43` status `ready` deltaP `47.0849` edge `1.4502` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2117` n `43` status `ready` deltaP `49.4105` edge `1.2322` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2455` n `43` status `ready` deltaP `29.7925` edge `1.1033` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.0236` n `43` status `ready` deltaP `18.8993` edge `0.8507` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2223` n `43` status `ready` deltaP `27.9877` edge `0.5212` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5664` n `110` status `ready` deltaP `22.6389` edge `0.3541` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3604` n `43` status `ready` deltaP `12.4031` edge `0.4059` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8544` n `133` status `ready` deltaP `23.4802` edge `0.429` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.1786` n `133` status `ready` deltaP `21.0022` edge `0.4761` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6091` n `43` status `ready` deltaP `37.924` edge `0.0664` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2693` n `43` status `ready` deltaP `30.1758` edge `0.2851` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0149` n `110` status `ready` deltaP `13.6774` edge `0.6846` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.5177` n `133` status `ready` deltaP `13.0467` edge `0.1838` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1658` n `43` status `ready` deltaP `27.4319` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7395` n `43` status `ready` deltaP `15.687` edge `0.1127` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.6521` n `110` status `ready` deltaP `10.606` edge `0.1147` maxDD `-1.1522`
- `market_context_high->crypto_major_1h` score `1.4255` n `133` status `ready` deltaP `13.1714` edge `0.1504` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1337` n `43` status `ready` deltaP `20.2966` edge `0.0061` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0314` n `133` status `ready` deltaP `9.1025` edge `0.144` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.6602` n `133` status `ready` deltaP `12.7499` edge `0.0526` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
