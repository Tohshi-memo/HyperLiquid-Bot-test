# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T06:52:33.032516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `news_risk_high->crypto_major_24h` score `41.0004` n `81` status `ready` deltaP `17.1103` edge `3.4694` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.367` n `81` status `ready` deltaP `28.6844` edge `3.0606` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.0224` n `75` status `ready` deltaP `35.9723` edge `0.3979` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2782` n `98` status `ready` deltaP `23.4476` edge `0.4878` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.1756` n `81` status `ready` deltaP `33.2755` edge `0.3064` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.8552` n `98` status `ready` deltaP `23.1427` edge `0.3761` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9283` n `78` status `ready` deltaP `34.6779` edge `0.1095` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.414` n `98` status `ready` deltaP `18.9234` edge `0.2049` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6261` n `98` status `ready` deltaP `21.1689` edge `0.13` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.365` n `78` status `ready` deltaP `31.1444` edge `0.0068` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.8006` n `78` status `ready` deltaP `20.2326` edge `0.0362` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4086` n `81` status `ready` deltaP `21.8557` edge `0.0561` maxDD `-2.4203`
- `market_context_high->unknown_4h` score `1.247` n `78` status `ready` deltaP `1.4267` edge `0.1094` maxDD `-0.5326`
- `market_context_high->fx_24h` score `1.0525` n `75` status `ready` deltaP `14.9861` edge `-0.008` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.8954` n `98` status `ready` deltaP `20.0441` edge `0.0464` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.7577` n `78` status `ready` deltaP `12.7092` edge `0.0042` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.7315` n `98` status `ready` deltaP `15.7552` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.3489` n `81` status `ready` deltaP `17.2068` edge `0.0606` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3432` n `98` status `ready` deltaP `5.7681` edge `0.0307` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.1049` n `98` status `ready` deltaP `4.9278` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
