# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T16:22:12.866510+00:00`
- Price records: `672`
- Market context records: `5057`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `12.0856` n `100` status `ready` deltaP `3.9042` edge `1.0312` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.8821` n `100` status `ready` deltaP `21.4939` edge `0.6991` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.4901` n `100` status `ready` deltaP `16.6585` edge `0.4848` maxDD `-7.7348`
- `market_context_high->crypto_major_4h` score `5.1562` n `100` status `ready` deltaP `15.9634` edge `0.4817` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `0.8986` n `100` status `ready` deltaP `7.6407` edge `0.1127` maxDD `-4.4335`
- `market_context_high->metal_4h` score `0.7888` n `100` status `ready` deltaP `8.9451` edge `0.114` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.5079` n `100` status `ready` deltaP `7.8982` edge `0.0698` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.4734` n `100` status `ready` deltaP `4.6768` edge `0.1635` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.395` n `100` status `ready` deltaP `6.9401` edge `0.0363` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2185` n `100` status `ready` deltaP `5.6467` edge `0.0909` maxDD `-5.3758`
- `market_context_high->fx_24h` score `-0.0725` n `76` status `ready` deltaP `8.7902` edge `0.0083` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1147` n `100` status `ready` deltaP `4.2683` edge `0.0381` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3453` n `100` status `ready` deltaP `1.0958` edge `0.0144` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4618` n `100` status `ready` deltaP `0.4491` edge `0.0119` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.758` n `100` status `ready` deltaP `7.9939` edge `0.0088` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0304` n `100` status `ready` deltaP `-4.5244` edge `-0.003` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4935` n `100` status `ready` deltaP `-8.7545` edge `-0.0051` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.5169` n `76` status `ready` deltaP `6.5698` edge `0.0508` maxDD `-32.9721`
- `market_context_high->unknown_24h` score `-3.8738` n `76` status `ready` deltaP `27.3209` edge `-0.4707` maxDD `-1.4072`
- `market_context_high->commodity_24h` score `-4.5702` n `76` status `ready` deltaP `0.1371` edge `-0.0902` maxDD `-26.7306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
