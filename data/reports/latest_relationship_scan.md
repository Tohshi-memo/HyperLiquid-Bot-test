# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T23:07:26.858870+00:00`
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

- `news_risk_high->unknown_1h` score `3301.7149` n `31` status `ready` deltaP `1.6322` edge `275.1496` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3165.5501` n `31` status `ready` deltaP `3.3291` edge `263.7793` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.369` n `31` status `ready` deltaP `27.9029` edge `1.2614` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.376` n `31` status `ready` deltaP `26.6898` edge `0.8534` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.0077` n `31` status `ready` deltaP `23.9168` edge `0.8412` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1541` n `31` status `ready` deltaP `20.5104` edge `0.6298` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4767` n `31` status `ready` deltaP `29.6027` edge `0.3071` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1314` n `31` status `ready` deltaP `14.3391` edge `0.704` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6814` n `31` status `ready` deltaP `38.6762` edge `0.1451` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5528` n `31` status `ready` deltaP `12.1877` edge `0.2423` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.354` n `31` status `ready` deltaP `28.993` edge `0.0289` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.303` n `31` status `ready` deltaP `15.6461` edge `0.1063` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.302` n `31` status `ready` deltaP `28.25` edge `0.012` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1956` n `31` status `ready` deltaP `24.6101` edge `0.0189` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.9349` n `31` status `ready` deltaP `6.2681` edge `0.2524` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7234` n `31` status `ready` deltaP `8.813` edge `0.1979` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1325` n `31` status `ready` deltaP `24.6426` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3873` n `31` status `ready` deltaP `9.5889` edge `0.0255` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3508` n `31` status `ready` deltaP `11.5952` edge `0.0234` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3759` n `31` status `ready` deltaP `-2.5111` edge `0.0116` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
