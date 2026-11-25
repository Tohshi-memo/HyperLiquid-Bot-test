# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T06:07:24.136423+00:00`
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

- `market_context_high->unknown_1h` score `32244.1657` n `45` status `ready` deltaP `2.0159` edge `2687.0098` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21980.8513` n `45` status `ready` deltaP `3.1776` edge `1831.7303` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1009.2108` n `31` status `ready` deltaP `2.231` edge `84.1036` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `727.9038` n `31` status `ready` deltaP `4.3962` edge `60.635` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `40.1034` n `31` status `ready` deltaP `44.6181` edge `3.0445` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.4511` n `31` status `ready` deltaP `50.1736` edge `2.9531` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.0369` n `31` status `ready` deltaP `49.8264` edge `2.6709` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0038` n `31` status `ready` deltaP `28.1323` edge `0.8998` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.3078` n `31` status `ready` deltaP `41.2355` edge `0.6949` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.9989` n `31` status `ready` deltaP `36.9198` edge `0.7185` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.6113` n `31` status `ready` deltaP `19.3696` edge `0.9884` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1534` n `31` status `ready` deltaP `45.3125` edge `0.2107` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2405` n `31` status `ready` deltaP `44.3157` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8347` n `31` status `ready` deltaP `19.8377` edge `0.206` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3286` n `31` status `ready` deltaP `35.7003` edge `0.0654` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7728` n `31` status `ready` deltaP `12.5555` edge `0.3179` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6447` n `31` status `ready` deltaP `31.244` edge `0.0206` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5932` n `45` status `ready` deltaP `31.7649` edge `0.0328` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3891` n `31` status `ready` deltaP `12.5555` edge `0.2583` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6038` n `31` status `ready` deltaP `30.3312` edge `0.0313` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
