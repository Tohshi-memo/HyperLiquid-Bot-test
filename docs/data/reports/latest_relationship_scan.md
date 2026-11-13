# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T01:22:31.303055+00:00`
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

- `market_context_high->unknown_24h` score `299.3881` n `84` status `ready` deltaP `6.2996` edge `24.9211` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `62.6474` n `94` status `ready` deltaP `7.8004` edge `5.2134` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.4679` n `53` status `ready` deltaP `26.0286` edge `2.4361` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.4505` n `84` status `ready` deltaP `23.7599` edge `1.7831` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.1348` n `53` status `ready` deltaP `38.7448` edge `1.494` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4621` n `53` status `ready` deltaP `32.7341` edge `0.6833` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.2376` n `84` status `ready` deltaP `44.5189` edge `1.2971` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.1003` n `53` status `ready` deltaP `43.2292` edge `0.3035` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5946` n `84` status `ready` deltaP `40.253` edge `0.3225` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5366` n `53` status `ready` deltaP `43.3474` edge `0.1267` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3394` n `84` status `ready` deltaP `24.6776` edge `0.2066` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9311` n `53` status `ready` deltaP `22.8806` edge `0.2054` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0461` n `53` status `ready` deltaP `27.7784` edge `0.094` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.9868` n `53` status `ready` deltaP `16.8173` edge `0.1998` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6459` n `53` status `ready` deltaP `19.3713` edge `0.2401` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1379` n `53` status `ready` deltaP `25.2909` edge `0.035` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.8` n `53` status `ready` deltaP `14.5997` edge `0.584` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6883` n `53` status `ready` deltaP `18.0022` edge `0.0643` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4039` n `53` status `ready` deltaP `24.5168` edge `0.1804` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.092` n `53` status `ready` deltaP `15.5293` edge `0.0176` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
