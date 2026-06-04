# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T04:07:24.415745+00:00`
- Price records: `672`
- Market context records: `2830`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.3255` n `142` status `ready` deltaP `2.9489` edge `0.2206` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9306` n `142` status `ready` deltaP `6.6429` edge `0.1386` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.8051` n `142` status `ready` deltaP `11.9058` edge `0.2971` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.3378` n `142` status `ready` deltaP `-0.5966` edge `0.4238` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.2854` n `142` status `ready` deltaP `12.996` edge `0.0341` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.049` n `142` status `ready` deltaP `4.3308` edge `0.0483` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1482` n `142` status `ready` deltaP `3.4495` edge `0.0074` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5501` n `142` status `ready` deltaP `0.466` edge `0.0017` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->index_24h` score `-0.7576` n `142` status `ready` deltaP `2.9465` edge `0.0153` maxDD `-2.5127`
- `market_context_high->metal_1h` score `-0.7775` n `142` status `ready` deltaP `-0.466` edge `-0.012` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.8215` n `142` status `ready` deltaP `4.4974` edge `0.0407` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-1.0387` n `142` status `ready` deltaP `3.3272` edge `0.0316` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0969` n `142` status `ready` deltaP `-3.4979` edge `0.0152` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.1254` n `142` status `ready` deltaP `1.9624` edge `0.0311` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1823` n `142` status `ready` deltaP `-4.0579` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2926` n `142` status `ready` deltaP `2.2951` edge `0.011` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6084` n `142` status `ready` deltaP `-3.6213` edge `-0.0227` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7437` n `142` status `ready` deltaP `13.2708` edge `0.2003` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.4366` n `142` status `ready` deltaP `-1.6854` edge `-0.0461` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
