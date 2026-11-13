# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T04:51:23.247357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11820`

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

- `market_context_high->unknown_24h` score `281.4937` n `84` status `ready` deltaP `6.2996` edge `23.4299` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.463` n `94` status `ready` deltaP `6.8857` edge `4.6208` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.3488` n `53` status `ready` deltaP `28.4592` edge `2.4933` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.3314` n `84` status `ready` deltaP `26.1905` edge `1.8403` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.7687` n `53` status `ready` deltaP `39.2656` edge `1.5718` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.8874` n `84` status `ready` deltaP `46.9494` edge `1.3642` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.5559` n `53` status `ready` deltaP `32.8865` edge `0.6901` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.9239` n `84` status `ready` deltaP `42.5099` edge `0.3349` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.6794` n `53` status `ready` deltaP `41.4931` edge `0.28` maxDD `0.0`
- `market_context_high->index_24h` score `4.4544` n `84` status `ready` deltaP `25.5456` edge `0.2104` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.2859` n `53` status `ready` deltaP `41.5181` edge `0.118` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0461` n `53` status `ready` deltaP `23.7486` edge `0.2092` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2283` n `53` status `ready` deltaP `29.4553` edge `0.098` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.2038` n `53` status `ready` deltaP `17.5658` edge `0.2129` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.9183` n `53` status `ready` deltaP `19.3713` edge `0.2628` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.4498` n `53` status `ready` deltaP `17.0302` edge `0.6511` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.066` n `53` status `ready` deltaP `24.6921` edge `0.033` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.694` n `53` status `ready` deltaP `25.4314` edge `0.2115` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.6761` n `53` status `ready` deltaP `17.8497` edge `0.0643` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.2778` edge `0.0194` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
