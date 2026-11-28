# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T15:22:23.758785+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7456`

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

- `news_risk_high->unknown_1h` score `3426.1728` n `31` status `ready` deltaP `2.231` edge `285.5171` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3255.0993` n `31` status `ready` deltaP `3.634` edge `271.2397` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.5539` n `31` status `ready` deltaP `37.0884` edge `1.7989` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.4662` n `31` status `ready` deltaP `35.182` edge `1.3043` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0232` n `31` status `ready` deltaP `29.2894` edge `0.89` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3168` n `31` status `ready` deltaP `24.1689` edge `0.7023` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.8943` n `31` status `ready` deltaP `18.1501` edge `0.7764` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.867` n `31` status `ready` deltaP `32.6515` edge `0.3193` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0912` n `31` status `ready` deltaP `41.969` edge `0.1573` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9482` n `31` status `ready` deltaP `17.0403` edge `0.2429` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6146` n `31` status `ready` deltaP `31.8893` edge `0.0313` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4549` n `31` status `ready` deltaP `26.5165` edge `0.0278` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3319` n `31` status `ready` deltaP `28.5494` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2491` n `31` status `ready` deltaP `14.7479` edge `0.1078` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0682` n `31` status `ready` deltaP `6.8669` edge `0.2655` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9595` n `31` status `ready` deltaP `10.7591` edge `0.2152` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1449` n `31` status `ready` deltaP `24.7923` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4663` n `31` status `ready` deltaP `10.8084` edge `0.0275` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.4492` n `65` status `ready` deltaP `11.6882` edge `0.0018` maxDD `-0.1042`
- `market_context_high->metal_4h` score `0.4159` n `54` status `ready` deltaP `8.4745` edge `0.0193` maxDD `-0.2914`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
