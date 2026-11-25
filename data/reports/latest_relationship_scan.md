# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T05:52:29.319627+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32244.0061` n `45` status `ready` deltaP `2.0159` edge `2686.9965` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21980.0809` n `45` status `ready` deltaP `3.1776` edge `1831.6661` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1009.0512` n `31` status `ready` deltaP `2.231` edge `84.0903` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `727.1334` n `31` status `ready` deltaP `4.3962` edge `60.5708` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.993` n `31` status `ready` deltaP `44.6181` edge `3.0353` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.4007` n `31` status `ready` deltaP `50.1736` edge `2.9489` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.9733` n `31` status `ready` deltaP `49.8264` edge `2.6656` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0146` n `31` status `ready` deltaP `28.1323` edge `0.9007` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2934` n `31` status `ready` deltaP `41.2355` edge `0.6937` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.9555` n `31` status `ready` deltaP `36.7673` edge `0.7159` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.6113` n `31` status `ready` deltaP `19.3696` edge `0.9884` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1275` n `31` status `ready` deltaP `45.1389` edge `0.2097` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2592` n `31` status `ready` deltaP `44.4893` edge `0.1545` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8119` n `31` status `ready` deltaP `19.688` edge `0.2051` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.314` n `31` status `ready` deltaP `35.5478` edge `0.0652` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7626` n `31` status `ready` deltaP `12.4058` edge `0.3176` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6327` n `31` status `ready` deltaP `31.0943` edge `0.0206` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5932` n `45` status `ready` deltaP `31.7649` edge `0.0328` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3782` n `31` status `ready` deltaP `12.4058` edge `0.2579` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6015` n `31` status `ready` deltaP `30.3312` edge `0.031` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
