# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T10:07:39.466662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9175`

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

- `market_context_high->unknown_4h` score `32.8345` n `58` status `ready` deltaP `1.23` edge `2.743` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.1272` n `101` status `ready` deltaP `9.8803` edge `2.4639` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `16.7044` n `101` status `ready` deltaP `10.2654` edge `1.8117` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.8561` n `101` status `ready` deltaP `17.5471` edge `0.3253` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.5243` n `101` status `ready` deltaP `20.291` edge `0.2842` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5267` n `101` status `ready` deltaP `15.4829` edge `0.1539` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8949` n `101` status `ready` deltaP `17.429` edge `0.094` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2018` n `101` status `ready` deltaP `23.544` edge `0.1277` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8163` n `58` status `ready` deltaP `6.1584` edge `0.0523` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6825` n `58` status `ready` deltaP `10.2777` edge `0.0139` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5466` n `101` status `ready` deltaP `13.9992` edge `0.0124` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3714` n `58` status `ready` deltaP `9.075` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3379` n `101` status `ready` deltaP `10.0126` edge `0.025` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.3139` n `101` status `ready` deltaP `14.9646` edge `0.0318` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2885` n `58` status `ready` deltaP `14.1716` edge `0.0062` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2686` n `58` status `ready` deltaP `5.5493` edge `0.0162` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1777` n `101` status `ready` deltaP `3.4416` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2586` n `101` status `ready` deltaP `1.7712` edge `0.0072` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.39` n `58` status `ready` deltaP `-2.39` edge `0.0553` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.4163` n `58` status `ready` deltaP `1.8187` edge `-0.0031` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
