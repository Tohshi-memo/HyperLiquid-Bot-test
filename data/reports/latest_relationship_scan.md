# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T00:52:24.679207+00:00`
- Price records: `672`
- Market context records: `6869`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11786`

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

- `market_context_high->unknown_24h` score `1.1541` n `176` status `ready` deltaP `-2.4933` edge `0.5398` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2409` n `224` status `ready` deltaP `2.3872` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5948` n `224` status `ready` deltaP `-0.5988` edge `-0.0038` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6489` n `224` status `ready` deltaP `1.4623` edge `0.0126` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6701` n `224` status `ready` deltaP `3.248` edge `0.0129` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8491` n `224` status `ready` deltaP `-2.2268` edge `-0.0029` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9492` n `224` status `ready` deltaP `-5.4908` edge `-0.0083` maxDD `-2.1427`
- `market_context_high->commodity_24h` score `-0.9788` n `176` status `ready` deltaP `4.7789` edge `0.0734` maxDD `-5.2791`
- `market_context_high->fx_4h` score `-0.9889` n `224` status `ready` deltaP `11.0242` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3475` n `224` status `ready` deltaP `-2.4102` edge `-0.0077` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7141` n `224` status `ready` deltaP `-3.8601` edge `-0.027` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8923` n `224` status `ready` deltaP `0.5881` edge `-0.0285` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.029` n `224` status `ready` deltaP `3.2616` edge `-0.0239` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4344` n `224` status `ready` deltaP `-0.2073` edge `-0.0124` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.146` n `224` status `ready` deltaP `-1.8319` edge `-0.0584` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.18` n `224` status `ready` deltaP `-0.7563` edge `-0.0443` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1997` n `224` status `ready` deltaP `-9.5823` edge `0.0338` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5474` n `176` status `ready` deltaP `-9.7083` edge `-0.0106` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4743` n `224` status `ready` deltaP `0.5022` edge `-0.1671` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9543` n `176` status `ready` deltaP `-18.7599` edge `-0.1744` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
