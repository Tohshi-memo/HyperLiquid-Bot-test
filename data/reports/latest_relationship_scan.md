# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T11:22:24.900058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `537.2903` n `69` status `ready` deltaP `4.5139` edge `44.7441` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.311` n `53` status `ready` deltaP `37.4869` edge `3.0133` maxDD `-3.6503`
- `market_context_high->equity_24h` score `33.0378` n `69` status `ready` deltaP `33.3031` edge `2.6853` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `21.2335` n `69` status `ready` deltaP `54.0761` edge `1.5254` maxDD `-6.9826`
- `news_risk_high->crypto_major_24h` score `16.0573` n `53` status `ready` deltaP `42.0434` edge `1.9749` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2462` n `53` status `ready` deltaP `36.2402` edge `0.8086` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9002` n `53` status `ready` deltaP `47.2222` edge `0.2602` maxDD `0.0`
- `market_context_high->index_24h` score `6.6644` n `69` status `ready` deltaP `39.1078` edge `0.3038` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.4697` n `53` status `ready` deltaP `35.0334` edge `0.2526` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9075` n `53` status `ready` deltaP `46.2437` edge `0.1383` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.8858` n `69` status `ready` deltaP `47.8261` edge `0.3967` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.0882` n `53` status `ready` deltaP `21.2006` edge `0.3481` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5649` n `53` status `ready` deltaP `18.6137` edge `0.236` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1919` n `53` status `ready` deltaP `29.1504` edge `0.097` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1835` n `53` status `ready` deltaP `25.4406` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.1589` n `53` status `ready` deltaP `26.346` edge `0.265` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1565` n `53` status `ready` deltaP `21.9656` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8487` n `53` status `ready` deltaP `14.4261` edge `0.5914` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2502` n `53` status `ready` deltaP `16.8766` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7383` n `53` status `ready` deltaP `17.594` edge `0.0753` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
