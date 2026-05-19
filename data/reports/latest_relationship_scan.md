# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T14:07:22.615100+00:00`
- Price records: `672`
- Market context records: `1226`
- Flow alert records: `5436`
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

- `market_context_high->crypto_major_24h` score `18.9624` n `128` status `ready` deltaP `44.8784` edge `1.3942` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8419` n `128` status `ready` deltaP `3.6966` edge `0.7505` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.5061` n `128` status `ready` deltaP `22.6562` edge `0.6761` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.666` n `128` status `ready` deltaP `-1.5625` edge `0.6493` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.9822` n `128` status `ready` deltaP `-4.6875` edge `0.5946` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3045` n `128` status `ready` deltaP `16.6349` edge `0.2308` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.006` n `128` status `ready` deltaP `20.6597` edge `0.2214` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7339` n `128` status `ready` deltaP `20.8333` edge `0.4443` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.3339` n `128` status `ready` deltaP `12.519` edge `0.096` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.7107` n `128` status `ready` deltaP `8.2466` edge `0.0507` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.6828` n `128` status `ready` deltaP `10.0487` edge `0.0216` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6266` n `128` status `ready` deltaP `5.4593` edge `0.0527` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.5882` n `128` status `ready` deltaP `-0.3472` edge `0.3243` maxDD `-10.1706`
- `market_context_high->metal_1h` score `0.0495` n `128` status `ready` deltaP `9.9691` edge `-0.0013` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0473` n `128` status `ready` deltaP `6.0489` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1735` n `128` status `ready` deltaP `5.545` edge `0.1329` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3765` n `128` status `ready` deltaP `0.1965` edge `0.0347` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4144` n `128` status `ready` deltaP `2.5262` edge `0.0066` maxDD `-4.1256`
- `market_context_high->metal_4h` score `-0.559` n `128` status `ready` deltaP `13.4718` edge `0.0067` maxDD `-6.4478`
- `market_context_high->commodity_1h` score `-0.8254` n `128` status `ready` deltaP `-2.7601` edge `0.0111` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
