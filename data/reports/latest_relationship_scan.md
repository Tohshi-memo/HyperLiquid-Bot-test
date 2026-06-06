# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T19:22:20.412562+00:00`
- Price records: `672`
- Market context records: `3104`
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

- `market_context_high->crypto_alt_24h` score `16.5712` n `84` status `ready` deltaP `14.2113` edge `2.5608` maxDD `-33.816`
- `market_context_high->commodity_24h` score `15.0647` n `84` status `ready` deltaP `45.3621` edge `0.9958` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.7702` n `84` status `ready` deltaP `23.5119` edge `1.1229` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.5993` n `84` status `ready` deltaP `32.5893` edge `0.9152` maxDD `-15.6019`
- `market_context_high->equity_24h` score `7.3352` n `84` status `ready` deltaP `17.9811` edge `1.3681` maxDD `-37.4717`
- `market_context_high->commodity_4h` score `3.0577` n `119` status `ready` deltaP `18.4657` edge `0.1775` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.1541` n `122` status `ready` deltaP `0.6626` edge `0.025` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4751` n `122` status `ready` deltaP `4.4051` edge `0.016` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6325` n `84` status `ready` deltaP `3.3978` edge `-0.0026` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.7245` n `122` status `ready` deltaP `-7.5979` edge `-0.0038` maxDD `-0.4083`
- `market_context_high->crypto_alt_1h` score `-0.7469` n `122` status `ready` deltaP `3.7351` edge `0.0923` maxDD `-14.7034`
- `market_context_high->unknown_4h` score `-1.0694` n `119` status `ready` deltaP `5.2432` edge `0.0369` maxDD `-10.5444`
- `market_context_high->equity_1h` score `-1.265` n `122` status `ready` deltaP `-2.1596` edge `0.0008` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3105` n `119` status `ready` deltaP `-12.0362` edge `-0.0034` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4417` n `119` status `ready` deltaP `9.3552` edge `0.0437` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.1964` n `122` status `ready` deltaP `-1.0111` edge `0.05` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3671` n `122` status `ready` deltaP `-6.9132` edge `-0.0118` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.9676` n `122` status `ready` deltaP `3.0357` edge `-0.0726` maxDD `-13.5949`
- `market_context_high->crypto_alt_4h` score `-3.8876` n `119` status `ready` deltaP `12.6115` edge `0.222` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1134` n `119` status `ready` deltaP `5.5364` edge `-0.0337` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
