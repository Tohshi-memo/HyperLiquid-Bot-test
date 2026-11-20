# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T12:22:25.685589+00:00`
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

- `market_context_high->unknown_1h` score `10845.5867` n `119` status `ready` deltaP `2.0996` edge `903.8047` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.8893` n `108` status `ready` deltaP `0.5194` edge `621.4324` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4997` n `102` status `ready` deltaP `30.77` edge `1.3458` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.7612` n `102` status `ready` deltaP `16.8812` edge `1.1382` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `2.1285` n `108` status `ready` deltaP `6.6847` edge `0.4147` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.8756` n `108` status `ready` deltaP `7.7518` edge `0.3122` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.528` n `108` status `ready` deltaP `17.8693` edge `0.0593` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.2251` n `119` status `ready` deltaP `4.5778` edge `0.0172` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3205` n `119` status `ready` deltaP `2.5977` edge `0.0028` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.032` n `119` status `ready` deltaP `2.9311` edge `0.0429` maxDD `-7.2088`
- `market_context_high->fx_1h` score `-1.2869` n `119` status `ready` deltaP `-7.5442` edge `-0.001` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.4425` n `119` status `ready` deltaP `5.5678` edge `0.0226` maxDD `-11.0605`
- `market_context_high->index_4h` score `-1.6653` n `108` status `ready` deltaP `-0.3952` edge `-0.0018` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.8127` n `119` status `ready` deltaP `-2.9513` edge `0.0192` maxDD `-7.7133`
- `market_context_high->commodity_1h` score `-1.9951` n `119` status `ready` deltaP `-5.622` edge `-0.0156` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3446` n `108` status `ready` deltaP `-14.3405` edge `-0.0034` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.5719` n `102` status `ready` deltaP `14.5425` edge `0.1184` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5527` n `102` status `ready` deltaP `-16.7177` edge `-0.0073` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.7661` n `108` status `ready` deltaP `-26.5187` edge `-0.1011` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.8006` n `108` status `ready` deltaP `-4.3078` edge `-0.0225` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
