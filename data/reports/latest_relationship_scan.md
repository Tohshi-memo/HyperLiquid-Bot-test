# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T01:07:24.838504+00:00`
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

- `market_context_high->unknown_24h` score `300.2821` n `84` status `ready` deltaP `6.2996` edge `24.9956` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `62.8996` n `94` status `ready` deltaP `7.9528` edge `5.2334` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.4439` n `53` status `ready` deltaP `26.0286` edge `2.4341` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.4265` n `84` status `ready` deltaP `23.7599` edge `1.7811` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.12` n `53` status `ready` deltaP `38.7448` edge `1.4921` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4741` n `53` status `ready` deltaP `32.7341` edge `0.6843` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.2114` n `84` status `ready` deltaP `44.3453` edge `1.2949` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.1171` n `53` status `ready` deltaP `43.2292` edge `0.3049` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5862` n `84` status `ready` deltaP `40.253` edge `0.3218` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5596` n `53` status `ready` deltaP `43.4998` edge `0.1276` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3394` n `84` status `ready` deltaP `24.6776` edge `0.2066` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9311` n `53` status `ready` deltaP `22.8806` edge `0.2054` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0267` n `53` status `ready` deltaP `27.626` edge `0.0934` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.9916` n `53` status `ready` deltaP `16.8173` edge `0.2002` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6555` n `53` status `ready` deltaP `19.3713` edge `0.2409` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1547` n `53` status `ready` deltaP `25.4406` edge `0.0354` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.7738` n `53` status `ready` deltaP `14.4261` edge `0.5818` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6895` n `53` status `ready` deltaP `18.0022` edge `0.0644` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4023` n `53` status `ready` deltaP `24.5168` edge `0.1802` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1064` n `53` status `ready` deltaP `15.679` edge `0.0178` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
