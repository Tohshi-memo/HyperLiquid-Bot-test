# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T23:22:36.568910+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3301.7832` n `31` status `ready` deltaP `1.7819` edge `275.1543` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3165.5873` n `31` status `ready` deltaP `3.3291` edge `263.7824` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.3894` n `31` status `ready` deltaP `27.9029` edge `1.2631` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.3417` n `31` status `ready` deltaP `26.5165` edge `0.8517` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.9417` n `31` status `ready` deltaP `23.9168` edge `0.8357` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1229` n `31` status `ready` deltaP `20.5104` edge `0.6272` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4695` n `31` status `ready` deltaP `29.6027` edge `0.3065` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1166` n `31` status `ready` deltaP `14.3391` edge `0.7021` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6838` n `31` status `ready` deltaP `38.6762` edge `0.1453` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5324` n `31` status `ready` deltaP `12.1877` edge `0.2406` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3528` n `31` status `ready` deltaP `28.993` edge `0.0288` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3008` n `31` status `ready` deltaP `28.25` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.285` n `31` status `ready` deltaP `15.4964` edge `0.1058` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.1908` n `31` status `ready` deltaP `24.6101` edge `0.0185` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.9225` n `31` status `ready` deltaP `6.1184` edge `0.2518` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.707` n `31` status `ready` deltaP `8.6633` edge `0.1968` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1325` n `31` status `ready` deltaP `24.6426` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3794` n `31` status `ready` deltaP `9.4365` edge `0.0255` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3397` n `31` status `ready` deltaP `11.4427` edge `0.023` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3759` n `31` status `ready` deltaP `-2.5111` edge `0.0116` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
