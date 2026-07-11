# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T06:22:26.081837+00:00`
- Price records: `672`
- Market context records: `6363`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11106`

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

- `news_risk_high->crypto_alt_24h` score `14.7657` n `32` status `ready` deltaP `40.2778` edge `0.9767` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3052` n `32` status `ready` deltaP `52.4306` edge `0.1759` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4405` n `32` status `ready` deltaP `17.7083` edge `0.5292` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0766` n `32` status `ready` deltaP `42.3018` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9162` n `32` status `ready` deltaP `33.8542` edge `0.1212` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3248` n `32` status `ready` deltaP `27.994` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5427` n `32` status `ready` deltaP `15.0262` edge `0.1443` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9377` n `32` status `ready` deltaP `11.7702` edge `0.0879` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5135` n `208` status `ready` deltaP `15.4784` edge `0.0423` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1578` n `219` status `ready` deltaP `-6.8602` edge `0.1597` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1168` n `208` status `ready` deltaP `8.2903` edge `0.0221` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.4214` n `219` status `ready` deltaP `3.1704` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.4576` n `129` status `ready` deltaP `-3.234` edge `0.1493` maxDD `-6.2457`
- `news_risk_high->unknown_1h` score `-0.4887` n `32` status `ready` deltaP `5.4828` edge `-0.0428` maxDD `-0.7581`
- `market_context_high->index_1h` score `-0.6042` n `219` status `ready` deltaP `-1.2762` edge `0.003` maxDD `-0.7564`
- `market_context_high->metal_24h` score `-0.6156` n `129` status `ready` deltaP `15.2576` edge `0.0762` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.6931` n `219` status `ready` deltaP `-0.4307` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7073` n `32` status `ready` deltaP `0.5208` edge `-0.007` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7411` n `32` status `ready` deltaP `-2.994` edge `-0.0253` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.9625` n `219` status `ready` deltaP `5.3632` edge `0.0161` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
