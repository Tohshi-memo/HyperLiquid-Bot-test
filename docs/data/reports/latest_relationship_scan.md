# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T21:35:23.102855+00:00`
- Price records: `672`
- Market context records: `6126`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.264` n `30` status `ready` deltaP `38.4722` edge `0.6136` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8566` n `30` status `ready` deltaP `69.6181` edge `0.1906` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3323` n `32` status `ready` deltaP `45.1982` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3919` n `32` status `ready` deltaP `28.7425` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.3212` n `32` status `ready` deltaP `14.128` edge `0.1219` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7227` n `32` status `ready` deltaP `9.2253` edge `0.0773` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.5603` n `195` status `ready` deltaP `4.8171` edge `0.1063` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.0761` n `30` status `ready` deltaP `8.7152` edge `0.0193` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2754` n `195` status `ready` deltaP `1.4348` edge `-0.0003` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5371` n `30` status `ready` deltaP `14.0973` edge `-0.1182` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.7043` n `195` status `ready` deltaP `2.9323` edge `0.0089` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.7502` n `195` status `ready` deltaP `0.0399` edge `0.0151` maxDD `-4.2573`
- `market_context_high->commodity_1h` score `-0.7763` n `195` status `ready` deltaP `-2.2885` edge `-0.0048` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7777` n `32` status `ready` deltaP `-2.994` edge `-0.03` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8308` n `195` status `ready` deltaP `2.3906` edge `-0.0053` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8533` n `195` status `ready` deltaP `4.2093` edge `0.0378` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8767` n `195` status `ready` deltaP `4.9133` edge `0.0316` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.0123` n `195` status `ready` deltaP `0.0219` edge `0.0165` maxDD `-1.381`
- `news_risk_high->crypto_major_24h` score `-1.0551` n `30` status `ready` deltaP `8.8194` edge `-0.1161` maxDD `-4.2368`
- `market_context_high->metal_24h` score `-1.1342` n `195` status `ready` deltaP `14.3002` edge `0.0161` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
