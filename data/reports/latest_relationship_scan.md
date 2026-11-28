# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T16:07:27.054552+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7476`

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

- `news_risk_high->unknown_1h` score `3428.988` n `31` status `ready` deltaP `2.231` edge `285.7517` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3254.8257` n `31` status `ready` deltaP `3.634` edge `271.2169` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.7467` n `31` status `ready` deltaP `37.6083` edge `1.8115` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.701` n `31` status `ready` deltaP `35.7019` edge `1.3204` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0508` n `31` status `ready` deltaP `29.2894` edge `0.8923` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3396` n `31` status `ready` deltaP `24.1689` edge `0.7042` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9296` n `31` status `ready` deltaP `18.4549` edge `0.7789` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.9216` n `31` status `ready` deltaP `33.1088` edge `0.3208` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0924` n `31` status `ready` deltaP `41.969` edge `0.1574` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.935` n `31` status `ready` deltaP `17.0403` edge `0.2418` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6547` n `31` status `ready` deltaP `32.3466` edge `0.0316` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4621` n `31` status `ready` deltaP `26.5165` edge `0.0284` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3559` n `31` status `ready` deltaP `28.8488` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2779` n `31` status `ready` deltaP `15.0473` edge `0.1082` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0667` n `31` status `ready` deltaP `6.8669` edge `0.2653` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9587` n `31` status `ready` deltaP `10.7591` edge `0.2151` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1527` n `31` status `ready` deltaP `24.942` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4932` n `31` status `ready` deltaP `11.2657` edge `0.0279` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.4313` n `31` status `ready` deltaP `12.8147` edge `0.0256` maxDD `-0.7918`
- `market_context_high->fx_1h` score `0.4243` n `65` status `ready` deltaP `11.2391` edge `0.0016` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
