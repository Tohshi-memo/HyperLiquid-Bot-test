# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T06:52:27.270414+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4104`

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

- `market_context_high->unknown_1h` score `32237.6713` n `45` status `ready` deltaP `2.0159` edge `2686.4686` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21978.7357` n `45` status `ready` deltaP `3.1776` edge `1831.554` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1002.7164` n `31` status `ready` deltaP `2.231` edge `83.5624` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `872.0939` n `31` status `ready` deltaP `5.7292` edge `72.6363` maxDD `0.0`
- `news_risk_high->unknown_4h` score `725.7882` n `31` status `ready` deltaP `4.3962` edge `60.4587` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `40.4931` n `31` status `ready` deltaP `45.1389` edge `3.0735` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.6083` n `31` status `ready` deltaP `50.1736` edge `2.9662` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.2411` n `31` status `ready` deltaP `50.1736` edge `2.6856` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9402` n `31` status `ready` deltaP `28.1323` edge `0.8945` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.3462` n `31` status `ready` deltaP `41.2355` edge `0.6981` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.0871` n `31` status `ready` deltaP `37.3771` edge `0.7228` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5853` n `31` status `ready` deltaP `19.0647` edge `0.9871` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.2371` n `31` status `ready` deltaP `45.8333` edge `0.2142` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1857` n `31` status `ready` deltaP `43.7948` edge `0.153` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8731` n `31` status `ready` deltaP `20.1371` edge `0.2072` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3322` n `31` status `ready` deltaP `35.7003` edge `0.0657` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7658` n `31` status `ready` deltaP `12.4058` edge `0.318` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6459` n `31` status `ready` deltaP `31.244` edge `0.0207` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5932` n `45` status `ready` deltaP `31.7649` edge `0.0328` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3649` n `31` status `ready` deltaP `12.4058` edge `0.2562` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
