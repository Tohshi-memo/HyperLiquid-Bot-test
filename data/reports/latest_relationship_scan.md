# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T05:52:20.521667+00:00`
- Price records: `672`
- Market context records: `2838`
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

- `market_context_high->unknown_24h` score `2.3965` n `142` status `ready` deltaP `3.2961` edge `0.2242` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.0554` n `142` status `ready` deltaP `0.6187` edge `0.4755` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8932` n `142` status `ready` deltaP `6.4904` edge `0.1365` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7021` n `142` status `ready` deltaP `11.0377` edge `0.2943` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3427` n `142` status `ready` deltaP `13.4533` edge `0.0384` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0442` n `142` status `ready` deltaP `4.3308` edge `0.0479` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1062` n `142` status `ready` deltaP `3.8986` edge `0.0098` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.2584` n `142` status `ready` deltaP `4.1618` edge `0.0488` maxDD `-2.5127`
- `market_context_high->fx_1h` score `-0.5778` n `142` status `ready` deltaP `-0.9867` edge `0.0028` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6109` n `142` status `ready` deltaP `-0.2825` edge `-0.0011` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7347` n `142` status `ready` deltaP `-0.1666` edge `-0.0085` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7443` n `142` status `ready` deltaP `4.6471` edge `0.0496` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.9722` n `142` status `ready` deltaP `-2.8991` edge `0.0216` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9771` n `142` status `ready` deltaP `3.6266` edge `0.0375` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0258` n `142` status `ready` deltaP `1.9624` edge `0.0394` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1433` n `142` status `ready` deltaP `-3.6005` edge `0.0066` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3522` n `142` status `ready` deltaP `1.8378` edge `0.0064` maxDD `-10.0279`
- `market_context_high->crypto_alt_4h` score `-1.4333` n `142` status `ready` deltaP `13.8805` edge `0.2221` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5149` n `142` status `ready` deltaP `-2.7533` edge `-0.0207` maxDD `-0.6418`
- `market_context_high->equity_24h` score `-1.6318` n `142` status `ready` deltaP `1.9635` edge `0.0513` maxDD `-12.6963`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
