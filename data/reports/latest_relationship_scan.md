# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T16:07:23.964493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4036`

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

- `market_context_high->unknown_1h` score `12031.5368` n `106` status `ready` deltaP `-0.6921` edge `1002.6525` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7502.8861` n `106` status `ready` deltaP `-2.5742` edge `625.2882` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1411.1745` n `31` status `ready` deltaP `4.1771` edge `117.5876` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1253.0277` n `31` status `ready` deltaP `3.634` edge `104.4004` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9454` n `31` status `ready` deltaP `40.121` edge `0.7762` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.6458` n `31` status `ready` deltaP `23.7116` edge `0.8161` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6214` n `31` status `ready` deltaP `14.644` edge `0.893` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.957` n `31` status `ready` deltaP `19.5383` edge `0.2182` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4768` n `31` status `ready` deltaP `36.1576` edge `0.0747` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.707` n `31` status `ready` deltaP `31.6931` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4097` n `31` status `ready` deltaP `8.9627` edge `0.2953` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0393` n `31` status `ready` deltaP `8.2142` edge `0.2424` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5353` n `31` status `ready` deltaP `20.5891` edge `0.1153` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.48` n `31` status `ready` deltaP `27.936` edge `0.0314` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.685` n `31` status `ready` deltaP `15.8389` edge `0.022` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0585` n `31` status `ready` deltaP `1.5308` edge `0.0111` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3635` n `106` status `ready` deltaP `1.8557` edge `0.0075` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4095` n `106` status `ready` deltaP `1.9913` edge `0.0013` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2598` n `106` status `ready` deltaP `-9.0753` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5259` n `106` status `ready` deltaP `-0.3164` edge `0.0037` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
