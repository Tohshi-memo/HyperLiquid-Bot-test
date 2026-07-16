# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T13:22:28.567049+00:00`
- Price records: `672`
- Market context records: `6922`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1701` n `224` status `ready` deltaP `3.5848` edge `0.0028` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2531` n `203` status `ready` deltaP `-4.757` edge `0.4009` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3587` n `224` status `ready` deltaP `3.2587` edge `0.0248` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4339` n `224` status `ready` deltaP `4.745` edge `0.0226` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6237` n `224` status `ready` deltaP `-0.7485` edge `-0.0065` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7035` n `224` status `ready` deltaP `0.1684` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7465` n `224` status `ready` deltaP `15.0697` edge `0.0102` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.756` n `224` status `ready` deltaP `-2.7962` edge `-0.0015` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4818` n `224` status `ready` deltaP `-3.1033` edge `-0.0203` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5091` n `224` status `ready` deltaP `-2.0637` edge `-0.0219` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6149` n `224` status `ready` deltaP `3.5821` edge `-0.0129` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7508` n `224` status `ready` deltaP `7.1429` edge `-0.0141` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.0175` n `224` status `ready` deltaP `4.3009` edge `0.011` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6581` n `224` status `ready` deltaP `2.5152` edge `0.0008` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7304` n `224` status `ready` deltaP `0.3702` edge `-0.0198` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9039` n `224` status `ready` deltaP `-7.0558` edge `0.0416` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-2.9719` n `203` status `ready` deltaP `-2.8404` edge `-0.0419` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.064` n `203` status `ready` deltaP `-4.3105` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.7963` n `224` status `ready` deltaP `4.5405` edge `-0.1071` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2603` n `203` status `ready` deltaP `-11.4812` edge `-0.1096` maxDD `-29.4965`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
