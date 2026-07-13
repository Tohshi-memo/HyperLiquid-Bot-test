# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T19:37:26.260148+00:00`
- Price records: `672`
- Market context records: `6634`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.3255` n `203` status `ready` deltaP `-5.6407` edge `0.3215` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.457` n `189` status `ready` deltaP `-1.4958` edge `0.4477` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5715` n `189` status `ready` deltaP `10.1326` edge `0.1669` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1072` n `203` status `ready` deltaP `8.8139` edge `0.0493` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1098` n `203` status `ready` deltaP `6.2011` edge `0.0426` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4758` n `203` status `ready` deltaP `0.8208` edge `0.0053` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.663` n `203` status `ready` deltaP `-1.289` edge `-0.0081` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7407` n `203` status `ready` deltaP `-15.729` edge `0.2837` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-0.7867` n `203` status `ready` deltaP `3.6511` edge `0.0128` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.8066` n `203` status `ready` deltaP `10.7788` edge `0.0127` maxDD `-5.7046`
- `market_context_high->crypto_major_4h` score `-1.0773` n `203` status `ready` deltaP `10.4147` edge `0.1239` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1281` n `203` status `ready` deltaP `-3.0574` edge `0.0005` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.3909` n `203` status `ready` deltaP `-1.3119` edge `-0.0201` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4733` n `203` status `ready` deltaP `7.26` edge `0.1029` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4974` n `203` status `ready` deltaP `4.3847` edge `0.0` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.926` n `203` status `ready` deltaP `1.3697` edge `0.03` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3503` n `203` status `ready` deltaP `8.9834` edge `0.0045` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.5545` n `189` status `ready` deltaP `-2.8561` edge `0.0251` maxDD `-22.4543`
- `market_context_high->fx_24h` score `-6.1498` n `189` status `ready` deltaP `-10.1124` edge `-0.0058` maxDD `-10.475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
