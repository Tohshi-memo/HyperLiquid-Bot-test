# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T15:52:28.235959+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3491`

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

- `news_risk_high->unknown_1h` score `3223.6608` n `31` status `ready` deltaP `1.9316` edge `268.6431` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.1119` n `31` status `ready` deltaP `3.4815` edge `268.0751` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `32.8689` n `31` status `ready` deltaP `41.6667` edge `2.4613` maxDD `0.0`
- `news_risk_high->equity_24h` score `31.3343` n `31` status `ready` deltaP `40.7986` edge `2.3392` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `26.7738` n `31` status `ready` deltaP `40.9722` edge `1.958` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3879` n `31` status `ready` deltaP `25.6933` edge `0.7814` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.7807` n `31` status `ready` deltaP `37.682` edge `0.6119` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.7031` n `31` status `ready` deltaP `27.3466` edge `0.4871` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8027` n `31` status `ready` deltaP `18.7598` edge `0.8888` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3526` n `31` status `ready` deltaP `42.1875` edge `0.1648` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8052` n `31` status `ready` deltaP `40.149` edge `0.1456` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.705` n `31` status `ready` deltaP `20.7359` edge `0.1892` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2922` n `31` status `ready` deltaP `36.31` edge `0.0583` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7572` n `31` status `ready` deltaP `32.741` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.472` n `31` status `ready` deltaP `9.8609` edge `0.2973` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2175` n `31` status `ready` deltaP `12.5555` edge `0.2363` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4215` n `31` status `ready` deltaP `28.2354` edge `0.0219` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9205` n `31` status `ready` deltaP `14.7964` edge `0.0751` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.364` n `31` status `ready` deltaP `11.5706` edge `0.0093` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4251` n `31` status `ready` deltaP `-2.5111` edge `0.0075` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
