# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T18:37:28.734951+00:00`
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

- `news_risk_high->unknown_1h` score `3222.18` n `31` status `ready` deltaP `2.231` edge `268.5177` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3215.8266` n `31` status `ready` deltaP `4.3962` edge `267.9619` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `30.6654` n `31` status `ready` deltaP `39.7569` edge `2.2904` maxDD `0.0`
- `news_risk_high->equity_24h` score `28.1767` n `31` status `ready` deltaP `38.8889` edge `2.0888` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.485` n `31` status `ready` deltaP `39.0625` edge `1.78` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3171` n `31` status `ready` deltaP `25.6933` edge `0.7755` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2995` n `31` status `ready` deltaP `37.682` edge `0.5718` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.0488` n `31` status `ready` deltaP `25.4369` edge `0.4453` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.6989` n `31` status `ready` deltaP `18.7598` edge `0.8755` maxDD `-7.6714`
- `news_risk_high->index_24h` score `4.931` n `31` status `ready` deltaP `40.2778` edge `0.1424` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8445` n `31` status `ready` deltaP `40.6698` edge `0.1454` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5154` n `31` status `ready` deltaP `20.2868` edge `0.1764` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2428` n `31` status `ready` deltaP `36.1576` edge `0.0552` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6949` n `31` status `ready` deltaP `32.1422` edge `0.0188` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4034` n `31` status `ready` deltaP `9.1124` edge `0.2935` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1513` n `31` status `ready` deltaP `12.1064` edge `0.2308` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4378` n `31` status `ready` deltaP `28.5348` edge `0.022` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8719` n `31` status `ready` deltaP `14.4915` edge `0.0709` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2906` n `31` status `ready` deltaP `10.5035` edge `0.007` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4538` n `31` status `ready` deltaP `-2.8105` edge `0.0071` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
