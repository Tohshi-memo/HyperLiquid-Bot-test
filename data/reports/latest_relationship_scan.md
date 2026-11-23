# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T22:37:28.155749+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32419.2025` n `45` status `ready` deltaP `2.6147` edge `2701.5922` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22262.6442` n `45` status `ready` deltaP `3.4824` edge `1855.211` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1209.6731` n `31` status `ready` deltaP `2.8298` edge `100.8048` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1027.291` n `31` status `ready` deltaP `4.701` edge `85.5819` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.7044` n `31` status `ready` deltaP `43.75` edge `2.9337` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9025` n `31` status `ready` deltaP `45.4861` edge `2.6053` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.87` n `31` status `ready` deltaP `45.6597` edge `2.2681` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.3411` n `31` status `ready` deltaP `44.8813` edge `0.7567` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.2734` n `31` status `ready` deltaP `22.4921` edge `0.7932` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6587` n `31` status `ready` deltaP `30.8222` edge `0.5643` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.5141` n `31` status `ready` deltaP `55.6004` edge `0.185` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2982` n `31` status `ready` deltaP `12.3574` edge `0.8668` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9745` n `31` status `ready` deltaP `41.6667` edge `0.2201` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3061` n `45` status `ready` deltaP `39.3868` edge `0.0414` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1653` n `31` status `ready` deltaP `17.5922` edge `0.1652` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9271` n `31` status `ready` deltaP `32.3466` edge `0.0543` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4913` n `31` status `ready` deltaP `29.747` edge `0.0178` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4898` n `31` status `ready` deltaP `10.9088` edge `0.2926` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1335` n `31` status `ready` deltaP `10.4597` edge `0.2395` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5461` n `31` status `ready` deltaP `29.8821` edge `0.0269` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
