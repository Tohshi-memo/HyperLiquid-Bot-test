# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T13:22:18.578988+00:00`
- Price records: `672`
- Market context records: `1223`
- Flow alert records: `5427`
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

- `market_context_high->crypto_major_24h` score `18.9931` n `128` status `ready` deltaP `45.052` edge `1.3956` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8191` n `128` status `ready` deltaP `3.6966` edge `0.7486` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.4161` n `128` status `ready` deltaP `22.6562` edge `0.6686` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.2794` n `128` status `ready` deltaP `-4.1667` edge `0.6159` maxDD `-6.8535`
- `market_context_high->metal_24h` score `5.2703` n `128` status `ready` deltaP `-2.0833` edge `0.6198` maxDD `-6.3373`
- `market_context_high->equity_4h` score `3.2659` n `128` status `ready` deltaP `16.4824` edge `0.2286` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.7987` n `128` status `ready` deltaP `20.1389` edge `0.2076` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5563` n `128` status `ready` deltaP `20.3125` edge `0.425` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.2627` n `128` status `ready` deltaP `12.2141` edge `0.0921` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.8027` n `128` status `ready` deltaP `8.7674` edge `0.0549` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.6552` n `128` status `ready` deltaP `9.899` edge `0.0203` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6039` n `128` status `ready` deltaP `5.3096` edge `0.0518` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.3427` n `128` status `ready` deltaP `-0.5208` edge `0.305` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.0129` n `128` status `ready` deltaP `9.8194` edge `-0.0055` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0737` n `128` status `ready` deltaP `5.7495` edge `0.0011` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1626` n `128` status `ready` deltaP `5.545` edge `0.1343` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3321` n `128` status `ready` deltaP `0.6456` edge `0.0374` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3895` n `128` status `ready` deltaP `2.8256` edge `0.0078` maxDD `-4.1256`
- `market_context_high->metal_4h` score `-0.7336` n `128` status `ready` deltaP `13.0145` edge `-0.0048` maxDD `-6.4478`
- `market_context_high->commodity_1h` score `-0.7691` n `128` status `ready` deltaP `-2.311` edge `0.0128` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
