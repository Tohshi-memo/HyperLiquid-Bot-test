# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T03:07:25.718388+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3218.0568` n `31` status `ready` deltaP `1.9316` edge `268.1761` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3189.0868` n `31` status `ready` deltaP `4.2437` edge `265.7346` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.347` n `31` status `ready` deltaP `34.0278` edge `1.8854` maxDD `0.0`
- `news_risk_high->equity_24h` score `22.5082` n `31` status `ready` deltaP `33.5069` edge `1.6523` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3844` n `31` status `ready` deltaP `33.1597` edge `1.3943` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3942` n `31` status `ready` deltaP `23.7116` edge `0.7118` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.9146` n `31` status `ready` deltaP `33.871` edge `0.4818` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.1756` n `31` status `ready` deltaP `16.9305` edge `0.8206` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.0307` n `31` status `ready` deltaP `21.0966` edge `0.3894` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8813` n `31` status `ready` deltaP `41.1907` edge `0.145` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.9756` n `31` status `ready` deltaP `35.0694` edge `0.0975` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.8943` n `31` status `ready` deltaP `17.5922` edge `0.1426` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.8042` n `31` status `ready` deltaP `31.8893` edge `0.0471` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4793` n `31` status `ready` deltaP `29.8967` edge `0.0158` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1322` n `31` status `ready` deltaP `7.1663` edge `0.2717` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8909` n `31` status `ready` deltaP `10.1603` edge `0.2104` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2103` n `31` status `ready` deltaP `25.9899` edge `0.0098` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5294` n `31` status `ready` deltaP `12.5098` edge `0.0402` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1255` n `31` status `ready` deltaP `8.0645` edge `0.0021` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5545` n `31` status `ready` deltaP `-3.8584` edge `0.0057` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
