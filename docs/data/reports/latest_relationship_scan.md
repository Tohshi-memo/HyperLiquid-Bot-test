# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T11:22:24.251312+00:00`
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

- `news_risk_high->unknown_1h` score `3250.3921` n `31` status `ready` deltaP `1.6322` edge `270.8727` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3201.4942` n `31` status `ready` deltaP `3.7864` edge `266.7716` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.0595` n `31` status `ready` deltaP `28.2986` edge `1.3163` maxDD `0.0`
- `news_risk_high->equity_24h` score `16.0798` n `31` status `ready` deltaP `27.7778` edge `1.1548` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.346` n `31` status `ready` deltaP `27.4306` edge `0.9293` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.4821` n `31` status `ready` deltaP `20.8153` edge `0.6551` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.4355` n `31` status `ready` deltaP `30.5173` edge `0.3809` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.3426` n `31` status `ready` deltaP `13.272` edge `0.7382` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `4.657` n `31` status `ready` deltaP `15.7146` edge `0.3108` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->index_24h` score `2.9316` n `31` status `ready` deltaP `29.3403` edge `0.0487` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5884` n `31` status `ready` deltaP `30.2125` edge `0.0403` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5141` n `31` status `ready` deltaP `15.7958` edge `0.1229` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3571` n `31` status `ready` deltaP `28.5494` edge `0.0146` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9724` n `31` status `ready` deltaP `5.9687` edge `0.2592` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8005` n `31` status `ready` deltaP `9.4118` edge `0.2038` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.152` n `31` status `ready` deltaP `24.942` edge `0.0093` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3374` n `31` status `ready` deltaP `11.4427` edge `0.0227` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0388` n `31` status `ready` deltaP `6.9974` edge `-0.0019` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5844` n `31` status `ready` deltaP `-4.1578` edge `0.0052` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
