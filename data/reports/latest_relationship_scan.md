# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T20:22:31.266950+00:00`
- Price records: `672`
- Market context records: `6851`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.0902` n `176` status `ready` deltaP `-1.5467` edge `0.5253` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2523` n `223` status `ready` deltaP `2.169` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3909` n `176` status `ready` deltaP `7.1023` edge `0.1069` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.5809` n `223` status `ready` deltaP `1.8622` edge `0.0156` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6058` n `223` status `ready` deltaP `3.8056` edge `0.0143` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6875` n `223` status `ready` deltaP `-2.171` edge `-0.0052` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8896` n `223` status `ready` deltaP `-2.9148` edge `-0.0035` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9573` n `223` status `ready` deltaP `-5.602` edge `-0.0086` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0057` n `215` status `ready` deltaP `10.6998` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4784` n `215` status `ready` deltaP `-4.0279` edge `-0.0137` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6454` n `223` status `ready` deltaP `-2.9115` edge `-0.0276` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9963` n `223` status `ready` deltaP `-0.527` edge `-0.0344` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.1035` n `215` status `ready` deltaP `2.3235` edge `-0.0272` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.5167` n `215` status `ready` deltaP `-1.2797` edge `-0.0158` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0546` n `215` status `ready` deltaP `-0.7488` edge `-0.0539` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1811` n `215` status `ready` deltaP `-0.6275` edge `-0.0453` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2018` n `215` status `ready` deltaP `-9.3392` edge `0.032` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.496` n `176` status `ready` deltaP `-9.7853` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.7343` n `215` status `ready` deltaP `-0.6587` edge `-0.1927` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.1038` n `176` status `ready` deltaP `-18.8447` edge `-0.193` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
