# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T12:07:26.226977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

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

- `market_context_high->unknown_1h` score `10946.8953` n `118` status `ready` deltaP `2.0071` edge `912.2477` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7457.3261` n `108` status `ready` deltaP `0.5194` edge `621.4688` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4877` n `102` status `ready` deltaP `30.77` edge `1.3448` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.742` n `102` status `ready` deltaP `16.8812` edge `1.1366` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `2.0851` n `108` status `ready` deltaP `6.5322` edge `0.4121` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.8298` n `108` status `ready` deltaP `7.5993` edge `0.3094` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.528` n `108` status `ready` deltaP `17.8693` edge `0.0593` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1993` n `118` status `ready` deltaP `4.8411` edge `0.0176` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3067` n `118` status `ready` deltaP `2.8468` edge `0.0029` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8468` n `118` status `ready` deltaP `3.1944` edge `0.0478` maxDD `-6.5061`
- `market_context_high->fx_1h` score `-1.3303` n `118` status `ready` deltaP `-8.0712` edge `-0.0011` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.3698` n `118` status `ready` deltaP `5.8383` edge `0.0248` maxDD `-10.8962`
- `market_context_high->crypto_alt_1h` score `-1.6588` n `118` status `ready` deltaP `-2.7378` edge `0.0228` maxDD `-7.0893`
- `market_context_high->index_4h` score `-1.6641` n `108` status `ready` deltaP `-0.3952` edge `-0.0017` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.0404` n `118` status `ready` deltaP `-6.1276` edge `-0.016` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3446` n `108` status `ready` deltaP `-14.3405` edge `-0.0034` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.5923` n `102` status `ready` deltaP `14.5425` edge `0.1167` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5515` n `102` status `ready` deltaP `-16.7177` edge `-0.0072` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.7661` n `108` status `ready` deltaP `-26.5187` edge `-0.1011` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.7862` n `108` status `ready` deltaP `-4.3078` edge `-0.0213` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
