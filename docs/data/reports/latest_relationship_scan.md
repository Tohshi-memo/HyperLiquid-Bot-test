# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T13:37:18.260493+00:00`
- Price records: `672`
- Market context records: `1224`
- Flow alert records: `5430`
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

- `market_context_high->crypto_major_24h` score `18.9835` n `128` status `ready` deltaP `45.052` edge `1.3948` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8263` n `128` status `ready` deltaP `3.6966` edge `0.7492` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.4389` n `128` status `ready` deltaP `22.6562` edge `0.6705` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.409` n `128` status `ready` deltaP `-1.9097` edge `0.6302` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `5.178` n `128` status `ready` deltaP `-4.3403` edge `0.6086` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.2647` n `128` status `ready` deltaP `16.4824` edge `0.2285` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.8618` n `128` status `ready` deltaP `20.3125` edge `0.2117` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6129` n `128` status `ready` deltaP `20.4861` edge `0.4311` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.2723` n `128` status `ready` deltaP `12.2141` edge `0.0929` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.7732` n `128` status `ready` deltaP `8.5938` edge `0.0536` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.642` n `128` status `ready` deltaP `9.7493` edge `0.0202` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5991` n `128` status `ready` deltaP `5.3096` edge `0.0514` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.4003` n `128` status `ready` deltaP `-0.5208` edge `0.3098` maxDD `-10.1706`
- `market_context_high->metal_1h` score `0.0087` n `128` status `ready` deltaP `9.8194` edge `-0.0037` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0593` n `128` status `ready` deltaP `5.8992` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1681` n `128` status `ready` deltaP `5.545` edge `0.1336` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3453` n `128` status `ready` deltaP `0.4959` edge `0.0367` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3903` n `128` status `ready` deltaP `2.8256` edge `0.0077` maxDD `-4.1256`
- `market_context_high->metal_4h` score `-0.6722` n `128` status `ready` deltaP `13.167` edge `-0.0007` maxDD `-6.4478`
- `market_context_high->commodity_1h` score `-0.7871` n `128` status `ready` deltaP `-2.4607` edge `0.0123` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
