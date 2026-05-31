# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T01:37:23.994340+00:00`
- Price records: `672`
- Market context records: `2410`
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

- `news_risk_high->crypto_alt_24h` score `20.3391` n `43` status `ready` deltaP `46.7377` edge `1.4422` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2537` n `43` status `ready` deltaP `49.4105` edge `1.2357` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2155` n `43` status `ready` deltaP `29.7925` edge `1.1008` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.942` n `43` status `ready` deltaP `18.8993` edge `0.8439` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2127` n `43` status `ready` deltaP `27.9877` edge `0.5204` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6308` n `108` status `ready` deltaP `22.4537` edge `0.3607` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3454` n `43` status `ready` deltaP `12.2295` edge `0.4058` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8028` n `131` status `ready` deltaP `23.1358` edge `0.427` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.2445` n `131` status `ready` deltaP `20.8364` edge `0.4827` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6127` n `43` status `ready` deltaP `37.924` edge `0.0667` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2748` n `43` status `ready` deltaP `30.1758` edge `0.2858` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.9573` n `108` status `ready` deltaP `13.0208` edge `0.6816` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4503` n `131` status `ready` deltaP `12.7432` edge `0.1802` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1658` n `43` status `ready` deltaP `27.4319` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7999` n `43` status `ready` deltaP `15.9919` edge `0.1157` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.7957` n `108` status `ready` deltaP `10.9375` edge `0.1198` maxDD `-1.1128`
- `market_context_high->crypto_major_1h` score `1.3806` n `131` status `ready` deltaP `12.6549` edge `0.1501` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1265` n `43` status `ready` deltaP `20.2966` edge `0.0055` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0378` n `131` status `ready` deltaP `9.1077` edge `0.1445` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.579` n `131` status `ready` deltaP `12.4546` edge `0.0478` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
