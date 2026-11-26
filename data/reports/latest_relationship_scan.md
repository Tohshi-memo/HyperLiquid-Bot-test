# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T05:22:36.617807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3971`

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

- `market_context_high->unknown_1h` score `15370.098` n `32` status `ready` deltaP `1.8338` edge `1280.8387` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3196.4837` n `31` status `ready` deltaP `3.3291` edge `266.3571` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `2455.8253` n `31` status `ready` deltaP `1.6322` edge `204.6588` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `41.9196` n `31` status `ready` deltaP `48.0903` edge `3.1727` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.6455` n `31` status `ready` deltaP `48.9583` edge `2.9774` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.1359` n `31` status `ready` deltaP `48.2639` edge `2.5229` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7571` n `31` status `ready` deltaP `26.3031` edge `0.8081` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2783` n `31` status `ready` deltaP `37.3771` edge `0.6554` maxDD `-2.178`
- `news_risk_high->metal_24h` score `10.2125` n `31` status `ready` deltaP `34.6383` edge `0.6476` maxDD `-0.1986`
- `news_risk_high->index_24h` score `6.8659` n `31` status `ready` deltaP `49.4792` edge `0.2423` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7757` n `31` status `ready` deltaP `17.2354` edge `0.8955` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3643` n `31` status `ready` deltaP `45.8782` edge `0.154` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5779` n `31` status `ready` deltaP `19.688` edge `0.1856` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3534` n `31` status `ready` deltaP `36.31` edge `0.0634` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6447` n `31` status `ready` deltaP `31.3937` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4322` n `31` status `ready` deltaP `9.7112` edge `0.2932` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2245` n `31` status `ready` deltaP `12.5555` edge `0.2372` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1434` n `32` status `ready` deltaP `27.0579` edge `0.0267` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5001` n `31` status `ready` deltaP `29.433` edge `0.024` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1149` n `31` status `ready` deltaP `16.9305` edge `0.0858` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
