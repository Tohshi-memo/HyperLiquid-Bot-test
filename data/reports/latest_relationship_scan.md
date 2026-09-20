# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T15:22:30.437644+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9386`

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

- `news_risk_high->crypto_major_24h` score `22.5372` n `98` status `ready` deltaP `8.4503` edge `2.5076` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.1997` n `98` status `ready` deltaP `14.7463` edge `2.0731` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `10.1335` n `53` status `ready` deltaP `0.742` edge `0.8545` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9813` n `101` status `ready` deltaP `23.1873` edge `0.4648` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5224` n `101` status `ready` deltaP `21.9678` edge `0.3562` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3823` n `53` status `ready` deltaP `37.3072` edge `0.1298` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `4.3051` n `42` status `ready` deltaP `25.4961` edge `0.2413` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `3.0545` n `101` status `ready` deltaP `16.6805` edge `0.1899` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2475` n `101` status `ready` deltaP `18.4769` edge `0.1164` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.9288` n `53` status `ready` deltaP `25.4919` edge `0.0123` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.7925` n `42` status `ready` deltaP `19.8412` edge `0.0213` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.4005` n `53` status `ready` deltaP `15.8287` edge `0.0387` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0729` n `98` status `ready` deltaP `22.775` edge `0.1163` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7911` n `53` status `ready` deltaP `11.5467` edge `0.0064` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.7286` n `101` status `ready` deltaP `18.3183` edge `0.044` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.6149` n `98` status `ready` deltaP `16.571` edge `0.0817` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3769` n `53` status `ready` deltaP `9.4792` edge `0.0075` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2336` n `98` status `ready` deltaP `15.5046` edge `0.011` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2221` n `101` status `ready` deltaP `5.2143` edge `0.0243` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
