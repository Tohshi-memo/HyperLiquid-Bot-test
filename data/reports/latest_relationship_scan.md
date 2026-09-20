# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T06:07:52.324882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_major_24h` score `40.8972` n `81` status `ready` deltaP `17.1103` edge `3.4608` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4289` n `81` status `ready` deltaP `28.858` edge `3.0646` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.1306` n `78` status `ready` deltaP `36.4851` edge `0.4035` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2794` n `98` status `ready` deltaP `23.4476` edge `0.4879` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.2548` n `81` status `ready` deltaP `33.2755` edge `0.313` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.8924` n `98` status `ready` deltaP `23.1427` edge `0.3792` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.827` n `81` status `ready` deltaP `33.9657` edge `0.1058` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4271` n `98` status `ready` deltaP `19.0731` edge `0.205` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6645` n `98` status `ready` deltaP `21.4683` edge `0.1312` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3542` n `81` status `ready` deltaP `31.1145` edge `0.0061` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.784` n `81` status `ready` deltaP `20.1449` edge `0.0354` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4599` n `81` status `ready` deltaP `22.3765` edge `0.0569` maxDD `-2.4203`
- `market_context_high->fx_24h` score `0.9897` n `78` status `ready` deltaP `14.5165` edge `-0.0101` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.8978` n `98` status `ready` deltaP `20.0441` edge `0.0466` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7566` n `98` status `ready` deltaP `16.0546` edge `0.0162` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.5755` n `81` status `ready` deltaP `10.492` edge `0.0038` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3528` n `98` status `ready` deltaP `5.7681` edge `0.0315` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.3341` n `81` status `ready` deltaP `17.2068` edge `0.0587` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.1427` n `98` status `ready` deltaP `4.4705` edge `0.0219` maxDD `-0.421`
- `news_risk_high->index_1h` score `-0.435` n `98` status `ready` deltaP `-0.1222` edge `0.0016` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
