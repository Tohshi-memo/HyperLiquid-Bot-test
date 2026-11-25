# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T16:07:36.441357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32187.2701` n `45` status `ready` deltaP `2.1656` edge `2682.2675` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21890.1153` n `45` status `ready` deltaP `2.8727` edge `1824.171` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `952.3151` n `31` status `ready` deltaP `2.3807` edge `79.3613` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `637.1678` n `31` status `ready` deltaP `4.0913` edge `53.0757` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `425.1227` n `31` status `ready` deltaP `5.7292` edge `35.3887` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.7158` n `31` status `ready` deltaP `51.5625` edge `3.4659` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.1784` n `31` status `ready` deltaP `53.125` edge `3.1607` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.66` n `31` status `ready` deltaP `55.5556` edge `2.8513` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9834` n `31` status `ready` deltaP `41.2355` edge `0.7512` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.9765` n `31` status `ready` deltaP `27.3701` edge `0.9026` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.4504` n `31` status `ready` deltaP `38.1393` edge `0.748` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5048` n `31` status `ready` deltaP `18.9123` edge `0.9778` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.309` n `31` status `ready` deltaP `52.2569` edge `0.2607` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3957` n `31` status `ready` deltaP `46.2254` edge `0.1543` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0062` n `31` status `ready` deltaP `20.5862` edge `0.2153` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4778` n `31` status `ready` deltaP `36.9198` edge `0.0697` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7094` n `31` status `ready` deltaP `31.8428` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6504` n `31` status `ready` deltaP `11.2082` edge `0.3112` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4554` n `45` status `ready` deltaP `30.0881` edge `0.0325` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4273` n `31` status `ready` deltaP `13.1543` edge `0.2592` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
