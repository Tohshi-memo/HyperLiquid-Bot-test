# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T01:35:11.170164+00:00`
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

- `news_risk_high->crypto_major_24h` score `47.69` n `75` status `ready` deltaP `22.9584` edge `3.9103` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `42.0491` n `75` status `ready` deltaP `31.875` edge `3.4295` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `19.626` n `98` status `ready` deltaP `-6.2064` edge `1.7002` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.8377` n `96` status `ready` deltaP `38.8889` edge `0.4464` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.8328` n `75` status `ready` deltaP `36.3403` edge `0.4147` maxDD `-0.0053`
- `news_risk_high->crypto_alt_4h` score `5.9786` n `98` status `ready` deltaP `22.8378` edge `0.4669` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6778` n `98` status `ready` deltaP `23.2951` edge `0.3603` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8265` n `98` status `ready` deltaP `34.7997` edge `0.1002` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2688` n `98` status `ready` deltaP `18.624` edge `0.1948` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4954` n `98` status `ready` deltaP `20.5701` edge `0.1231` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.7863` n `99` status `ready` deltaP `20.7434` edge `0.0316` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6407` n `75` status `ready` deltaP `22.7014` edge `0.0698` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.0956` n `98` status `ready` deltaP `20.3864` edge `0.0022` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8077` n `98` status `ready` deltaP `18.9771` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7183` n `98` status `ready` deltaP `15.6055` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.6497` n `96` status `ready` deltaP `11.6319` edge `-0.0192` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.415` n `98` status `ready` deltaP `6.6663` edge `0.0307` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3803` n `99` status `ready` deltaP `8.2472` edge `0.0025` maxDD `-0.063`
- `news_risk_high->fx_24h` score `0.1883` n `75` status `ready` deltaP `2.0069` edge `0.0349` maxDD `-0.2736`
- `news_risk_high->commodity_24h` score `0.0094` n `75` status `ready` deltaP `14.6389` edge `0.0342` maxDD `-3.4467`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
