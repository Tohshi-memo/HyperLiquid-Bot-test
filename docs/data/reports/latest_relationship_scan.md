# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T11:07:24.263296+00:00`
- Price records: `672`
- Market context records: `1213`
- Flow alert records: `5399`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.8401` n `128` status `ready` deltaP `44.0104` edge `1.3898` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.6259` n `128` status `ready` deltaP `2.782` edge `0.7386` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.0234` n `128` status `ready` deltaP `21.9618` edge `0.6405` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `6.0896` n `128` status `ready` deltaP `-2.6042` edge `0.673` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.3588` n `128` status `ready` deltaP `-3.4722` edge `0.5531` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.9053` n `128` status `ready` deltaP `15.1105` edge `0.2077` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1529` n `128` status `ready` deltaP `18.5764` edge `0.1642` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.8721` n `128` status `ready` deltaP `18.75` edge `0.3477` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0621` n `128` status `ready` deltaP `10.3299` edge `0.0661` maxDD `-0.3831`
- `market_context_high->index_4h` score `1.0198` n `128` status `ready` deltaP `10.8422` edge `0.081` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6073` n `128` status `ready` deltaP `9.4499` edge `0.0193` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4972` n `128` status `ready` deltaP `4.5611` edge `0.0479` maxDD `-1.2834`
- `market_context_high->metal_1h` score `-0.0393` n `128` status `ready` deltaP `9.8194` edge `-0.0077` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.13` n `128` status `ready` deltaP `5.1507` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.2049` n `128` status `ready` deltaP `5.3926` edge `0.1299` maxDD `-8.3693`
- `market_context_high->unknown_24h` score `-0.2693` n `128` status `ready` deltaP `-0.5208` edge `0.254` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.396` n `128` status `ready` deltaP `0.1965` edge `0.0322` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4354` n `128` status `ready` deltaP `2.3765` edge `0.0049` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7679` n `128` status `ready` deltaP `-2.311` edge `0.0129` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.0258` n `128` status `ready` deltaP `11.6426` edge `-0.02` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
