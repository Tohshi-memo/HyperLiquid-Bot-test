# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T12:37:38.327034+00:00`
- Price records: `672`
- Market context records: `1220`
- Flow alert records: `5418`
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

- `market_context_high->crypto_major_24h` score `18.9425` n `128` status `ready` deltaP `44.7048` edge `1.3937` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.7429` n `128` status `ready` deltaP `3.2393` edge `0.7453` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.3074` n `128` status `ready` deltaP `22.4826` edge `0.6607` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.5695` n `128` status `ready` deltaP `-3.6458` edge `0.6366` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.9263` n `128` status `ready` deltaP `-2.6042` edge `0.5946` maxDD `-6.3373`
- `market_context_high->equity_4h` score `3.1585` n `128` status `ready` deltaP `16.0251` edge `0.2227` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.577` n `128` status `ready` deltaP `19.6181` edge `0.1926` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3147` n `128` status `ready` deltaP `19.7917` edge `0.3975` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.1733` n `128` status `ready` deltaP `11.7568` edge `0.0877` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.89` n `128` status `ready` deltaP `9.2882` edge `0.0587` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.642` n `128` status `ready` deltaP `9.7493` edge `0.0202` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5655` n `128` status `ready` deltaP `5.0102` edge `0.0506` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.1195` n `128` status `ready` deltaP `-0.5208` edge `0.2864` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.0453` n `128` status `ready` deltaP `9.6697` edge `-0.0072` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1025` n `128` status `ready` deltaP `5.4501` edge `0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1611` n `128` status `ready` deltaP `5.545` edge `0.1345` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.2955` n `128` status `ready` deltaP `1.0947` edge `0.0391` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3778` n `128` status `ready` deltaP `2.9753` edge `0.0083` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7715` n `128` status `ready` deltaP `-2.311` edge `0.0126` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.8518` n `128` status `ready` deltaP `12.5572` edge `-0.0116` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
