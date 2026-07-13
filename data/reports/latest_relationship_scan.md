# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T17:37:26.348290+00:00`
- Price records: `672`
- Market context records: `6625`
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

- `market_context_high->unknown_24h` score `2.4879` n `181` status `ready` deltaP `-0.5554` edge `0.494` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.1672` n `203` status `ready` deltaP `-6.2395` edge `0.3123` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.286` n `181` status `ready` deltaP `8.7528` edge `0.1523` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0269` n `203` status `ready` deltaP `8.2151` edge `0.0361` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2633` n `203` status `ready` deltaP `2.4866` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.3352` n `203` status `ready` deltaP `5.4526` edge `0.0288` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5194` n `203` status `ready` deltaP `0.0723` edge `0.0047` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6139` n `203` status `ready` deltaP `-0.6902` edge `-0.0058` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8294` n `203` status `ready` deltaP `10.6264` edge `0.0108` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.885` n `203` status `ready` deltaP `2.9026` edge `0.0096` maxDD `-3.8827`
- `market_context_high->unknown_4h` score `-1.0901` n `203` status `ready` deltaP `-16.7961` edge `0.2617` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-1.1413` n `203` status `ready` deltaP `-3.2071` edge `0.0004` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.2946` n `203` status `ready` deltaP `-0.8546` edge `-0.0108` maxDD `-5.6246`
- `market_context_high->crypto_major_4h` score `-1.381` n `203` status `ready` deltaP `9.1952` edge `0.0931` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.5648` n `203` status `ready` deltaP `3.1652` edge `-0.0005` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.7925` n `203` status `ready` deltaP `6.0404` edge `0.0701` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0276` n `203` status `ready` deltaP `0.1502` edge `0.0251` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4475` n `203` status `ready` deltaP `8.9834` edge `-0.0036` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-4.6998` n `181` status `ready` deltaP `-1.9719` edge `0.0381` maxDD `-17.8664`
- `market_context_high->fx_24h` score `-5.8872` n `181` status `ready` deltaP `-8.6858` edge `-0.0028` maxDD `-9.7252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
