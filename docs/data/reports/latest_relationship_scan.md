# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T18:26:26.339319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11764`

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

- `market_context_high->unknown_24h` score `303.7651` n `84` status `ready` deltaP `6.4425` edge `25.2849` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `85.4274` n `94` status `ready` deltaP `8.1053` edge `7.1097` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.0166` n `53` status `ready` deltaP `22.0866` edge `2.2581` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.9992` n `84` status `ready` deltaP `19.8179` edge `1.6051` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.2451` n `53` status `ready` deltaP `37.0699` edge `1.3911` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.3289` n `53` status `ready` deltaP `32.7341` edge `0.6722` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `7.7909` n `84` status `ready` deltaP `39.7677` edge `1.1433` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.5168` n `53` status `ready` deltaP `43.4256` edge `0.3369` maxDD `0.0`
- `market_context_high->metal_24h` score `6.1631` n `84` status `ready` deltaP `38.8491` edge `0.2959` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.728` n `53` status `ready` deltaP `44.7193` edge `0.1335` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9249` n `84` status `ready` deltaP `21.7911` edge `0.1913` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.5165` n `53` status `ready` deltaP `19.9941` edge `0.1901` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0291` n `53` status `ready` deltaP `26.7114` edge `0.0997` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0264` n `53` status `ready` deltaP `21.353` edge `0.2586` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.0083` n `53` status `ready` deltaP `16.967` edge `0.2006` maxDD `-3.7082`
- `news_risk_high->metal_1h` score `2.2301` n `53` status `ready` deltaP `26.1891` edge `0.0367` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.7124` n `53` status `ready` deltaP `18.1546` edge `0.0653` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.596` n `53` status `ready` deltaP `25.7363` edge `0.1969` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1831` n `53` status `ready` deltaP `16.4275` edge `0.0192` maxDD `-0.4103`
- `market_context_high->fx_24h` score `0.5717` n `84` status `ready` deltaP `23.896` edge `0.0483` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
