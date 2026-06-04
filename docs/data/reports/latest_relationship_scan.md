# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T03:52:25.396486+00:00`
- Price records: `672`
- Market context records: `2829`
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

- `market_context_high->unknown_24h` score `2.3351` n `142` status `ready` deltaP `2.9489` edge `0.2214` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9774` n `142` status `ready` deltaP `6.6429` edge `0.1425` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.8238` n `142` status `ready` deltaP `12.0794` edge `0.2975` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.3071` n `142` status `ready` deltaP `-0.7702` edge `0.4224` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.2807` n `142` status `ready` deltaP `12.996` edge `0.0335` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1126` n `142` status `ready` deltaP `4.3308` edge `0.0536` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1389` n `142` status `ready` deltaP `3.5992` edge `0.0076` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5408` n `142` status `ready` deltaP `0.6157` edge `0.0019` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.591` n `142` status `ready` deltaP `-1.1364` edge `0.0027` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.776` n `142` status `ready` deltaP `-0.466` edge `-0.0118` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.8051` n `142` status `ready` deltaP `4.6471` edge `0.0418` maxDD `-10.747`
- `market_context_high->index_24h` score `-0.8279` n `142` status `ready` deltaP `2.7729` edge `0.0106` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `-1.0309` n `142` status `ready` deltaP `3.3272` edge `0.0326` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0945` n `142` status `ready` deltaP `-3.4979` edge `0.0154` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.1422` n `142` status `ready` deltaP `1.9624` edge `0.0297` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1957` n `142` status `ready` deltaP `-4.2103` edge `0.0063` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2902` n `142` status `ready` deltaP `2.2951` edge `0.0113` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6259` n `142` status `ready` deltaP `-3.795` edge `-0.023` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7991` n `142` status `ready` deltaP `13.1183` edge `0.1967` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.4421` n `142` status `ready` deltaP `-1.6854` edge `-0.0468` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
