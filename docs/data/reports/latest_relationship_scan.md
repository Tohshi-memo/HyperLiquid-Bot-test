# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T17:37:30.644448+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_1h` score `3224.4588` n `31` status `ready` deltaP `2.231` edge `268.7076` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.9396` n `31` status `ready` deltaP `4.2437` edge `268.139` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `31.4229` n `31` status `ready` deltaP `40.4514` edge `2.3489` maxDD `0.0`
- `news_risk_high->equity_24h` score `29.1287` n `31` status `ready` deltaP `39.5833` edge `2.1635` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.2294` n `31` status `ready` deltaP `39.7569` edge `1.8374` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3821` n `31` status `ready` deltaP `25.8457` edge `0.7799` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.4711` n `31` status `ready` deltaP `37.682` edge `0.5861` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.2603` n `31` status `ready` deltaP `26.1313` edge `0.4583` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7652` n `31` status `ready` deltaP `18.7598` edge `0.884` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.067` n `31` status `ready` deltaP `40.9722` edge `0.1491` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8004` n `31` status `ready` deltaP `40.149` edge `0.1452` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.543` n `31` status `ready` deltaP `20.2868` edge `0.1787` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.267` n `31` status `ready` deltaP `36.31` edge `0.0562` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7225` n `31` status `ready` deltaP `32.4416` edge `0.0191` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4533` n `31` status `ready` deltaP `9.5615` edge `0.2969` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1816` n `31` status `ready` deltaP `12.4058` edge `0.2327` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4386` n `31` status `ready` deltaP `28.5348` edge `0.0221` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8898` n `31` status `ready` deltaP `14.4915` edge `0.0732` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3198` n `31` status `ready` deltaP `10.9608` edge `0.0077` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.3939` n `31` status `ready` deltaP `-2.2117` edge `0.0081` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
