# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T20:22:30.393637+00:00`
- Price records: `672`
- Market context records: `6954`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.26` n `237` status `ready` deltaP `2.0345` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3794` n `237` status `ready` deltaP `2.43` edge `0.0216` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7247` n `237` status `ready` deltaP `-0.2388` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7434` n `237` status `ready` deltaP `-2.3895` edge `-0.0026` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9623` n `236` status `ready` deltaP `11.2495` edge `0.008` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2245` n `237` status `ready` deltaP `2.8791` edge `0.014` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2777` n `237` status `ready` deltaP `-2.8241` edge `-0.0155` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.5843` n `223` status `ready` deltaP `-8.9134` edge `0.3061` maxDD `-18.3163`
- `market_context_high->unknown_1h` score `-1.5901` n `237` status `ready` deltaP `-1.9809` edge `-0.0292` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6583` n `236` status `ready` deltaP `-4.4879` edge `-0.0337` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8351` n `236` status `ready` deltaP `7.2861` edge `-0.0149` maxDD `-12.1818`
- `market_context_high->equity_1h` score `-2.0357` n `237` status `ready` deltaP `1.9391` edge `-0.0185` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1325` n `236` status `ready` deltaP `3.364` edge `0.0025` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.128` n `236` status `ready` deltaP `-0.1861` edge `-0.0247` maxDD `-22.0069`
- `market_context_high->unknown_4h` score `-3.3059` n `236` status `ready` deltaP `-8.7356` edge `0.0193` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7022` n `223` status `ready` deltaP `-6.0736` edge `-0.0812` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.8091` n `236` status `ready` deltaP `-1.5915` edge `-0.0538` maxDD `-24.2483`
- `market_context_high->fx_24h` score `-4.383` n `223` status `ready` deltaP `-7.098` edge `-0.0143` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.7169` n `236` status `ready` deltaP `3.6068` edge `-0.0978` maxDD `-66.2476`
- `market_context_high->metal_24h` score `-9.3453` n `223` status `ready` deltaP `-13.8329` edge `-0.1199` maxDD `-38.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
