# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T22:04:06.727454+00:00`
- Price records: `672`
- Market context records: `2804`
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

- `market_context_high->unknown_24h` score `2.7508` n `142` status `ready` deltaP `3.9906` edge `0.2491` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `1.109` n `142` status `ready` deltaP `7.2526` edge `0.1494` maxDD `-3.7602`
- `market_context_high->crypto_alt_24h` score `1.099` n `142` status `ready` deltaP `1.3131` edge `0.4745` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.6199` n `142` status `ready` deltaP `11.2114` edge `0.2863` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3278` n `142` status `ready` deltaP `13.3009` edge `0.0375` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0118` n `142` status `ready` deltaP `4.6302` edge `0.0432` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0454` n `142` status `ready` deltaP `4.6471` edge `0.0126` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5251` n `142` status `ready` deltaP `-0.3879` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5858` n `142` status `ready` deltaP `1.031` edge `0.0026` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7036` n `142` status `ready` deltaP `-1.031` edge `-0.008` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7981` n `142` status `ready` deltaP `4.7968` edge `0.0417` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8559` n `142` status `ready` deltaP `-2.3003` edge `0.0273` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9802` n `142` status `ready` deltaP `3.6266` edge `0.0371` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.1046` n `142` status `ready` deltaP `2.2673` edge `0.0308` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1459` n `142` status `ready` deltaP `-3.753` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.6326` n `142` status `ready` deltaP `-0.4488` edge `-0.0143` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6747` n `142` status `ready` deltaP `-4.3158` edge `-0.0236` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.7023` n `142` status `ready` deltaP `13.7281` edge `0.2007` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.0529` n `142` status `ready` deltaP `0.1439` edge `-0.0091` maxDD `-11.4038`
- `market_context_high->index_24h` score `-2.1001` n `142` status `ready` deltaP `-1.2202` edge `-0.0688` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
