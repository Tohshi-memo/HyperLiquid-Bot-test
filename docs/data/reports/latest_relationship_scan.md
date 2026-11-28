# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T17:22:25.046581+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7546`

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

- `news_risk_high->unknown_1h` score `3437.2535` n `31` status `ready` deltaP `2.3807` edge `286.4395` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3268.0389` n `31` status `ready` deltaP `3.634` edge `272.318` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.1064` n `31` status `ready` deltaP `38.4749` edge `1.8357` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.1939` n `31` status `ready` deltaP `36.5685` edge `1.3557` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1228` n `31` status `ready` deltaP `29.2894` edge `0.8983` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4831` n `31` status `ready` deltaP `24.7787` edge `0.7121` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0126` n `31` status `ready` deltaP `33.871` edge `0.3233` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9869` n `31` status `ready` deltaP `18.9123` edge `0.7832` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.1503` n `31` status `ready` deltaP `42.6623` edge `0.1576` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.917` n `31` status `ready` deltaP `17.0403` edge `0.2403` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7217` n `31` status `ready` deltaP `33.1088` edge `0.0321` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4904` n `31` status `ready` deltaP `26.6898` edge `0.0296` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3786` n `31` status `ready` deltaP `29.1482` edge `0.0124` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3042` n `31` status `ready` deltaP `15.3467` edge `0.1084` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0978` n `31` status `ready` deltaP `7.1663` edge `0.2673` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0039` n `31` status `ready` deltaP `11.2082` edge `0.2179` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5399` n `31` status `ready` deltaP `12.0279` edge `0.0288` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.4757` n `31` status `ready` deltaP `13.5769` edge `0.0262` maxDD `-0.7918`
- `market_context_high->fx_1h` score `0.4406` n `65` status `ready` deltaP `11.5385` edge `0.0017` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
