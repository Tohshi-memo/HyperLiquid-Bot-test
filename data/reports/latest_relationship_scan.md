# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T19:37:18.325984+00:00`
- Price records: `672`
- Market context records: `1250`
- Flow alert records: `5505`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `18.1582` n `128` status `ready` deltaP `42.1006` edge `1.3457` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.044` n `128` status `ready` deltaP `2.2569` edge `0.822` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `7.9903` n `128` status `ready` deltaP `5.221` edge `0.7527` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6535` n `128` status `ready` deltaP `22.309` edge `0.6907` maxDD `-15.1306`
- `market_context_high->index_24h` score `3.9883` n `128` status `ready` deltaP `23.2639` edge `0.2859` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.4922` n `128` status `ready` deltaP `-8.5069` edge `0.4959` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3236` n `128` status `ready` deltaP `17.5495` edge `0.2263` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2395` n `128` status `ready` deltaP `22.3958` edge `0.4987` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.0358` n `128` status `ready` deltaP `1.5625` edge `0.4322` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5483` n `128` status `ready` deltaP `14.0434` edge `0.1037` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7188` n `128` status `ready` deltaP `10.1984` edge `0.0236` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6745` n `128` status `ready` deltaP `6.2078` edge `0.0517` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.336` n `128` status `ready` deltaP `11.4661` edge `0.0126` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.3007` n `128` status `ready` deltaP `5.6424` edge `0.0339` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2803` n `128` status `ready` deltaP `15.7584` edge `0.0614` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.0063` n `128` status `ready` deltaP `6.917` edge `0.1452` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0785` n `128` status `ready` deltaP `5.8992` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2549` n `128` status `ready` deltaP `1.2444` edge `0.0433` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3949` n `128` status `ready` deltaP `2.5262` edge `0.0091` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6622` n `128` status `ready` deltaP `8.0983` edge `0.1576` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
