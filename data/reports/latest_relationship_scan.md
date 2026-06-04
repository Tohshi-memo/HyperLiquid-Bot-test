# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T08:37:29.258043+00:00`
- Price records: `672`
- Market context records: `2849`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.8465` n `142` status `ready` deltaP `4.5114` edge `0.2536` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.7418` n `142` status `ready` deltaP `2.5284` edge `0.6033` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.9993` n `142` status `ready` deltaP `12.7739` edge `0.3075` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.799` n `142` status `ready` deltaP `6.0331` edge `0.1317` maxDD `-3.7602`
- `market_context_high->index_24h` score `0.4464` n `142` status `ready` deltaP `6.0715` edge `0.0948` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.278` n `142` status `ready` deltaP `12.5387` edge `0.0362` maxDD `-2.3986`
- `market_context_high->equity_24h` score `0.2394` n `142` status `ready` deltaP `3.8732` edge `0.1945` maxDD `-12.6963`
- `market_context_high->unknown_1h` score `0.1006` n `142` status `ready` deltaP `4.6302` edge `0.0506` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0812` n `142` status `ready` deltaP `4.198` edge `0.011` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.6569` n `142` status `ready` deltaP `-1.8849` edge `0.0022` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6609` n `142` status `ready` deltaP `4.9465` edge `0.0583` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6615` n `142` status `ready` deltaP `-1.031` edge `-0.0026` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7043` n `142` status `ready` deltaP `0.1328` edge `-0.0066` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8624` n `142` status `ready` deltaP `4.0757` edge `0.0492` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.8692` n `142` status `ready` deltaP `-2.1506` edge `0.0252` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.0582` n `142` status `ready` deltaP `1.9624` edge `0.0367` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.2321` n `142` status `ready` deltaP `-4.5152` edge `0.0053` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.2739` n `142` status `ready` deltaP `13.7281` edge `0.2364` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.3468` n `142` status `ready` deltaP `1.8378` edge `0.0071` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4095` n `142` status `ready` deltaP `-1.8852` edge `-0.0177` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
