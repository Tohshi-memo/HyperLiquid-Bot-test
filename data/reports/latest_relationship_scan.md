# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T09:22:29.536921+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_4h` score `3259.7707` n `31` status `ready` deltaP `3.4815` edge `271.63` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3232.5445` n `31` status `ready` deltaP `1.6322` edge `269.3854` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `102.2526` n `31` status `ready` deltaP `1.6322` edge `8.5196` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `38.5498` n `31` status `ready` deltaP `45.3125` edge `2.9104` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.5644` n `31` status `ready` deltaP `46.1806` edge `2.8225` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.9205` n `31` status `ready` deltaP `45.4861` edge `2.3568` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0338` n `31` status `ready` deltaP `27.8275` edge `0.821` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.803` n `31` status `ready` deltaP `39.5112` edge `0.6849` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.2498` n `31` status `ready` deltaP `31.8605` edge `0.5859` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9918` n `31` status `ready` deltaP `19.2171` edge `0.91` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.3725` n `31` status `ready` deltaP `46.7014` edge `0.2197` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2141` n `31` status `ready` deltaP `44.3157` edge `0.1519` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7794` n `31` status `ready` deltaP `20.5862` edge `0.1964` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5817` n `31` status `ready` deltaP `38.4442` edge `0.0682` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7621` n `31` status `ready` deltaP `32.5913` edge `0.0214` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.479` n `31` status `ready` deltaP `9.8609` edge `0.2982` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2869` n `31` status `ready` deltaP `13.1543` edge `0.2412` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0836` n `31` status `ready` deltaP `26.5048` edge `0.0254` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5126` n `31` status `ready` deltaP `29.5827` edge `0.0246` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1093` n `31` status `ready` deltaP `16.7781` edge `0.0861` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
