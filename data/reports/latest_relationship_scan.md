# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T18:37:28.892959+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32284.2446` n `45` status `ready` deltaP `1.4171` edge `2690.3537` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22090.4725` n `45` status `ready` deltaP `3.1776` edge `1840.8654` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1049.2897` n `31` status `ready` deltaP `1.6322` edge `87.4475` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `837.525` n `31` status `ready` deltaP `4.3962` edge `69.7701` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.0836` n `31` status `ready` deltaP `50.0` edge `2.8403` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.1652` n `31` status `ready` deltaP `42.5347` edge `2.7302` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.4159` n `31` status `ready` deltaP `48.2639` edge `2.4629` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.4151` n `31` status `ready` deltaP `25.6933` edge `0.867` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1002` n `31` status `ready` deltaP `41.2355` edge `0.6776` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.895` n `31` status `ready` deltaP `34.1759` edge `0.6448` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.0859` n `31` status `ready` deltaP `16.9305` edge `0.9373` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.2022` n `31` status `ready` deltaP `52.3018` edge `0.181` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.3822` n `31` status `ready` deltaP `40.2778` edge `0.18` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4485` n `31` status `ready` deltaP `18.4904` edge `0.1828` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0031` n `31` status `ready` deltaP `32.6515` edge `0.0586` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8061` n `45` status `ready` deltaP `34.0515` edge `0.0353` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.5771` n `31` status `ready` deltaP `11.3579` edge `0.3008` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5117` n `31` status `ready` deltaP `29.8967` edge `0.0185` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2161` n `31` status `ready` deltaP `10.9088` edge `0.2471` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6342` n `31` status `ready` deltaP `30.6306` edge `0.0332` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
