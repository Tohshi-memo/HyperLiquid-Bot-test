# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T07:52:24.374889+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3225.4189` n `31` status `ready` deltaP `1.6322` edge `268.7916` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.1274` n `31` status `ready` deltaP `3.7864` edge `265.1577` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.0067` n `31` status `ready` deltaP `30.7292` edge `1.5457` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.8471` n `31` status `ready` deltaP `30.2083` edge `1.3692` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.8193` n `31` status `ready` deltaP `29.8611` edge `1.1192` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.9782` n `31` status `ready` deltaP `22.1872` edge `0.6873` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.8281` n `31` status `ready` deltaP `31.5844` edge `0.4065` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.7186` n `31` status `ready` deltaP `15.1013` edge `0.7742` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.3458` n `31` status `ready` deltaP `18.1452` edge `0.352` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6334` n `31` status `ready` deltaP `38.5865` edge `0.1417` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.3757` n `31` status `ready` deltaP `31.7708` edge `0.0695` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.7108` n `31` status `ready` deltaP `16.694` edge `0.1333` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.6308` n `31` status `ready` deltaP `30.5173` edge `0.0418` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.441` n `31` status `ready` deltaP `29.4476` edge `0.0156` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0838` n `31` status `ready` deltaP `6.8669` edge `0.2675` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8839` n `31` status `ready` deltaP `10.0106` edge `0.2105` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1613` n `31` status `ready` deltaP `25.0917` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4443` n `31` status `ready` deltaP `12.5098` edge `0.0293` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1288` n `31` status `ready` deltaP `5.1682` edge `-0.0112` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6923` n `31` status `ready` deltaP `-5.2057` edge `0.0032` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
