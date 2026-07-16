# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T12:58:07.317822+00:00`
- Price records: `672`
- Market context records: `6920`
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
- `market_context_high->unknown_24h` score `-0.266` n `203` status `ready` deltaP `-4.9303` edge `0.4004` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3587` n `224` status `ready` deltaP `3.2587` edge `0.0248` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4411` n `224` status `ready` deltaP `4.745` edge `0.022` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6221` n `224` status `ready` deltaP `-0.7485` edge `-0.0063` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7137` n `224` status `ready` deltaP `0.0187` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7378` n `224` status `ready` deltaP `15.2222` edge `0.0103` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.7809` n `224` status `ready` deltaP `-3.0956` edge `-0.0027` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4371` n `224` status `ready` deltaP `-2.7984` edge `-0.0166` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5379` n `224` status `ready` deltaP `-2.3631` edge `-0.0223` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6219` n `224` status `ready` deltaP `3.5821` edge `-0.0138` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.776` n `224` status `ready` deltaP `6.838` edge `-0.0153` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.0528` n `224` status `ready` deltaP `3.9961` edge `0.0085` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6439` n `224` status `ready` deltaP `2.6677` edge `0.0016` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7446` n `224` status `ready` deltaP `0.2177` edge `-0.0206` maxDD `-16.9508`
- `market_context_high->commodity_24h` score `-2.8962` n `203` status `ready` deltaP `-2.4938` edge `-0.0379` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-2.9087` n `224` status `ready` deltaP `-7.0558` edge `0.0412` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0303` n `203` status `ready` deltaP `-3.9639` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.8535` n `224` status `ready` deltaP `4.2356` edge `-0.1124` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2986` n `203` status `ready` deltaP `-11.8278` edge `-0.1122` maxDD `-29.4965`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
