# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T22:37:27.924900+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3348`

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

- `news_risk_high->unknown_1h` score `3216.558` n `31` status `ready` deltaP `2.0813` edge `268.0502` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3192.9474` n `31` status `ready` deltaP `4.3962` edge `266.0553` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `27.9051` n `31` status `ready` deltaP `36.9792` edge `2.0789` maxDD `0.0`
- `news_risk_high->equity_24h` score `24.9761` n `31` status `ready` deltaP `36.1111` edge `1.8406` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.7524` n `31` status `ready` deltaP `36.2847` edge `1.5708` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.8254` n `31` status `ready` deltaP `24.0165` edge `0.7457` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.4757` n `31` status `ready` deltaP `35.3954` edge `0.5184` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.4144` n `31` status `ready` deltaP `22.8327` edge `0.4098` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.3308` n `31` status `ready` deltaP `16.9305` edge `0.8405` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.0068` n `31` status `ready` deltaP `42.5795` edge `0.1462` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.4172` n `31` status `ready` deltaP `37.5` edge `0.1181` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1773` n `31` status `ready` deltaP `18.6401` edge `0.1592` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0021` n `31` status `ready` deltaP `33.7186` edge `0.0514` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.55` n `31` status `ready` deltaP `30.4955` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2694` n `31` status `ready` deltaP `7.9148` edge `0.2843` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0578` n `31` status `ready` deltaP `11.0585` edge `0.2258` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3592` n `31` status `ready` deltaP `27.4869` edge `0.0189` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.7047` n `31` status `ready` deltaP `13.272` edge `0.0576` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2605` n `31` status `ready` deltaP `10.0462` edge `0.0062` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.3916` n `31` status `ready` deltaP `-2.062` edge `0.0073` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
