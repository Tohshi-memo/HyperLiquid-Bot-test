# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T17:22:34.257189+00:00`
- Price records: `672`
- Market context records: `5165`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `29.6243` n `64` status `ready` deltaP `33.1597` edge `2.2666` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `5.9044` n `140` status `ready` deltaP `20.0174` edge `0.4608` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.612` n `140` status `ready` deltaP `14.6777` edge `0.4464` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.6061` n `64` status `ready` deltaP `19.4444` edge `0.7996` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.4353` n `64` status `ready` deltaP `17.5347` edge `0.8179` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `3.8809` n `140` status `ready` deltaP `13.554` edge `0.4623` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.8205` n `149` status `ready` deltaP `9.9486` edge `0.3162` maxDD `-2.7986`
- `market_context_high->commodity_24h` score `1.1277` n `64` status `ready` deltaP `19.2708` edge `0.1499` maxDD `-5.704`
- `market_context_high->crypto_major_1h` score `0.8224` n `149` status `ready` deltaP `8.0376` edge `0.1395` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7794` n `149` status `ready` deltaP `5.2656` edge `0.126` maxDD `-5.0257`
- `market_context_high->metal_24h` score `0.7208` n `64` status `ready` deltaP `0.3472` edge `0.2333` maxDD `-6.123`
- `market_context_high->equity_4h` score `0.5609` n `140` status `ready` deltaP `8.2665` edge `0.1555` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3079` n `149` status `ready` deltaP `7.7231` edge `0.0707` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0358` n `149` status `ready` deltaP `5.0386` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0952` n `149` status `ready` deltaP `4.8266` edge `0.0148` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.196` n `149` status `ready` deltaP `2.9428` edge `0.0005` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.417` n `140` status `ready` deltaP `4.4207` edge `0.0288` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4696` n `140` status `ready` deltaP `5.3223` edge `0.0077` maxDD `-1.6047`
- `market_context_high->fx_24h` score `-0.5151` n `64` status `ready` deltaP `6.0764` edge `0.0061` maxDD `-0.8294`
- `market_context_high->commodity_1h` score `-0.5511` n `149` status `ready` deltaP `1.3061` edge `0.0015` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
