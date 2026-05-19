# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T13:52:16.787650+00:00`
- Price records: `672`
- Market context records: `1225`
- Flow alert records: `5433`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8777`

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

- `market_context_high->crypto_major_24h` score `18.9847` n `128` status `ready` deltaP `45.052` edge `1.3949` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8335` n `128` status `ready` deltaP `3.6966` edge `0.7498` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.4761` n `128` status `ready` deltaP `22.6562` edge `0.6736` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.5429` n `128` status `ready` deltaP `-1.7361` edge `0.6402` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `5.0741` n `128` status `ready` deltaP `-4.5139` edge `0.6011` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.2731` n `128` status `ready` deltaP `16.4824` edge `0.2292` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.9321` n `128` status `ready` deltaP `20.4861` edge `0.2164` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6703` n `128` status `ready` deltaP `20.6597` edge `0.4373` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.3001` n `128` status `ready` deltaP `12.3666` edge `0.0942` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.7426` n `128` status `ready` deltaP `8.4202` edge `0.0522` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.66` n `128` status `ready` deltaP `9.899` edge `0.0207` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6015` n `128` status `ready` deltaP `5.3096` edge `0.0516` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.4771` n `128` status `ready` deltaP `-0.5208` edge `0.3162` maxDD `-10.1706`
- `market_context_high->metal_1h` score `0.0231` n `128` status `ready` deltaP `9.8194` edge `-0.0025` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0593` n `128` status `ready` deltaP `5.8992` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.172` n `128` status `ready` deltaP `5.545` edge `0.1331` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3632` n `128` status `ready` deltaP `0.3462` edge `0.0354` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4012` n `128` status `ready` deltaP `2.6759` edge `0.0073` maxDD `-4.1256`
- `market_context_high->metal_4h` score `-0.618` n `128` status `ready` deltaP `13.3194` edge `0.0028` maxDD `-6.4478`
- `market_context_high->commodity_1h` score `-0.8038` n `128` status `ready` deltaP `-2.6104` edge `0.0119` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
