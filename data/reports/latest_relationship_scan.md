# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T03:52:27.232384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11780`

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

- `market_context_high->unknown_24h` score `289.0237` n `84` status `ready` deltaP `6.2996` edge `24.0574` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.8404` n `94` status `ready` deltaP `7.3431` edge `4.6492` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.0712` n `53` status `ready` deltaP `27.7647` edge `2.4748` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.0538` n `84` status `ready` deltaP `25.496` edge `1.8218` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.5186` n `53` status `ready` deltaP `39.092` edge `1.5409` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.6703` n `84` status `ready` deltaP `46.255` edge `1.341` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.4477` n `53` status `ready` deltaP `32.7341` edge `0.6821` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.8358` n `53` status `ready` deltaP `42.1875` edge `0.2884` maxDD `0.0`
- `market_context_high->metal_24h` score `6.8144` n `84` status `ready` deltaP `41.8155` edge `0.3304` maxDD `-0.3044`
- `market_context_high->index_24h` score `4.3972` n `84` status `ready` deltaP `25.0248` edge `0.2091` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.3235` n `53` status `ready` deltaP `41.823` edge `0.1191` maxDD `-1.0104`
- `news_risk_high->index_24h` score `3.9888` n `53` status `ready` deltaP `23.2278` edge `0.2079` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2125` n `53` status `ready` deltaP `29.3028` edge `0.0977` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1499` n `53` status `ready` deltaP `17.2664` edge `0.2104` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.7299` n `53` status `ready` deltaP `19.3713` edge `0.2471` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.2327` n `53` status `ready` deltaP `16.3358` edge `0.6279` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0384` n `53` status `ready` deltaP `24.3927` edge `0.0327` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6579` n `53` status `ready` deltaP `17.6973` edge `0.0638` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5565` n `53` status `ready` deltaP `25.1265` edge `0.1959` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
