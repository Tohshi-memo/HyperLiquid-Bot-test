# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T22:37:23.756067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3302.1985` n `31` status `ready` deltaP `1.6322` edge `275.1899` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3169.8641` n `31` status `ready` deltaP `3.3291` edge `264.1388` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.3048` n `31` status `ready` deltaP `27.7296` edge `1.2572` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4229` n `31` status `ready` deltaP `27.0364` edge `0.855` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.1205` n `31` status `ready` deltaP `23.9168` edge `0.8506` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2097` n `31` status `ready` deltaP `20.8153` edge `0.6324` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.5071` n `31` status `ready` deltaP `29.9076` edge `0.3076` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1454` n `31` status `ready` deltaP `14.3391` edge `0.7058` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6766` n `31` status `ready` deltaP `38.6762` edge `0.1447` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5912` n `31` status `ready` deltaP `12.1877` edge `0.2455` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3528` n `31` status `ready` deltaP `28.993` edge `0.0288` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.285` n `31` status `ready` deltaP `15.4964` edge `0.1058` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.2756` n `31` status `ready` deltaP `27.9506` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2016` n `31` status `ready` deltaP `24.6101` edge `0.0194` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.9458` n `31` status `ready` deltaP `6.4178` edge `0.2528` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7242` n `31` status `ready` deltaP `8.813` edge `0.198` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1325` n `31` status `ready` deltaP `24.6426` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4071` n `31` status `ready` deltaP `9.8938` edge `0.026` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3554` n `31` status `ready` deltaP `11.5952` edge `0.024` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3507` n `31` status `ready` deltaP `-2.2117` edge `0.0117` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
