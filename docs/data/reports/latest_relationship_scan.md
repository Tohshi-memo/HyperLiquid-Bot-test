# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T20:22:27.719103+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `308.9563` n `84` status `ready` deltaP `6.4578` edge `25.7174` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `77.0442` n `94` status `ready` deltaP `8.1053` edge `6.4111` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.8001` n `53` status `ready` deltaP `23.361` edge `2.3149` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.7827` n `84` status `ready` deltaP `21.0923` edge `1.6619` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.5278` n `53` status `ready` deltaP `37.2127` edge `1.4264` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.1575` n `53` status `ready` deltaP `31.9719` edge `0.663` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.3391` n `84` status `ready` deltaP `41.0993` edge `1.2047` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.4051` n `53` status `ready` deltaP `43.1542` edge `0.3294` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2359` n `84` status `ready` deltaP `38.7699` edge `0.3025` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6164` n `53` status `ready` deltaP `43.8047` edge `0.1303` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.0755` n `84` status `ready` deltaP `23.0585` edge `0.1954` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.6671` n `53` status `ready` deltaP `21.2615` edge `0.1942` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1546` n `53` status `ready` deltaP `17.5658` edge `0.2088` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9787` n `53` status `ready` deltaP `26.7114` edge `0.0955` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8646` n `53` status `ready` deltaP `20.5908` edge `0.2502` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2445` n `53` status `ready` deltaP `26.3388` edge `0.0369` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6143` n `53` status `ready` deltaP `17.3924` edge `0.0622` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5294` n `53` status `ready` deltaP `25.4314` edge `0.1904` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2238` n `53` status `ready` deltaP `16.8766` edge `0.0196` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.9015` n `53` status `ready` deltaP `11.1801` edge `0.4916` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
