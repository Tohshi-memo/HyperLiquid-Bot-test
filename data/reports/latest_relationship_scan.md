# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T17:22:25.065039+00:00`
- Price records: `672`
- Market context records: `6624`
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

- `market_context_high->unknown_24h` score `2.6138` n `180` status `ready` deltaP `-0.446` edge `0.4996` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.1648` n `203` status `ready` deltaP `-6.2395` edge `0.3121` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2583` n `180` status `ready` deltaP `8.5717` edge `0.1512` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0355` n `203` status `ready` deltaP `8.0654` edge `0.036` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2633` n `203` status `ready` deltaP `2.4866` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.358` n `203` status `ready` deltaP `5.3029` edge `0.0279` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5194` n `203` status `ready` deltaP `0.0723` edge `0.0047` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6108` n `203` status `ready` deltaP `-0.6902` edge `-0.0054` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8309` n `203` status `ready` deltaP `10.6264` edge `0.0106` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9006` n `203` status `ready` deltaP `2.7529` edge `0.0093` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1269` n `203` status `ready` deltaP `-3.0574` edge `0.0006` maxDD `-1.5966`
- `market_context_high->unknown_4h` score `-1.1347` n `203` status `ready` deltaP `-16.9485` edge `0.259` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.2789` n `203` status `ready` deltaP `-0.7022` edge `-0.0098` maxDD `-5.6246`
- `market_context_high->crypto_major_4h` score `-1.4186` n `203` status `ready` deltaP `9.0427` edge `0.0893` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.5727` n `203` status `ready` deltaP `3.0127` edge `-0.0005` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.8332` n `203` status `ready` deltaP `5.888` edge `0.0659` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.041` n `203` status `ready` deltaP `-0.0022` edge `0.0244` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4607` n `203` status `ready` deltaP `8.9834` edge `-0.0047` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-4.6013` n `180` status `ready` deltaP `-1.9608` edge `0.0395` maxDD `-17.3067`
- `market_context_high->fx_24h` score `-5.8554` n `180` status `ready` deltaP `-8.4986` edge `-0.0025` maxDD `-9.6369`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
