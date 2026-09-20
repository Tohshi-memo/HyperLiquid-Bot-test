# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T03:07:29.272581+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9116`

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

- `news_risk_high->crypto_major_24h` score `40.3742` n `81` status `ready` deltaP `16.2423` edge `3.423` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4675` n `81` status `ready` deltaP `29.2052` edge `3.0655` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `26.3713` n `92` status `ready` deltaP `-3.4001` edge `2.2436` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.6333` n `90` status `ready` deltaP `38.1945` edge `0.434` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.538` n `81` status `ready` deltaP `33.2755` edge `0.3366` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.0114` n `98` status `ready` deltaP `23.1427` edge `0.4676` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.716` n `98` status `ready` deltaP `23.1427` edge `0.3645` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9207` n `92` status `ready` deltaP `35.737` edge `0.1018` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.3444` n `98` status `ready` deltaP `18.7737` edge `0.2001` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6057` n `98` status `ready` deltaP `21.1689` edge `0.1283` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.9733` n `93` status `ready` deltaP `22.7513` edge `0.0338` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4875` n `81` status `ready` deltaP `22.3765` edge `0.0592` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1998` n `92` status `ready` deltaP `21.5536` edge `0.0031` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8576` n `98` status `ready` deltaP `19.5868` edge `0.0463` maxDD `-2.0994`
- `market_context_high->fx_24h` score `0.7563` n `90` status `ready` deltaP `12.6042` edge `-0.0168` maxDD `-0.0027`
- `news_risk_high->metal_1h` score `0.7315` n `98` status `ready` deltaP `15.7552` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.3839` n `98` status `ready` deltaP `6.2172` edge `0.0311` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3791` n `93` status `ready` deltaP `8.2014` edge `0.0027` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `0.2576` n `81` status `ready` deltaP `17.2068` edge `0.0489` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0549` n `98` status `ready` deltaP `5.5376` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
