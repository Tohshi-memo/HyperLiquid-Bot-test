# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T23:37:44.673848+00:00`
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

- `market_context_high->unknown_24h` score `383.2313` n `75` status `ready` deltaP `2.1944` edge `31.9354` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `35.1114` n `53` status `ready` deltaP `34.3619` edge `2.7675` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.8777` n `75` status `ready` deltaP `28.9027` edge `2.2013` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.8834` n `75` status `ready` deltaP `47.5834` edge `1.3412` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.7711` n `53` status `ready` deltaP `42.0434` edge `1.81` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9502` n `53` status `ready` deltaP `34.7158` edge `0.7941` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.0467` n `53` status `ready` deltaP `39.5833` edge `0.24` maxDD `0.0`
- `market_context_high->index_24h` score `5.2528` n `75` status `ready` deltaP `29.382` edge `0.251` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0259` n `53` status `ready` deltaP `47.7681` edge `0.138` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.5718` n `53` status `ready` deltaP `27.3945` edge `0.2287` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1192` n `75` status `ready` deltaP `41.3334` edge `0.3417` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5277` n `53` status `ready` deltaP `18.3143` edge `0.2349` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.4166` n `53` status `ready` deltaP `20.5908` edge `0.2962` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.2087` n `53` status `ready` deltaP `29.1504` edge `0.0984` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.302` n `53` status `ready` deltaP `26.9376` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9154` n `53` status `ready` deltaP `19.2217` edge `0.0751` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8063` n `53` status `ready` deltaP `25.4314` edge `0.2259` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7684` n `53` status `ready` deltaP `14.4261` edge `0.5811` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1616` n `53` status `ready` deltaP `15.8287` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6408` n `53` status `ready` deltaP `16.9952` edge `0.0668` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
