# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T19:51:19.800244+00:00`
- Price records: `672`
- Market context records: `3106`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.5153` n `86` status `ready` deltaP `14.3976` edge `2.5524` maxDD `-33.816`
- `market_context_high->commodity_24h` score `14.9634` n `86` status `ready` deltaP `45.6113` edge `0.9857` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.3519` n `86` status `ready` deltaP `22.9934` edge `1.0915` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.2868` n `86` status `ready` deltaP `31.137` edge `0.9051` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.8641` n `86` status `ready` deltaP `17.0825` edge `1.3526` maxDD `-39.918`
- `market_context_high->commodity_4h` score `2.993` n `120` status `ready` deltaP `17.9878` edge `0.1753` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.1705` n `124` status `ready` deltaP `0.623` edge `0.0239` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4881` n `124` status `ready` deltaP `4.2158` edge `0.0156` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5953` n `86` status `ready` deltaP `3.7427` edge `-0.0018` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7374` n `124` status `ready` deltaP `3.8584` edge `0.0927` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.7747` n `124` status `ready` deltaP `-8.1225` edge `-0.0048` maxDD `-0.5632`
- `market_context_high->equity_1h` score `-1.2007` n `124` status `ready` deltaP `-1.3135` edge `0.0034` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.2948` n `120` status `ready` deltaP `-11.8089` edge `-0.0029` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4605` n `120` status `ready` deltaP `9.0244` edge `0.0435` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.8572` n `120` status `ready` deltaP `4.8984` edge `0.0143` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.2755` n `124` status `ready` deltaP `-1.6854` edge `0.0479` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3318` n `124` status `ready` deltaP `-6.5917` edge `-0.011` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-3.1783` n `124` status `ready` deltaP `2.1103` edge `-0.0793` maxDD `-13.9704`
- `market_context_high->crypto_alt_4h` score `-3.9375` n `120` status `ready` deltaP `12.2053` edge `0.2183` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0656` n `120` status `ready` deltaP `5.9146` edge `-0.0301` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
