# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T17:52:25.680840+00:00`
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

- `news_risk_high->unknown_1h` score `3279.9853` n `31` status `ready` deltaP `1.6322` edge `273.3388` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3184.3169` n `31` status `ready` deltaP `3.3291` edge `265.3432` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.2258` n `31` status `ready` deltaP `25.8681` edge `1.1797` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.9987` n `31` status `ready` deltaP `23.9583` edge `0.9235` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.87` n `31` status `ready` deltaP `25.0` edge `0.8225` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.9609` n `31` status `ready` deltaP `20.5104` edge `0.6137` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.6277` n `31` status `ready` deltaP `30.3649` edge `0.3146` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9097` n `31` status `ready` deltaP `13.272` edge `0.6827` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6394` n `31` status `ready` deltaP `38.5865` edge `0.1422` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8584` n `31` status `ready` deltaP `12.2424` edge `0.2674` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.433` n `31` status `ready` deltaP `29.7551` edge `0.0304` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.3294` n `31` status `ready` deltaP `15.4964` edge `0.1095` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.3278` n `31` status `ready` deltaP `25.3472` edge `0.025` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2984` n `31` status `ready` deltaP `28.1003` edge `0.0127` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9209` n `31` status `ready` deltaP `6.2681` edge `0.2506` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7015` n `31` status `ready` deltaP `8.813` edge `0.1951` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1722` n `31` status `ready` deltaP `25.2414` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3592` n `31` status `ready` deltaP `11.4427` edge `0.0255` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3428` n `31` status `ready` deltaP `9.5889` edge `0.0198` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4035` n `31` status `ready` deltaP `-2.5111` edge `0.0093` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
