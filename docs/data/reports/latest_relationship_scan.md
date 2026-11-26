# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T14:37:30.470472+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3224.8008` n `31` status `ready` deltaP `1.7819` edge `268.7391` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3219.1591` n `31` status `ready` deltaP `3.4815` edge `268.2457` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `33.92` n `31` status `ready` deltaP `42.5347` edge `2.5431` maxDD `0.0`
- `news_risk_high->equity_24h` score `32.8569` n `31` status `ready` deltaP `41.6667` edge `2.4603` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `27.9088` n `31` status `ready` deltaP `41.8403` edge `2.0468` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.4229` n `31` status `ready` deltaP `25.8457` edge `0.7833` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.0655` n `31` status `ready` deltaP `37.9869` edge `0.6336` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.0402` n `31` status `ready` deltaP `28.2146` edge `0.5094` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8247` n `31` status `ready` deltaP `18.9123` edge `0.8906` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.5516` n `31` status `ready` deltaP `43.0556` edge `0.1756` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8691` n `31` status `ready` deltaP `40.8434` edge `0.1463` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7422` n `31` status `ready` deltaP `20.5862` edge `0.1933` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3442` n `31` status `ready` deltaP `36.6149` edge `0.0606` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7656` n `31` status `ready` deltaP `32.741` edge `0.0207` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4634` n `31` status `ready` deltaP `9.7112` edge `0.2972` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.223` n `31` status `ready` deltaP `12.5555` edge `0.237` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4394` n `31` status `ready` deltaP `28.3851` edge `0.0232` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9694` n `31` status `ready` deltaP `15.4062` edge `0.0773` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.4169` n `31` status `ready` deltaP `12.3328` edge `0.011` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4059` n `31` status `ready` deltaP `-2.3614` edge `0.0081` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
