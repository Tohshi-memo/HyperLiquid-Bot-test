# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T04:07:30.198460+00:00`
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

- `market_context_high->unknown_24h` score `287.2033` n `84` status `ready` deltaP `6.2996` edge `23.9057` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.8054` n `94` status `ready` deltaP `7.1906` edge `4.6473` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.1427` n `53` status `ready` deltaP `27.9383` edge `2.4796` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.1253` n `84` status `ready` deltaP `25.6696` edge `1.8266` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.5764` n `53` status `ready` deltaP `39.092` edge `1.5483` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.7223` n `84` status `ready` deltaP `46.4286` edge `1.3465` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.4729` n `53` status `ready` deltaP `32.7341` edge `0.6842` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.8403` n `84` status `ready` deltaP `41.9891` edge `0.3314` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.8003` n `53` status `ready` deltaP `42.0139` edge `0.2866` maxDD `0.0`
- `market_context_high->index_24h` score `4.4147` n `84` status `ready` deltaP `25.1984` edge `0.2094` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.3065` n `53` status `ready` deltaP `41.6705` edge `0.1187` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0063` n `53` status `ready` deltaP `23.4014` edge `0.2082` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2271` n `53` status `ready` deltaP `29.4553` edge `0.0979` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1607` n `53` status `ready` deltaP `17.2664` edge `0.2113` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.7707` n `53` status `ready` deltaP `19.3713` edge `0.2505` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.2846` n `53` status `ready` deltaP `16.5094` edge `0.6334` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.036` n `53` status `ready` deltaP `24.3927` edge `0.0325` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6591` n `53` status `ready` deltaP `17.6973` edge `0.0639` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5822` n `53` status `ready` deltaP `25.1265` edge `0.1992` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1471` n `53` status `ready` deltaP `15.9784` edge `0.0192` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
