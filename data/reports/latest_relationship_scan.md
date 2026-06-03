# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T16:22:27.333940+00:00`
- Price records: `672`
- Market context records: `2780`
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

- `market_context_high->unknown_24h` score `3.6512` n `140` status `ready` deltaP `7.4752` edge `0.3009` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `3.3226` n `140` status `ready` deltaP `4.5387` edge `0.6383` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8842` n `142` status `ready` deltaP `6.0331` edge `0.1388` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.334` n `140` status `ready` deltaP `10.6051` edge `0.2815` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.1996` n `142` status `ready` deltaP `12.0813` edge `0.0292` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0817` n `142` status `ready` deltaP `3.732` edge `0.0414` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1202` n `142` status `ready` deltaP `3.7489` edge `0.009` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5874` n `142` status `ready` deltaP `-1.1364` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6419` n `142` status `ready` deltaP `0.4322` edge `-0.0006` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6475` n `142` status `ready` deltaP `-0.4322` edge `-0.0048` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6968` n `142` status `ready` deltaP `5.0962` edge `0.0527` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9147` n `142` status `ready` deltaP `3.926` edge `0.0435` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0705` n `142` status `ready` deltaP `-3.4979` edge `0.0174` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1215` n `142` status `ready` deltaP `-3.4481` edge `0.0074` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3784` n `140` status `ready` deltaP `-1.002` edge `-0.021` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4213` n `142` status `ready` deltaP `13.8805` edge `0.2231` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.5658` n `142` status `ready` deltaP `0.161` edge `-0.0098` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.6069` n `142` status `ready` deltaP `0.7429` edge `-0.0009` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.2452` n `142` status `ready` deltaP `-1.3805` edge `-0.0236` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.5444` n `142` status `ready` deltaP `5.2774` edge `0.1292` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
