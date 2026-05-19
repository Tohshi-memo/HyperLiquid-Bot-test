# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T14:14:44.433680+00:00`
- Price records: `672`
- Market context records: `1227`
- Flow alert records: `5437`
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

- `market_context_high->crypto_major_24h` score `18.9648` n `128` status `ready` deltaP `44.8784` edge `1.3944` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8431` n `128` status `ready` deltaP `3.6966` edge `0.7506` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.5109` n `128` status `ready` deltaP `22.6562` edge `0.6765` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.6708` n `128` status `ready` deltaP `-1.5625` edge `0.6497` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.9786` n `128` status `ready` deltaP `-4.6875` edge `0.5943` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3105` n `128` status `ready` deltaP `16.6349` edge `0.2313` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.0084` n `128` status `ready` deltaP `20.6597` edge `0.2216` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7378` n `128` status `ready` deltaP `20.8333` edge `0.4448` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.3375` n `128` status `ready` deltaP `12.519` edge `0.0963` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.7119` n `128` status `ready` deltaP `8.2466` edge `0.0508` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.6852` n `128` status `ready` deltaP `10.0487` edge `0.0218` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6326` n `128` status `ready` deltaP `5.4593` edge `0.0532` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.5894` n `128` status `ready` deltaP `-0.3472` edge `0.3244` maxDD `-10.1706`
- `market_context_high->metal_1h` score `0.0531` n `128` status `ready` deltaP `9.9691` edge `-0.001` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0461` n `128` status `ready` deltaP `6.0489` edge `0.0014` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.172` n `128` status `ready` deltaP `5.545` edge `0.1331` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3741` n `128` status `ready` deltaP `0.1965` edge `0.035` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4128` n `128` status `ready` deltaP `2.5262` edge `0.0068` maxDD `-4.1256`
- `market_context_high->metal_4h` score `-0.5554` n `128` status `ready` deltaP `13.4718` edge `0.007` maxDD `-6.4478`
- `market_context_high->commodity_1h` score `-0.8278` n `128` status `ready` deltaP `-2.7601` edge `0.0109` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
