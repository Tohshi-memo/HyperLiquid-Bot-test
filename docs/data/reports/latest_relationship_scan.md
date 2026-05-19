# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T23:07:16.748928+00:00`
- Price records: `672`
- Market context records: `1264`
- Flow alert records: `5548`
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

- `market_context_high->crypto_major_24h` score `17.9641` n `128` status `ready` deltaP `41.5798` edge `1.333` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.5212` n `128` status `ready` deltaP `4.6875` edge `0.9289` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.2388` n `128` status `ready` deltaP `24.0451` edge `0.7279` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `8.2142` n `128` status `ready` deltaP `5.8308` edge `0.7673` maxDD `-6.7322`
- `market_context_high->index_24h` score `4.7095` n `128` status `ready` deltaP `25.6944` edge `0.3298` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.6892` n `128` status `ready` deltaP `19.0739` edge `0.2466` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.5933` n `128` status `ready` deltaP `23.7847` edge `0.5348` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.4134` n `128` status `ready` deltaP `-10.9375` edge `0.4222` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.2806` n `128` status `ready` deltaP `1.5625` edge `0.4526` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.8052` n `128` status `ready` deltaP `15.1105` edge `0.118` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.7726` n `128` status `ready` deltaP `17.8926` edge `0.0882` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.6619` n `135` status `ready` deltaP `9.592` edge `0.0229` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.641` n `135` status `ready` deltaP `6.1643` edge `0.0492` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.4144` n `135` status `ready` deltaP `12.026` edge `0.0154` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.2875` n `128` status `ready` deltaP `8.4414` edge `0.1727` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.1072` n `128` status `ready` deltaP `3.7327` edge `0.0305` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.3101` n `128` status `ready` deltaP `9.4702` edge `0.1936` maxDD `-16.7194`
- `market_context_high->fx_1h` score `-0.318` n `135` status `ready` deltaP `3.1604` edge `-0.002` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.425` n `135` status `ready` deltaP `0.3393` edge `0.0303` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.6724` n `135` status `ready` deltaP `0.3704` edge `0.0023` maxDD `-4.9451`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
