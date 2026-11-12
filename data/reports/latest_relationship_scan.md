# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T19:52:43.734115+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `308.0131` n `84` status `ready` deltaP `6.4425` edge `25.6389` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `79.263` n `94` status `ready` deltaP `8.1053` edge `6.596` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.6636` n `53` status `ready` deltaP `23.1247` edge `2.3051` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.6462` n `84` status `ready` deltaP `20.856` edge `1.6521` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.481` n `53` status `ready` deltaP `37.243` edge `1.4202` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.1635` n `53` status `ready` deltaP `31.9719` edge `0.6635` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.2349` n `84` status `ready` deltaP `40.8058` edge `1.1933` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.41` n `53` status `ready` deltaP `43.0796` edge `0.3303` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2315` n `84` status `ready` deltaP `38.8491` edge `0.3016` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.648` n `53` status `ready` deltaP `44.1096` edge `0.1309` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.0475` n `84` status `ready` deltaP `22.8291` edge `0.1946` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.6392` n `53` status `ready` deltaP `21.0321` edge `0.1934` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1079` n `53` status `ready` deltaP `17.2664` edge `0.2069` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9955` n `53` status `ready` deltaP `26.7114` edge `0.0969` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.885` n `53` status `ready` deltaP `20.5908` edge `0.2519` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2445` n `53` status `ready` deltaP `26.3388` edge `0.0369` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6203` n `53` status `ready` deltaP `17.3924` edge `0.0627` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5513` n `53` status `ready` deltaP `25.4314` edge `0.1932` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2106` n `53` status `ready` deltaP `16.7269` edge `0.0195` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.7973` n `53` status `ready` deltaP `10.8866` edge `0.4802` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
