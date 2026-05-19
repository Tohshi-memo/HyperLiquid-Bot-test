# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T14:37:16.574362+00:00`
- Price records: `672`
- Market context records: `1229`
- Flow alert records: `5443`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8788`

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

- `market_context_high->crypto_major_24h` score `18.9142` n `128` status `ready` deltaP `44.5312` edge `1.3925` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8539` n `128` status `ready` deltaP `3.6966` edge `0.7515` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.5601` n `128` status `ready` deltaP `22.6562` edge `0.6806` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.9326` n `128` status `ready` deltaP `-1.2153` edge `0.6692` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.814` n `128` status `ready` deltaP `-5.0347` edge `0.5829` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3876` n `128` status `ready` deltaP `16.9397` edge `0.2357` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.1573` n `128` status `ready` deltaP `21.0069` edge `0.2317` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8573` n `128` status `ready` deltaP `21.1806` edge `0.4578` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.4123` n `128` status `ready` deltaP `12.8239` edge `0.1005` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `0.796` n `128` status `ready` deltaP `0.0` edge `0.3393` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.744` n `128` status `ready` deltaP `10.3481` edge `0.0247` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7046` n `128` status `ready` deltaP `5.7587` edge `0.0572` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.6505` n `128` status `ready` deltaP `7.8994` edge `0.048` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1046` n `128` status `ready` deltaP `10.1188` edge `0.0023` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0222` n `128` status `ready` deltaP `6.3483` edge `0.0014` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1673` n `128` status `ready` deltaP `5.545` edge `0.1337` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.371` n `128` status `ready` deltaP `0.1965` edge `0.0354` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4113` n `128` status `ready` deltaP `2.5262` edge `0.007` maxDD `-4.1256`
- `market_context_high->metal_4h` score `-0.4194` n `128` status `ready` deltaP `13.7767` edge `0.0163` maxDD `-6.4478`
- `market_context_high->commodity_1h` score `-0.859` n `128` status `ready` deltaP `-2.9098` edge `0.0093` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
