# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T15:56:07.899420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3720`

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

- `market_context_high->unknown_1h` score `32187.6997` n `45` status `ready` deltaP `2.1656` edge `2682.3033` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21893.3721` n `45` status `ready` deltaP `2.8727` edge `1824.4424` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `952.7447` n `31` status `ready` deltaP `2.3807` edge `79.3971` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `640.4246` n `31` status `ready` deltaP `4.0913` edge `53.3471` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `438.2459` n `31` status `ready` deltaP `5.7292` edge `36.4823` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.5819` n `31` status `ready` deltaP `51.3889` edge `3.4559` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.1105` n `31` status `ready` deltaP `52.9514` edge `3.1562` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.6138` n `31` status `ready` deltaP `55.3819` edge `2.8486` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9738` n `31` status `ready` deltaP `41.2355` edge `0.7504` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.9645` n `31` status `ready` deltaP `27.3701` edge `0.9016` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.4144` n `31` status `ready` deltaP `38.1393` edge `0.745` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5017` n `31` status `ready` deltaP `18.9123` edge `0.9774` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.2819` n `31` status `ready` deltaP `52.0833` edge `0.2596` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3794` n `31` status `ready` deltaP `46.0518` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9858` n `31` status `ready` deltaP `20.5862` edge `0.2136` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.462` n `31` status `ready` deltaP `36.7673` edge `0.0694` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.695` n `31` status `ready` deltaP `31.6931` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6606` n `31` status `ready` deltaP `11.3579` edge `0.3115` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4566` n `45` status `ready` deltaP `30.0881` edge `0.0326` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4273` n `31` status `ready` deltaP `13.1543` edge `0.2592` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
