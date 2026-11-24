# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T17:52:39.198610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4200`

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

- `market_context_high->unknown_1h` score `32290.0178` n `45` status `ready` deltaP `1.4171` edge `2690.8348` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22100.0951` n `45` status `ready` deltaP `3.0251` edge `1841.6683` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1055.0629` n `31` status `ready` deltaP `1.6322` edge `87.9286` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `847.1476` n `31` status `ready` deltaP `4.2437` edge `70.573` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.8518` n `31` status `ready` deltaP `49.6528` edge `2.8233` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.8415` n `31` status `ready` deltaP `42.0139` edge `2.7067` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.1174` n `31` status `ready` deltaP `47.7431` edge `2.4415` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.2885` n `31` status `ready` deltaP `25.236` edge `0.8595` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1002` n `31` status `ready` deltaP `41.2355` edge `0.6776` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.7012` n `31` status `ready` deltaP `33.7186` edge `0.6317` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.0083` n `31` status `ready` deltaP `16.4732` edge `0.9304` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.2727` n `31` status `ready` deltaP `52.8226` edge `0.1834` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.3214` n `31` status `ready` deltaP `39.7569` edge `0.1784` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4749` n `31` status `ready` deltaP `18.6401` edge `0.184` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9825` n `31` status `ready` deltaP `32.499` edge `0.0579` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8451` n `45` status `ready` deltaP `34.5088` edge `0.0355` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.5974` n `31` status `ready` deltaP `11.5076` edge `0.3024` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.538` n `31` status `ready` deltaP `30.1961` edge `0.0187` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2341` n `31` status `ready` deltaP `11.0585` edge `0.2484` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6529` n `31` status `ready` deltaP `30.93` edge `0.0336` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
