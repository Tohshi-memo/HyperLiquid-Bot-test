# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T23:37:30.802416+00:00`
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

- `news_risk_high->unknown_1h` score `3301.7436` n `31` status `ready` deltaP `1.7819` edge `275.151` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3165.6053` n `31` status `ready` deltaP `3.3291` edge `263.7839` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.411` n `31` status `ready` deltaP `27.9029` edge `1.2649` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.3099` n `31` status `ready` deltaP `26.3432` edge `0.8502` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.8757` n `31` status `ready` deltaP `23.9168` edge `0.8302` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0807` n `31` status `ready` deltaP `20.3579` edge `0.6247` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4575` n `31` status `ready` deltaP `29.6027` edge `0.3055` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1033` n `31` status `ready` deltaP `14.3391` edge `0.7004` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6874` n `31` status `ready` deltaP `38.6762` edge `0.1456` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.512` n `31` status `ready` deltaP `12.1877` edge `0.2389` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3394` n `31` status `ready` deltaP `28.8405` edge `0.0287` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2888` n `31` status `ready` deltaP `28.1003` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2622` n `31` status `ready` deltaP `15.3467` edge `0.1049` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.1872` n `31` status `ready` deltaP `24.6101` edge `0.0182` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.9084` n `31` status `ready` deltaP `5.9687` edge `0.251` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6891` n `31` status `ready` deltaP `8.5136` edge `0.1955` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1247` n `31` status `ready` deltaP `24.4929` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3699` n `31` status `ready` deltaP `9.284` edge `0.0253` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3295` n `31` status `ready` deltaP `11.2903` edge `0.0227` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3891` n `31` status `ready` deltaP `-2.6608` edge `0.0115` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
