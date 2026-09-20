# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T07:22:25.428876+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9238`

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

- `news_risk_high->crypto_major_24h` score `41.117` n `81` status `ready` deltaP `17.4575` edge `3.4768` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.3658` n `81` status `ready` deltaP `28.6844` edge `3.0605` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `6.9619` n `73` status `ready` deltaP `35.607` edge `0.3953` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2554` n `98` status `ready` deltaP `23.4476` edge `0.4859` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.13` n `81` status `ready` deltaP `33.2755` edge `0.3026` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.812` n `98` status `ready` deltaP `23.1427` edge `0.3725` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1488` n `76` status `ready` deltaP `36.9384` edge `0.1128` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4176` n `98` status `ready` deltaP `18.9234` edge `0.2052` maxDD `-2.058`
- `market_context_high->unknown_4h` score `3.1017` n `76` status `ready` deltaP `2.455` edge `0.2571` maxDD `-0.5326`
- `news_risk_high->crypto_major_1h` score `2.6033` n `98` status `ready` deltaP `21.0192` edge `0.1291` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3687` n `76` status `ready` deltaP `31.1457` edge `0.0071` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.8768` n `76` status `ready` deltaP `20.9896` edge `0.0375` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.3736` n `81` status `ready` deltaP `21.5085` edge `0.0555` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.0977` n `73` status `ready` deltaP `15.2968` edge `-0.0063` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.8924` n `76` status `ready` deltaP `14.3476` edge `0.0045` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.8686` n `98` status `ready` deltaP `19.7393` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7195` n `98` status `ready` deltaP `15.6055` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.3567` n `81` status `ready` deltaP `17.2068` edge `0.0616` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3252` n `98` status `ready` deltaP `5.6184` edge `0.0302` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0805` n `98` status `ready` deltaP `5.2327` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
