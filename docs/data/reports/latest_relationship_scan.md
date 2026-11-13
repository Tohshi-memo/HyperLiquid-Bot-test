# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T23:52:23.941924+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10332`

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

- `market_context_high->unknown_24h` score `385.3265` n `75` status `ready` deltaP `2.1944` edge `32.11` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `35.193` n `53` status `ready` deltaP `34.3619` edge `2.7743` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.9593` n `75` status `ready` deltaP `28.9027` edge `2.2081` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.887` n `75` status `ready` deltaP `47.5834` edge `1.3415` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.8046` n `53` status `ready` deltaP `42.0434` edge `1.8143` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9768` n `53` status `ready` deltaP `34.8682` edge `0.7953` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.069` n `53` status `ready` deltaP `39.7569` edge `0.2407` maxDD `0.0`
- `market_context_high->index_24h` score `5.2727` n `75` status `ready` deltaP `29.5556` edge `0.2515` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0259` n `53` status `ready` deltaP `47.7681` edge `0.138` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.5917` n `53` status `ready` deltaP `27.5681` edge `0.2292` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1239` n `75` status `ready` deltaP `41.3334` edge `0.3423` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5421` n `53` status `ready` deltaP `18.464` edge `0.2351` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.46` n `53` status `ready` deltaP `20.7433` edge `0.2988` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1941` n `53` status `ready` deltaP `28.998` edge `0.0982` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.302` n `53` status `ready` deltaP `26.9376` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9142` n `53` status `ready` deltaP `19.2217` edge `0.075` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8291` n `53` status `ready` deltaP `25.5838` edge `0.2278` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7707` n `53` status `ready` deltaP `14.4261` edge `0.5814` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1604` n `53` status `ready` deltaP `15.8287` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6416` n `53` status `ready` deltaP `16.9952` edge `0.0669` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
