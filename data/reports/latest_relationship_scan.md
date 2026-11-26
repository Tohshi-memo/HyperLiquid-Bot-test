# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T17:52:30.874878+00:00`
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

- `news_risk_high->unknown_1h` score `3224.4276` n `31` status `ready` deltaP `2.0813` edge `268.706` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.9408` n `31` status `ready` deltaP `4.2437` edge `268.1391` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `31.2278` n `31` status `ready` deltaP `40.2778` edge `2.3338` maxDD `0.0`
- `news_risk_high->equity_24h` score `28.8688` n `31` status `ready` deltaP `39.4097` edge `2.143` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.0367` n `31` status `ready` deltaP `39.5833` edge `1.8225` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3725` n `31` status `ready` deltaP `25.8457` edge `0.7791` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.4171` n `31` status `ready` deltaP `37.682` edge `0.5816` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.2032` n `31` status `ready` deltaP `25.9577` edge `0.4547` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7512` n `31` status `ready` deltaP `18.7598` edge `0.8822` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.0303` n `31` status `ready` deltaP `40.7986` edge `0.1472` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8016` n `31` status `ready` deltaP `40.149` edge `0.1453` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5298` n `31` status `ready` deltaP `20.2868` edge `0.1776` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2634` n `31` status `ready` deltaP `36.31` edge `0.0559` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7081` n `31` status `ready` deltaP `32.2919` edge `0.0189` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4548` n `31` status `ready` deltaP `9.5615` edge `0.2971` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1824` n `31` status `ready` deltaP `12.4058` edge `0.2328` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4386` n `31` status `ready` deltaP `28.5348` edge `0.0221` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8851` n `31` status `ready` deltaP `14.4915` edge `0.0726` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3103` n `31` status `ready` deltaP `10.8084` edge `0.0075` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4083` n `31` status `ready` deltaP `-2.3614` edge `0.0079` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
