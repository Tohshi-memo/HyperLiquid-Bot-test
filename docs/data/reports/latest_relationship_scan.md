# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T23:07:34.170551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11823`

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

- `market_context_high->unknown_24h` score `17.6922` n `81` status `ready` deltaP `18.0362` edge `1.3584` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4085` n `90` status `ready` deltaP `1.7479` edge `0.5386` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6272` n `90` status `ready` deltaP `17.6897` edge `0.1023` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.0836` n `81` status `ready` deltaP `0.4437` edge `0.2528` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8737` n `81` status `ready` deltaP `22.8588` edge `0.0802` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3013` n `90` status `ready` deltaP `5.7917` edge `0.0281` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0991` n `90` status `ready` deltaP `7.006` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0854` n `90` status `ready` deltaP `13.4621` edge `0.0072` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.3903` n `81` status `ready` deltaP `6.5201` edge `0.0508` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5503` n `90` status `ready` deltaP `-1.7565` edge `-0.0094` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5713` n `90` status `ready` deltaP `-0.1563` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6935` n `90` status `ready` deltaP `3.4891` edge `0.0113` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7499` n `90` status `ready` deltaP `-2.4584` edge `-0.0087` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-0.985` n `90` status `ready` deltaP `3.1809` edge `-0.0085` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7048` n `90` status `ready` deltaP `4.3513` edge `-0.094` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.8584` n `81` status `ready` deltaP `-6.5201` edge `0.0247` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.0279` n `90` status `ready` deltaP `-11.8259` edge `-0.0557` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.4033` n `90` status `ready` deltaP `-11.2608` edge `-0.0712` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.43` n `90` status `ready` deltaP `1.8995` edge `-0.2538` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-5.5673` n `81` status `ready` deltaP `6.3465` edge `-0.1034` maxDD `-40.5468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
