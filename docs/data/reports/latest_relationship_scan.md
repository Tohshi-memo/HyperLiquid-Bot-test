# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T21:37:17.328464+00:00`
- Price records: `672`
- Market context records: `1258`
- Flow alert records: `5529`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9521` n `128` status `ready` deltaP `41.5798` edge `1.332` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.8451` n `128` status `ready` deltaP `3.6458` edge `0.8795` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.0167` n `128` status `ready` deltaP `5.221` edge `0.7549` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8471` n `128` status `ready` deltaP `23.0034` edge `0.7022` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.3778` n `128` status `ready` deltaP `24.6528` edge `0.3091` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.454` n `128` status `ready` deltaP `18.1592` edge `0.2331` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.3902` n `128` status `ready` deltaP `22.7431` edge `0.5157` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.8843` n `128` status `ready` deltaP `-9.8958` edge `0.4545` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.2134` n `128` status `ready` deltaP `1.5625` edge `0.447` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.6072` n `128` status `ready` deltaP `14.1958` edge `0.1076` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.8476` n `129` status `ready` deltaP `11.4643` edge `0.0259` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7833` n `129` status `ready` deltaP `7.1925` edge `0.0542` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.5291` n `128` status `ready` deltaP `16.9779` edge `0.074` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.4132` n `129` status `ready` deltaP `12.1757` edge `0.0143` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.1898` n `128` status `ready` deltaP `4.6007` edge `0.0316` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `0.112` n `128` status `ready` deltaP `7.5267` edge `0.1563` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1556` n `129` status `ready` deltaP `5.1455` edge `-0.0017` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2585` n `129` status `ready` deltaP `1.2963` edge `0.0425` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4303` n `129` status `ready` deltaP `1.9647` edge `0.0083` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.5238` n `128` status `ready` deltaP `8.5556` edge `0.1723` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
