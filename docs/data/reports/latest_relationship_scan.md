# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T23:52:41.829529+00:00`
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

- `market_context_high->unknown_1h` score `32422.0081` n `45` status `ready` deltaP `2.6147` edge `2701.826` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22247.4486` n `45` status `ready` deltaP `3.4824` edge `1853.9447` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1212.4787` n `31` status `ready` deltaP `2.8298` edge `101.0386` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1012.0954` n `31` status `ready` deltaP `4.701` edge `84.3156` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.2544` n `31` status `ready` deltaP `43.75` edge `2.8962` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9289` n `31` status `ready` deltaP `45.4861` edge `2.6075` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9192` n `31` status `ready` deltaP `45.6597` edge `2.2722` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.2948` n `31` status `ready` deltaP `44.7077` edge `0.754` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.465` n `31` status `ready` deltaP `23.1018` edge `0.8051` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6959` n `31` status `ready` deltaP `30.8222` edge `0.5674` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6051` n `31` status `ready` deltaP `56.4684` edge `0.1868` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.3717` n `31` status `ready` deltaP `12.6623` edge `0.8742` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9265` n `31` status `ready` deltaP `41.6667` edge `0.2161` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3085` n `45` status `ready` deltaP `39.3868` edge `0.0416` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1605` n `31` status `ready` deltaP `17.4425` edge `0.1658` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9417` n `31` status `ready` deltaP `32.499` edge `0.0545` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4805` n `31` status `ready` deltaP `29.5973` edge `0.0179` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.45` n `31` status `ready` deltaP `10.6094` edge `0.2895` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0984` n `31` status `ready` deltaP `10.1603` edge `0.237` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5461` n `31` status `ready` deltaP `29.8821` edge `0.0269` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
