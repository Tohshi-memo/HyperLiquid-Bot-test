# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T21:22:28.920158+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10308`

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

- `market_context_high->unknown_24h` score `370.3201` n `75` status `ready` deltaP `2.7152` edge `30.856` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.5095` n `53` status `ready` deltaP `34.1883` edge `2.7185` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.2759` n `75` status `ready` deltaP `28.7291` edge `2.1523` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9578` n `75` status `ready` deltaP `47.5834` edge `1.3474` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.5355` n `53` status `ready` deltaP `42.0434` edge `1.7798` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8272` n `53` status `ready` deltaP `34.2585` edge `0.7869` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.8473` n `53` status `ready` deltaP `38.0208` edge `0.2338` maxDD `0.0`
- `market_context_high->index_24h` score `5.075` n `75` status `ready` deltaP `27.8195` edge `0.2466` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.9079` n `53` status `ready` deltaP `46.5486` edge `0.1363` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.394` n `53` status `ready` deltaP `25.832` edge `0.2243` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0645` n `75` status `ready` deltaP `40.9861` edge `0.337` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.4258` n `53` status `ready` deltaP `17.7155` edge `0.2304` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2573` n `53` status `ready` deltaP `29.6077` edge `0.0994` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0789` n `53` status `ready` deltaP `19.2189` edge `0.2772` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2505` n `53` status `ready` deltaP `26.3388` edge `0.0374` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.902` n `53` status `ready` deltaP `19.0693` edge `0.075` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8167` n `53` status `ready` deltaP `14.4261` edge `0.5873` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7065` n `53` status `ready` deltaP `25.4314` edge `0.2131` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1604` n `53` status `ready` deltaP `15.8287` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6058` n `53` status `ready` deltaP `16.6958` edge `0.0643` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
