# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T08:07:29.579831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4164`

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

- `market_context_high->unknown_1h` score `32238.6649` n `45` status `ready` deltaP `2.1656` edge `2686.5504` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21977.1025` n `45` status `ready` deltaP `3.1776` edge `1831.4179` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1003.7099` n `31` status `ready` deltaP `2.3807` edge `83.6442` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `805.8971` n `31` status `ready` deltaP `5.7292` edge `67.1199` maxDD `0.0`
- `news_risk_high->unknown_4h` score `724.155` n `31` status `ready` deltaP `4.3962` edge `60.3226` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `41.2226` n `31` status `ready` deltaP `46.0069` edge `3.1285` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.8843` n `31` status `ready` deltaP `50.1736` edge `2.9892` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.5941` n `31` status `ready` deltaP `50.5208` edge `2.7127` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8592` n `31` status `ready` deltaP `27.675` edge `0.8908` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.4278` n `31` status `ready` deltaP `41.2355` edge `0.7049` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2267` n `31` status `ready` deltaP `37.682` edge `0.7324` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5805` n `31` status `ready` deltaP `18.9123` edge `0.9875` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.3857` n `31` status `ready` deltaP `46.7014` edge `0.2208` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1193` n `31` status `ready` deltaP `43.1004` edge `0.1521` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9966` n `31` status `ready` deltaP `20.7359` edge `0.2135` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3808` n `31` status `ready` deltaP `36.1576` edge `0.0667` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.8063` n `31` status `ready` deltaP `12.5555` edge `0.3222` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7034` n `31` status `ready` deltaP `31.8428` edge `0.0215` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.598` n `45` status `ready` deltaP `31.7649` edge `0.0332` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4078` n `31` status `ready` deltaP `12.7052` edge `0.2597` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
