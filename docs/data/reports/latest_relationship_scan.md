# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T18:22:35.871512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3251`

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

- `news_risk_high->unknown_1h` score `3224.448` n `31` status `ready` deltaP `2.231` edge `268.7067` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3218.1546` n `31` status `ready` deltaP `4.3962` edge `268.1559` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `30.864` n `31` status `ready` deltaP `39.9306` edge `2.3058` maxDD `0.0`
- `news_risk_high->equity_24h` score `28.4042` n `31` status `ready` deltaP `39.0625` edge `2.1066` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.6765` n `31` status `ready` deltaP `39.2361` edge `1.7948` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3461` n `31` status `ready` deltaP `25.8457` edge `0.7769` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3451` n `31` status `ready` deltaP `37.682` edge `0.5756` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.101` n `31` status `ready` deltaP `25.6105` edge `0.4485` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7177` n `31` status `ready` deltaP `18.7598` edge `0.8779` maxDD `-7.6714`
- `news_risk_high->index_24h` score `4.9641` n `31` status `ready` deltaP `40.4514` edge `0.144` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8306` n `31` status `ready` deltaP `40.4962` edge `0.1454` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5382` n `31` status `ready` deltaP `20.4365` edge `0.1773` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2464` n `31` status `ready` deltaP `36.1576` edge `0.0555` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7081` n `31` status `ready` deltaP `32.2919` edge `0.0189` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4299` n `31` status `ready` deltaP `9.2621` edge `0.2959` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1707` n `31` status `ready` deltaP `12.2561` edge `0.2323` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4472` n `31` status `ready` deltaP `28.6845` edge `0.0222` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8766` n `31` status `ready` deltaP `14.4915` edge `0.0715` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3` n `31` status `ready` deltaP `10.656` edge `0.0072` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4395` n `31` status `ready` deltaP `-2.6608` edge `0.0073` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
