# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T18:52:31.724332+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3156`

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

- `news_risk_high->unknown_1h` score `3222.1548` n `31` status `ready` deltaP `2.231` edge `268.5156` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3215.8518` n `31` status `ready` deltaP `4.3962` edge `267.964` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `30.4727` n `31` status `ready` deltaP `39.5833` edge `2.2755` maxDD `0.0`
- `news_risk_high->equity_24h` score `27.9708` n `31` status `ready` deltaP `38.7153` edge `2.0728` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.2983` n `31` status `ready` deltaP `38.8889` edge `1.7656` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.2857` n `31` status `ready` deltaP `25.5409` edge `0.7739` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2623` n `31` status `ready` deltaP `37.682` edge `0.5687` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.0001` n `31` status `ready` deltaP `25.2633` edge `0.4424` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.6723` n `31` status `ready` deltaP `18.6074` edge `0.8731` maxDD `-7.6714`
- `news_risk_high->index_24h` score `4.9015` n `31` status `ready` deltaP `40.1042` edge `0.1411` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8595` n `31` status `ready` deltaP `40.8434` edge `0.1455` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.4951` n `31` status `ready` deltaP `20.1371` edge `0.1757` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2282` n `31` status `ready` deltaP `36.0051` edge `0.055` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6818` n `31` status `ready` deltaP `31.9925` edge `0.0187` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3831` n `31` status `ready` deltaP `8.9627` edge `0.2919` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1372` n `31` status `ready` deltaP `11.9567` edge `0.23` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4371` n `31` status `ready` deltaP `28.5348` edge `0.0219` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.868` n `31` status `ready` deltaP `14.4915` edge `0.0704` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2906` n `31` status `ready` deltaP `10.5035` edge `0.007` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4682` n `31` status `ready` deltaP `-2.9602` edge `0.0069` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
