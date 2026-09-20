# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T08:07:27.769254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9292`

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

- `news_risk_high->crypto_major_24h` score `41.2919` n `81` status `ready` deltaP `17.9784` edge `3.4879` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.3694` n `81` status `ready` deltaP `28.6844` edge `3.0608` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `6.825` n `70` status `ready` deltaP `35.0199` edge `0.3878` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.223` n `98` status `ready` deltaP `23.4476` edge `0.4832` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.064` n `81` status `ready` deltaP `33.2755` edge `0.2971` maxDD `-0.4217`
- `market_context_high->unknown_4h` score `5.4503` n `73` status `ready` deltaP `2.2928` edge `0.4539` maxDD `-0.5326`
- `news_risk_high->crypto_major_4h` score `4.7374` n `98` status `ready` deltaP `22.9902` edge `0.3673` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1688` n `73` status `ready` deltaP `36.6041` edge `0.1167` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.19` n `100` status `ready` deltaP `17.4132` edge `0.1963` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4189` n `100` status `ready` deltaP `19.509` edge `0.1238` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3334` n `73` status `ready` deltaP `30.659` edge `0.0074` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `2.0535` n `73` status `ready` deltaP `22.3485` edge `0.039` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.3339` n `81` status `ready` deltaP `21.1613` edge `0.0545` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.1515` n `70` status `ready` deltaP `15.7589` edge `-0.0049` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.8941` n `73` status `ready` deltaP `14.3241` edge `0.0048` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.8406` n `98` status `ready` deltaP `19.4344` edge `0.0459` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6782` n `100` status `ready` deltaP `15.1497` edge `0.0157` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.3707` n `81` status `ready` deltaP `17.2068` edge `0.0634` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3394` n `100` status `ready` deltaP `6.006` edge `0.0288` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0805` n `98` status `ready` deltaP `5.2327` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
