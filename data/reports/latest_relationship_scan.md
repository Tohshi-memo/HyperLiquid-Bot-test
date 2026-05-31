# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T09:07:19.917265+00:00`
- Price records: `672`
- Market context records: `2442`
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

- `news_risk_high->crypto_alt_24h` score `19.2477` n `43` status `ready` deltaP `43.2655` edge `1.3744` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.9745` n `43` status `ready` deltaP `53.23` edge `1.2703` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8087` n `43` status `ready` deltaP `29.7925` edge `1.0669` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.5616` n `43` status `ready` deltaP `16.9896` edge `0.7416` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.0847` n `43` status `ready` deltaP `23.4738` edge `0.4565` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7638` n `104` status `ready` deltaP `22.3558` edge `0.3641` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9627` n `43` status `ready` deltaP `8.9309` edge `0.3959` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.9322` n `124` status `ready` deltaP `22.7577` edge `0.4403` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.8048` n `124` status `ready` deltaP `23.1904` edge `0.5137` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.2127` n `43` status `ready` deltaP `33.5837` edge `0.0623` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1847` n `43` status `ready` deltaP `28.8038` edge `0.2834` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.6982` n `124` status `ready` deltaP `13.5327` edge `0.1956` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.3506` n `104` status `ready` deltaP `10.6837` edge `0.6194` maxDD `-25.1408`
- `market_context_high->index_24h` score `2.1237` n `104` status `ready` deltaP `10.6303` edge `0.1318` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7685` n `43` status `ready` deltaP `15.8395` edge `0.1141` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0653` n `43` status `ready` deltaP `20.1469` edge `0.0014` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `1.0509` n `131` status `ready` deltaP `10.8139` edge `0.1349` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.8243` n `131` status `ready` deltaP `8.1947` edge `0.1328` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5757` n `124` status `ready` deltaP `12.9082` edge `0.0445` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
