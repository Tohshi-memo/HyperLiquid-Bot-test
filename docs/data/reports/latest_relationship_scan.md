# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T02:52:28.172257+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `377.4708` n `83` status `ready` deltaP `-20.9007` edge `31.6847` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.6143` n `83` status `ready` deltaP `38.5249` edge `1.2656` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.2069` n `83` status `ready` deltaP `30.5911` edge `1.2628` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.4022` n `83` status `ready` deltaP `39.8239` edge `0.8621` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.6588` n `52` status `ready` deltaP `43.0556` edge `0.3512` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.6588` n `52` status `ready` deltaP `43.0556` edge `0.3512` maxDD `0.0`
- `news_risk_high->index_24h` score `6.5159` n `83` status `ready` deltaP `45.2539` edge `0.2589` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.3597` n `149` status `ready` deltaP `36.3442` edge `0.3402` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.7046` n `83` status `ready` deltaP `31.9905` edge `0.2242` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5572` n `52` status `ready` deltaP `33.32` edge `-0.0048` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5572` n `52` status `ready` deltaP `33.32` edge `-0.0048` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4223` n `149` status `ready` deltaP `30.5451` edge `0.0198` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2392` n `52` status `ready` deltaP `28.2716` edge `0.0331` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2392` n `52` status `ready` deltaP `28.2716` edge `0.0331` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.139` n `149` status `ready` deltaP `24.7739` edge `0.0549` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9312` n `149` status `ready` deltaP `14.5642` edge `0.0182` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3651` n `83` status `ready` deltaP `11.736` edge `0.0314` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3079` n `52` status `ready` deltaP `7.6463` edge `0.0099` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3079` n `52` status `ready` deltaP `7.6463` edge `0.0099` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1646` n `52` status `ready` deltaP `6.5638` edge `0.0079` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
