# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T00:08:02.100042+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8828`

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

- `news_risk_high->crypto_major_24h` score `50.9238` n `72` status `ready` deltaP `26.7361` edge `4.1546` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.2102` n `72` status `ready` deltaP `32.6389` edge `3.6045` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `17.6752` n `102` status `ready` deltaP `-5.6462` edge `1.5339` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.4484` n `72` status `ready` deltaP `36.8055` edge `0.4629` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9381` n `102` status `ready` deltaP `39.1544` edge `0.453` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.9712` n `98` status `ready` deltaP `22.6854` edge `0.4673` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6476` n `98` status `ready` deltaP `23.1427` edge `0.3588` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.6788` n `102` status `ready` deltaP `33.7039` edge `0.0952` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2305` n `98` status `ready` deltaP `18.3246` edge `0.1936` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4427` n `98` status `ready` deltaP `20.121` edge `0.1217` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.764` n `104` status `ready` deltaP `21.1942` edge `0.0309` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6858` n `72` status `ready` deltaP `22.3958` edge `0.0756` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1369` n `102` status `ready` deltaP `20.9619` edge `0.0018` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7833` n `98` status `ready` deltaP `18.6722` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6943` n `98` status `ready` deltaP `15.3061` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.6521` n `72` status `ready` deltaP `4.6875` edge `0.0413` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.5425` n `102` status `ready` deltaP `10.6515` edge `-0.0216` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4426` n `98` status `ready` deltaP `6.9657` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3867` n `104` status `ready` deltaP `8.3717` edge `0.0022` maxDD `-0.063`
- `news_risk_high->fx_4h` score `-0.1171` n `98` status `ready` deltaP `4.7754` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
