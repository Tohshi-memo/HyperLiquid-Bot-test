# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T07:52:30.380407+00:00`
- Price records: `672`
- Market context records: `6898`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `0.5269` n `185` status `ready` deltaP `-4.3019` edge `0.4836` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2292` n `224` status `ready` deltaP `2.5369` edge `0.0022` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4763` n `224` status `ready` deltaP `2.6599` edge `0.019` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5586` n `224` status `ready` deltaP `4.1462` edge `0.0162` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.5871` n `224` status `ready` deltaP `-0.4491` edge `-0.0038` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7946` n `224` status `ready` deltaP `-1.1789` edge `-0.0029` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8168` n `224` status `ready` deltaP `14.0027` edge `0.0083` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8612` n `224` status `ready` deltaP `-3.9938` edge `-0.007` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3287` n `224` status `ready` deltaP `-1.8838` edge `-0.0088` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7081` n `224` status `ready` deltaP `-3.8601` edge `-0.0265` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8019` n `224` status `ready` deltaP `1.7857` edge `-0.0249` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.974` n `224` status `ready` deltaP `4.0941` edge `-0.0224` maxDD `-11.3047`
- `market_context_high->commodity_24h` score `-2.0188` n `185` status `ready` deltaP `1.1981` edge `0.0106` maxDD `-5.2791`
- `market_context_high->metal_4h` score `-2.2606` n `224` status `ready` deltaP `1.7095` edge `-0.0029` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8931` n `224` status `ready` deltaP `1.2957` edge `-0.0212` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.9654` n `224` status `ready` deltaP `-0.8493` edge `-0.0418` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0849` n `224` status `ready` deltaP `-8.7326` edge `0.0377` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2662` n `185` status `ready` deltaP `-6.7029` edge `-0.0072` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3027` n `224` status `ready` deltaP `1.4917` edge `-0.1517` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.4521` n `185` status `ready` deltaP `-14.0147` edge `-0.1316` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
