# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T04:37:27.578800+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_1h` score `32243.8573` n `45` status `ready` deltaP `2.1656` edge `2686.9831` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21973.8481` n `45` status `ready` deltaP `3.1776` edge `1831.1467` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1008.9023` n `31` status `ready` deltaP `2.3807` edge `84.0769` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `720.9006` n `31` status `ready` deltaP `4.3962` edge `60.0514` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.4344` n `31` status `ready` deltaP `44.4444` edge `2.9899` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.1295` n `31` status `ready` deltaP `50.1736` edge `2.9263` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.5855` n `31` status `ready` deltaP `49.4792` edge `2.6356` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0122` n `31` status `ready` deltaP `28.1323` edge `0.9005` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2358` n `31` status `ready` deltaP `41.2355` edge `0.6889` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.7289` n `31` status `ready` deltaP `36.0051` edge `0.7021` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5477` n `31` status `ready` deltaP `18.9123` edge `0.9833` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9945` n `31` status `ready` deltaP `44.2708` edge `0.2044` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3539` n `31` status `ready` deltaP `45.3573` edge `0.1566` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7292` n `31` status `ready` deltaP `19.2389` edge `0.2012` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2363` n `31` status `ready` deltaP `34.7856` edge `0.0638` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7509` n `31` status `ready` deltaP `12.4058` edge `0.3161` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.604` n `31` status `ready` deltaP `30.7949` edge `0.0202` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.365` n `31` status `ready` deltaP `12.2561` edge `0.2572` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5991` n `31` status `ready` deltaP `30.3312` edge `0.0307` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
