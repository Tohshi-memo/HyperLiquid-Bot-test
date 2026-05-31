# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T09:36:19.830264+00:00`
- Price records: `672`
- Market context records: `2444`
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

- `news_risk_high->crypto_alt_24h` score `19.2254` n `43` status `ready` deltaP `43.0919` edge `1.3737` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.0214` n `43` status `ready` deltaP `53.5772` edge `1.2719` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7811` n `43` status `ready` deltaP `29.7925` edge `1.0646` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.4853` n `43` status `ready` deltaP `16.816` edge `0.7364` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.0247` n `43` status `ready` deltaP `23.4738` edge `0.4515` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8853` n `106` status `ready` deltaP `22.4646` edge `0.3735` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.9962` n `124` status `ready` deltaP `23.0626` edge `0.4436` maxDD `-10.1468`
- `news_risk_high->index_24h` score `4.9639` n `43` status `ready` deltaP `8.9309` edge `0.396` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.8228` n `124` status `ready` deltaP `23.1904` edge `0.5152` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1894` n `43` status `ready` deltaP `28.8038` edge `0.284` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1825` n `43` status `ready` deltaP `33.2365` edge `0.0621` maxDD `-0.1442`
- `market_context_high->unknown_4h` score `2.6512` n `124` status `ready` deltaP `13.3802` edge `0.1927` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.4531` n `106` status `ready` deltaP `11.1995` edge `0.6291` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1098` n `43` status `ready` deltaP `26.8221` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.901` n `106` status `ready` deltaP `9.1064` edge `0.1234` maxDD `-0.3888`
- `news_risk_high->unknown_4h` score `1.7215` n `43` status `ready` deltaP `15.687` edge `0.1112` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0461` n `43` status `ready` deltaP `20.1469` edge `-0.0002` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.9291` n `133` status `ready` deltaP `9.8611` edge `0.1311` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7685` n `133` status `ready` deltaP `7.9015` edge `0.1301` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5927` n `124` status `ready` deltaP `13.0606` edge `0.0449` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
