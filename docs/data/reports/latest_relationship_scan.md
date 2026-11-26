# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T22:07:27.535678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3336`

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

- `news_risk_high->unknown_1h` score `3216.0168` n `31` status `ready` deltaP `2.0813` edge `268.0051` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3192.9486` n `31` status `ready` deltaP `4.3962` edge `266.0554` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `28.1921` n `31` status `ready` deltaP `37.3264` edge `2.1005` maxDD `0.0`
- `news_risk_high->equity_24h` score `25.3219` n `31` status `ready` deltaP `36.4583` edge `1.8671` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.043` n `31` status `ready` deltaP `36.6319` edge `1.5927` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.9024` n `31` status `ready` deltaP `24.1689` edge `0.7511` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5685` n `31` status `ready` deltaP `35.7003` edge `0.5241` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.4631` n `31` status `ready` deltaP `23.0063` edge `0.4127` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.3826` n `31` status `ready` deltaP `17.2354` edge `0.8451` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9791` n `31` status `ready` deltaP `42.2323` edge `0.1462` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.4786` n `31` status `ready` deltaP `37.8472` edge `0.1209` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1929` n `31` status `ready` deltaP `18.6401` edge `0.1605` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0313` n `31` status `ready` deltaP `34.0234` edge `0.0518` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.55` n `31` status `ready` deltaP `30.4955` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2499` n `31` status `ready` deltaP `7.7651` edge `0.2828` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.043` n `31` status `ready` deltaP `10.9088` edge `0.2249` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3623` n `31` status `ready` deltaP `27.4869` edge `0.0193` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.7393` n `31` status `ready` deltaP `13.5769` edge `0.06` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2621` n `31` status `ready` deltaP `10.0462` edge `0.0064` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4047` n `31` status `ready` deltaP `-2.2117` edge `0.0072` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
