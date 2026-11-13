# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T05:37:27.494485+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11860`

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

- `market_context_high->unknown_24h` score `275.7997` n `84` status `ready` deltaP `6.2996` edge `22.9554` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.3896` n `94` status `ready` deltaP `6.7333` edge `4.6157` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.5345` n `53` status `ready` deltaP `28.98` edge `2.5053` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.5171` n `84` status `ready` deltaP `26.7113` edge `1.8523` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.9509` n `53` status `ready` deltaP `39.4392` edge `1.594` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.0479` n `84` status `ready` deltaP `47.4703` edge `1.3813` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.7053` n `53` status `ready` deltaP `33.3438` edge `0.6995` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.0076` n `84` status `ready` deltaP `43.0307` edge `0.3384` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.567` n `53` status `ready` deltaP `40.9722` edge `0.2741` maxDD `0.0`
- `market_context_high->index_24h` score `4.464` n `84` status `ready` deltaP `25.5456` edge `0.2112` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.3235` n `53` status `ready` deltaP `41.823` edge `0.1191` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0557` n `53` status `ready` deltaP `23.7486` edge `0.21` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2211` n `53` status `ready` deltaP `29.4553` edge `0.0974` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.2074` n `53` status `ready` deltaP `17.5658` edge `0.2132` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.0889` n `53` status `ready` deltaP `19.5237` edge `0.276` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.6102` n `53` status `ready` deltaP `17.5511` edge `0.6682` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.042` n `53` status `ready` deltaP `24.3927` edge `0.033` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8231` n `53` status `ready` deltaP `25.8887` edge `0.225` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.7246` n `53` status `ready` deltaP `18.3071` edge `0.0653` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1747` n `53` status `ready` deltaP `16.2778` edge `0.0195` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
