# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T20:07:42.767052+00:00`
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

- `market_context_high->unknown_24h` score `308.5987` n `84` status `ready` deltaP `6.4425` edge `25.6877` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `78.2034` n `94` status `ready` deltaP `8.1053` edge `6.5077` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.7819` n `53` status `ready` deltaP `23.2977` edge `2.3138` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.7645` n `84` status `ready` deltaP `21.029` edge `1.6608` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.5208` n `53` status `ready` deltaP `37.243` edge `1.4253` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.1695` n `53` status `ready` deltaP `31.9719` edge `0.664` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.3048` n `84` status `ready` deltaP `40.9788` edge `1.2011` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.3944` n `53` status `ready` deltaP `43.0796` edge `0.329` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2447` n `84` status `ready` deltaP `38.8491` edge `0.3027` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6334` n `53` status `ready` deltaP `43.9571` edge `0.1307` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.0698` n `84` status `ready` deltaP `23.0022` edge `0.1953` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.6614` n `53` status `ready` deltaP `21.2052` edge `0.1941` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1367` n `53` status `ready` deltaP `17.4161` edge `0.2083` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9871` n `53` status `ready` deltaP `26.7114` edge `0.0962` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.879` n `53` status `ready` deltaP `20.5908` edge `0.2514` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2565` n `53` status `ready` deltaP `26.4885` edge `0.0369` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6179` n `53` status `ready` deltaP `17.3924` edge `0.0625` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5427` n `53` status `ready` deltaP `25.4314` edge `0.1921` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2238` n `53` status `ready` deltaP `16.8766` edge `0.0196` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.8671` n `53` status `ready` deltaP `11.0596` edge `0.488` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
