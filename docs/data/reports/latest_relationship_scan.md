# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T01:07:25.606036+00:00`
- Price records: `672`
- Market context records: `3130`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7125`

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

- `market_context_high->commodity_24h` score `14.2322` n `106` status `ready` deltaP `47.5858` edge `0.9116` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.672` n `106` status `ready` deltaP `20.7842` edge `0.8829` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7714` n `106` status `ready` deltaP `10.0727` edge `2.3114` maxDD `-71.142`
- `market_context_high->index_24h` score `6.445` n `106` status `ready` deltaP `30.5293` edge `0.8782` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3364` n `106` status `ready` deltaP `10.8556` edge `1.3252` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0847` n `133` status `ready` deltaP `19.9741` edge `0.1697` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0846` n `145` status `ready` deltaP `3.376` edge `0.0268` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4401` n `145` status `ready` deltaP `4.6593` edge `0.0188` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4524` n `145` status `ready` deltaP `5.7392` edge `0.1167` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4657` n `106` status `ready` deltaP `5.3328` edge `-0.0016` maxDD `-0.4876`
- `market_context_high->equity_1h` score `-0.8595` n `145` status `ready` deltaP `2.7132` edge `0.0203` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.02` n `145` status `ready` deltaP `2.8525` edge `0.0765` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.182` n `145` status `ready` deltaP `-11.6519` edge `-0.0056` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2795` n `133` status `ready` deltaP `11.065` edge `0.0531` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.5089` n `133` status `ready` deltaP `-14.6307` edge `-0.0087` maxDD `-1.3104`
- `market_context_high->metal_1h` score `-1.9943` n `145` status `ready` deltaP `-3.6486` edge `-0.0025` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2318` n `133` status `ready` deltaP `3.6058` edge `0.0122` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-3.038` n `133` status `ready` deltaP `16.7981` edge `0.303` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0492` n `145` status `ready` deltaP `2.2104` edge `-0.0662` maxDD `-14.2111`
- `market_context_high->equity_4h` score `-3.45` n `133` status `ready` deltaP `10.3131` edge `0.0195` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
