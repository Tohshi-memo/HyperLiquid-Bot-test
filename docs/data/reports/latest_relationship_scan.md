# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T08:22:26.052686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10464`

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

- `market_context_high->unknown_24h` score `455.8949` n `75` status `ready` deltaP `2.1944` edge `37.9907` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.5509` n `53` status `ready` deltaP `36.4453` edge `2.9569` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.3172` n `75` status `ready` deltaP `30.9861` edge `2.3907` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.695` n `75` status `ready` deltaP `47.5834` edge `1.3255` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.6642` n `53` status `ready` deltaP `42.0434` edge `1.9245` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3166` n `53` status `ready` deltaP `36.8499` edge `0.8104` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.6627` n `53` status `ready` deltaP `45.1389` edge `0.2543` maxDD `0.0`
- `market_context_high->index_24h` score `5.9621` n `75` status `ready` deltaP `35.4584` edge `0.2696` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.2811` n `53` status `ready` deltaP `33.4709` edge `0.2473` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0245` n `53` status `ready` deltaP `47.6157` edge `0.1389` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3384` n `75` status `ready` deltaP `41.3334` edge `0.3698` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.1728` n `53` status `ready` deltaP `21.6579` edge `0.3521` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5697` n `53` status `ready` deltaP `18.6137` edge `0.2364` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1225` n `53` status `ready` deltaP `28.3882` edge `0.0963` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2326` n `53` status `ready` deltaP `26.0394` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.2065` n `53` status `ready` deltaP `22.5754` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0925` n `53` status `ready` deltaP `26.1936` edge `0.2575` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6459` n `53` status `ready` deltaP `14.4261` edge `0.5654` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2622` n `53` status `ready` deltaP `17.0263` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7702` n `53` status `ready` deltaP `17.8934` edge `0.0774` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
