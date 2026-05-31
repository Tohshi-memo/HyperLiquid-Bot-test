# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T10:22:17.572527+00:00`
- Price records: `672`
- Market context records: `2447`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.2604` n `43` status `ready` deltaP `43.4391` edge `1.3743` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.0967` n `43` status `ready` deltaP `54.098` edge `1.2747` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7379` n `43` status `ready` deltaP `29.7925` edge `1.061` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.3994` n `43` status `ready` deltaP `16.6424` edge `0.7304` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `6.9197` n `43` status `ready` deltaP `23.3002` edge `0.4439` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9662` n `108` status `ready` deltaP `22.3958` edge `0.3807` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.1048` n `124` status `ready` deltaP `23.5199` edge `0.4496` maxDD `-10.1468`
- `news_risk_high->index_24h` score `4.9591` n `43` status `ready` deltaP `8.9309` edge `0.3956` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.8784` n `124` status `ready` deltaP `23.4952` edge `0.5178` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1823` n `43` status `ready` deltaP `28.6514` edge `0.2841` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1396` n `43` status `ready` deltaP `32.7156` edge `0.062` maxDD `-0.1442`
- `market_context_high->unknown_4h` score `2.5774` n `124` status `ready` deltaP `12.9229` edge `0.1896` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.5254` n `108` status `ready` deltaP `11.6898` edge `0.6351` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6477` n `43` status `ready` deltaP `15.2297` edge `0.1081` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.5668` n `108` status `ready` deltaP `7.6389` edge `0.1152` maxDD `-0.5117`
- `news_risk_high->unknown_1h` score `1.1529` n `43` status `ready` deltaP `20.596` edge `0.0057` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.8069` n `136` status `ready` deltaP `8.9336` edge `0.1271` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.6996` n `136` status `ready` deltaP `7.6259` edge `0.1262` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5927` n `124` status `ready` deltaP `13.0606` edge `0.0449` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
