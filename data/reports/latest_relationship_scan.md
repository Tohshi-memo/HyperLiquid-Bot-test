# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T06:07:30.037240+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3680`

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

- `news_risk_high->unknown_1h` score `3352.3789` n `31` status `ready` deltaP `1.4825` edge `279.3726` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3210.7641` n `31` status `ready` deltaP `3.634` edge `267.5451` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.7911` n `31` status `ready` deltaP `30.8492` edge `1.4436` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.812` n `31` status `ready` deltaP `28.7695` edge `0.9592` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.612` n `31` status `ready` deltaP `24.6101` edge `0.8036` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.6629` n `31` status `ready` deltaP `20.2055` edge `0.5909` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.1174` n `31` status `ready` deltaP `28.2308` edge `0.2863` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.751` n `31` status `ready` deltaP `38.6762` edge `0.1509` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.7358` n `31` status `ready` deltaP `14.1866` edge `0.6543` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.4331` n `31` status `ready` deltaP `12.8809` edge `0.2277` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.272` n `31` status `ready` deltaP `27.9506` edge `0.0115` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.2287` n `31` status `ready` deltaP `27.621` edge `0.0276` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2257` n `31` status `ready` deltaP `24.9567` edge `0.0191` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1064` n `31` status `ready` deltaP `14.2988` edge `0.0989` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7306` n `31` status `ready` deltaP `5.3699` edge `0.2322` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6321` n `31` status `ready` deltaP `8.6633` edge `0.1872` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1045` n `31` status `ready` deltaP `24.1935` edge `0.0082` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.2922` n `31` status `ready` deltaP `7.7596` edge `0.0255` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2552` n `31` status `ready` deltaP `10.2232` edge `0.0203` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3244` n `31` status `ready` deltaP `-1.9123` edge `0.0119` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
