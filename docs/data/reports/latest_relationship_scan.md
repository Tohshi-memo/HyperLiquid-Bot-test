# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T05:22:26.478983+00:00`
- Price records: `672`
- Market context records: `6888`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `0.451` n `185` status `ready` deltaP `-5.3417` edge `0.4808` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2144` n `224` status `ready` deltaP `2.8363` edge `0.0021` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5458` n `224` status `ready` deltaP `2.2108` edge `0.0162` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6113` n `224` status `ready` deltaP `3.6971` edge `0.0148` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.612` n `224` status `ready` deltaP `-0.8982` edge `-0.004` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8009` n `224` status `ready` deltaP `-1.3286` edge `-0.0027` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8832` n `224` status `ready` deltaP `12.9356` edge `0.0069` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8939` n `224` status `ready` deltaP `-4.5926` edge `-0.0072` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3146` n `224` status `ready` deltaP `-1.8838` edge `-0.007` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6242` n `224` status `ready` deltaP `-3.1116` edge `-0.0245` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8058` n `224` status `ready` deltaP `1.636` edge `-0.0244` maxDD `-13.1084`
- `market_context_high->commodity_24h` score `-1.834` n `185` status `ready` deltaP `1.1981` edge `0.026` maxDD `-5.2791`
- `market_context_high->index_4h` score `-2.0174` n `224` status `ready` deltaP `3.4844` edge `-0.0239` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3605` n `224` status `ready` deltaP `0.7948` edge `-0.0096` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0828` n `224` status `ready` deltaP `-1.3066` edge `-0.0538` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0947` n `224` status `ready` deltaP `-0.0762` edge `-0.0379` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1905` n `224` status `ready` deltaP `-9.6472` edge `0.035` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2379` n `185` status `ready` deltaP `-6.5296` edge `-0.006` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3936` n `224` status `ready` deltaP `1.0344` edge `-0.1603` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.6231` n `185` status `ready` deltaP `-15.0546` edge `-0.1466` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
