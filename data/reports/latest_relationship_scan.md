# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T21:37:29.033370+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3336`

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

- `news_risk_high->unknown_1h` score `3218.2392` n `31` status `ready` deltaP `2.0813` edge `268.1903` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3193.8102` n `31` status `ready` deltaP `4.3962` edge `266.1272` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `28.4743` n `31` status `ready` deltaP `37.6736` edge `2.1217` maxDD `0.0`
- `news_risk_high->equity_24h` score `25.6772` n `31` status `ready` deltaP `36.8056` edge `1.8944` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.3347` n `31` status `ready` deltaP `36.9792` edge `1.6147` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.9735` n `31` status `ready` deltaP `24.4738` edge `0.755` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6601` n `31` status `ready` deltaP `36.0051` edge `0.5297` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.5269` n `31` status `ready` deltaP `23.3535` edge `0.4157` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.4273` n `31` status `ready` deltaP `17.5403` edge `0.8488` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9501` n `31` status `ready` deltaP `41.8851` edge `0.1461` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.54` n `31` status `ready` deltaP `38.1944` edge `0.1237` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2025` n `31` status `ready` deltaP `18.7898` edge `0.1603` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0629` n `31` status `ready` deltaP `34.3283` edge `0.0524` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.562` n `31` status `ready` deltaP `30.6452` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2242` n `31` status `ready` deltaP `7.6154` edge `0.2805` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0243` n `31` status `ready` deltaP `10.7591` edge `0.2235` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3545` n `31` status `ready` deltaP `27.3372` edge `0.0193` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.7731` n `31` status `ready` deltaP `13.8818` edge `0.0623` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2803` n `31` status `ready` deltaP `10.3511` edge `0.0067` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4047` n `31` status `ready` deltaP `-2.2117` edge `0.0072` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
