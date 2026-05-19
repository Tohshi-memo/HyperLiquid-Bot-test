# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T14:52:21.848780+00:00`
- Price records: `672`
- Market context records: `1230`
- Flow alert records: `5446`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8788`

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

- `market_context_high->crypto_major_24h` score `18.9094` n `128` status `ready` deltaP `44.5312` edge `1.3921` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8599` n `128` status `ready` deltaP `3.6966` edge `0.752` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.5997` n `128` status `ready` deltaP `22.6562` edge `0.6839` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.0641` n `128` status `ready` deltaP `-1.0417` edge `0.679` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.7317` n `128` status `ready` deltaP `-5.2083` edge `0.5772` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.4202` n `128` status `ready` deltaP `17.0922` edge `0.2374` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.23` n `128` status `ready` deltaP `21.1806` edge `0.2366` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9108` n `128` status `ready` deltaP `21.3542` edge `0.4635` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.4473` n `128` status `ready` deltaP `12.9763` edge `0.1024` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `0.8879` n `128` status `ready` deltaP `0.1736` edge `0.3458` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.7679` n `128` status `ready` deltaP `10.4978` edge `0.0257` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7346` n `128` status `ready` deltaP `5.9084` edge `0.0587` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.6186` n `128` status `ready` deltaP `7.7257` edge `0.0465` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1394` n `128` status `ready` deltaP `10.2685` edge `0.0042` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.021` n `128` status `ready` deltaP `6.3483` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1595` n `128` status `ready` deltaP `5.545` edge `0.1347` maxDD `-8.3693`
- `market_context_high->metal_4h` score `-0.3508` n `128` status `ready` deltaP `13.9292` edge `0.021` maxDD `-6.4478`
- `market_context_high->crypto_alt_1h` score `-0.3578` n `128` status `ready` deltaP `0.1965` edge `0.0371` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4035` n `128` status `ready` deltaP `2.5262` edge `0.008` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.8722` n `128` status `ready` deltaP `-2.9098` edge `0.0082` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
