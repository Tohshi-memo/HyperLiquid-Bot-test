# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T13:22:29.034203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3233.9172` n `31` status `ready` deltaP `1.9316` edge `269.4978` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3219.0163` n `31` status `ready` deltaP `3.4815` edge `268.2338` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `103.6254` n `31` status `ready` deltaP `1.9316` edge `8.632` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `34.9494` n `31` status `ready` deltaP `43.4028` edge `2.6231` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.3124` n `31` status `ready` deltaP `42.5347` edge `2.5758` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.0235` n `31` status `ready` deltaP `42.7083` edge `2.1339` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.6363` n `31` status `ready` deltaP `26.6079` edge `0.796` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4168` n `31` status `ready` deltaP `38.749` edge `0.6578` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.3484` n `31` status `ready` deltaP `29.0827` edge `0.5293` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9149` n `31` status `ready` deltaP `19.522` edge `0.8981` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7543` n `31` status `ready` deltaP `43.9236` edge `0.1867` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.9518` n `31` status `ready` deltaP `41.7115` edge `0.1474` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7207` n `31` status `ready` deltaP `20.1371` edge `0.1945` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4412` n `31` status `ready` deltaP `37.3771` edge `0.0636` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7345` n `31` status `ready` deltaP `32.2919` edge `0.0211` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5024` n `31` status `ready` deltaP `10.0106` edge `0.3002` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2806` n `31` status `ready` deltaP `13.1543` edge `0.2404` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9326` n `31` status `ready` deltaP `24.8279` edge `0.024` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4604` n `31` status `ready` deltaP `28.6845` edge `0.0239` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9944` n `31` status `ready` deltaP `15.5586` edge `0.0795` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
