# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T18:37:41.637534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3289.5267` n `31` status `ready` deltaP `1.6201` edge `274.134` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3186.8373` n `31` status `ready` deltaP `3.3191` edge `265.5533` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.2751` n `31` status `ready` deltaP `25.8232` edge `1.1841` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.8069` n `31` status `ready` deltaP `23.9168` edge `0.9078` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.9188` n `31` status `ready` deltaP `25.13` edge `0.8257` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0814` n `31` status `ready` deltaP `20.8916` edge `0.6212` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.5571` n `31` status `ready` deltaP `30.1419` edge `0.3102` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9854` n `31` status `ready` deltaP `13.4973` edge `0.6909` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6514` n `31` status `ready` deltaP `38.6762` edge `0.1426` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8132` n `31` status `ready` deltaP `12.1877` edge `0.264` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3935` n `31` status `ready` deltaP `29.3809` edge `0.0296` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2772` n `31` status `ready` deltaP `27.8799` edge `0.0124` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2769` n `31` status `ready` deltaP `15.2755` edge `0.1066` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.2749` n `31` status `ready` deltaP `24.9567` edge `0.0232` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.8945` n `31` status `ready` deltaP `6.196` edge `0.2477` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6851` n `31` status `ready` deltaP `8.7371` edge `0.1935` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1581` n `31` status `ready` deltaP `25.0156` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3828` n `31` status `ready` deltaP `9.9671` edge `0.0224` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3726` n `31` status `ready` deltaP `11.6708` edge `0.0257` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3639` n `31` status `ready` deltaP `-2.1361` edge `0.0101` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
