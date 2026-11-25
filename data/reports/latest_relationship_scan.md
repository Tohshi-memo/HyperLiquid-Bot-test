# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T06:37:28.801881+00:00`
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

- `market_context_high->unknown_1h` score `32241.7369` n `45` status `ready` deltaP `2.0159` edge `2686.8074` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21980.8993` n `45` status `ready` deltaP `3.1776` edge `1831.7343` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1006.782` n `31` status `ready` deltaP `2.231` edge `83.9012` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `867.0371` n `31` status `ready` deltaP `5.7292` edge `72.2149` maxDD `0.0`
- `news_risk_high->unknown_4h` score `727.9518` n `31` status `ready` deltaP `4.3962` edge `60.639` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `40.3556` n `31` status `ready` deltaP `44.9653` edge `3.0632` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.5495` n `31` status `ready` deltaP `50.1736` edge `2.9613` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.1636` n `31` status `ready` deltaP `50.0` edge `2.6803` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9582` n `31` status `ready` deltaP `28.1323` edge `0.896` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.3318` n `31` status `ready` deltaP `41.2355` edge `0.6969` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.0593` n `31` status `ready` deltaP `37.2247` edge `0.7215` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5876` n `31` status `ready` deltaP `19.0647` edge `0.9874` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.2076` n `31` status `ready` deltaP `45.6597` edge `0.2129` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2031` n `31` status `ready` deltaP `43.9684` edge `0.1533` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8515` n `31` status `ready` deltaP `19.9874` edge `0.2064` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3298` n `31` status `ready` deltaP `35.7003` edge `0.0655` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7603` n `31` status `ready` deltaP `12.4058` edge `0.3173` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6327` n `31` status `ready` deltaP `31.0943` edge `0.0206` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5932` n `45` status `ready` deltaP `31.7649` edge `0.0328` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3673` n `31` status `ready` deltaP `12.4058` edge `0.2565` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
