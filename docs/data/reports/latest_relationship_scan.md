# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T02:52:28.515579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `293.5237` n `84` status `ready` deltaP `6.2996` edge `24.4324` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `56.2896` n `94` status `ready` deltaP `7.6479` edge `4.6846` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.8657` n `53` status `ready` deltaP `27.0703` edge `2.4623` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.8483` n `84` status `ready` deltaP `24.8016` edge `1.8093` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.3275` n `53` status `ready` deltaP `39.092` edge `1.5164` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.472` n `84` status `ready` deltaP `45.5605` edge `1.3202` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.4489` n `53` status `ready` deltaP `32.7341` edge `0.6822` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9754` n `53` status `ready` deltaP `42.8819` edge `0.2954` maxDD `0.0`
- `market_context_high->metal_24h` score `6.7228` n `84` status `ready` deltaP `41.121` edge `0.3274` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.4059` n `53` status `ready` deltaP `42.4327` edge `0.1219` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3634` n `84` status `ready` deltaP `24.6776` edge `0.2086` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9551` n `53` status `ready` deltaP `22.8806` edge `0.2074` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.1493` n `53` status `ready` deltaP `28.6931` edge `0.0965` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1379` n `53` status `ready` deltaP `17.2664` edge `0.2094` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6255` n `53` status `ready` deltaP `19.3713` edge `0.2384` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1007` n `53` status `ready` deltaP `24.9915` edge `0.0339` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.0344` n `53` status `ready` deltaP `15.6413` edge `0.6071` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6761` n `53` status `ready` deltaP `17.8497` edge `0.0643` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4596` n `53` status `ready` deltaP `24.9741` edge `0.1845` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
