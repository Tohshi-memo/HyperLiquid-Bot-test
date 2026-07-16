# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T00:37:25.794187+00:00`
- Price records: `672`
- Market context records: `6868`
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

- `market_context_high->unknown_24h` score `1.1654` n `176` status `ready` deltaP `-2.32` edge `0.5401` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2487` n `224` status `ready` deltaP `2.2375` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6026` n `224` status `ready` deltaP `-0.7485` edge `-0.0038` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6632` n `224` status `ready` deltaP `1.3126` edge `0.0124` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6868` n `224` status `ready` deltaP `3.0983` edge `0.0125` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8585` n `224` status `ready` deltaP `-2.3765` edge `-0.0031` maxDD `-2.2895`
- `market_context_high->commodity_24h` score `-0.956` n `176` status `ready` deltaP `4.7789` edge `0.0753` maxDD `-5.2791`
- `market_context_high->metal_1h` score `-0.9577` n `224` status `ready` deltaP `-5.6405` edge `-0.0084` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9842` n `223` status `ready` deltaP `11.1282` edge `0.006` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3306` n `223` status `ready` deltaP `-2.1759` edge `-0.0071` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7141` n `224` status `ready` deltaP `-3.8601` edge `-0.027` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9063` n `224` status `ready` deltaP `0.4384` edge `-0.0293` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0228` n `223` status `ready` deltaP `3.3656` edge `-0.0238` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4317` n `223` status `ready` deltaP `-0.1693` edge `-0.0123` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1352` n `223` status `ready` deltaP `-1.7439` edge `-0.0576` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1747` n `223` status `ready` deltaP `-0.6703` edge `-0.0442` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2055` n `223` status `ready` deltaP `-9.7304` edge `0.0343` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.545` n `176` status `ready` deltaP `-9.7083` edge `-0.0104` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4733` n `223` status `ready` deltaP `0.5802` edge `-0.1675` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9636` n `176` status `ready` deltaP `-18.7599` edge `-0.1756` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
