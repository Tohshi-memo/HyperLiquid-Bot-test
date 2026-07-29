# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T18:22:32.683946+00:00`
- Price records: `672`
- Market context records: `8328`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6250.9171` n `52` status `ready` deltaP `35.016` edge `520.7184` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.0426` n `52` status `ready` deltaP `25.1524` edge `0.4789` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7517` n `52` status `ready` deltaP `20.3823` edge `0.1243` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6014` n `52` status `ready` deltaP `21.9512` edge `0.0895` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0679` n `52` status `ready` deltaP `9.674` edge `0.27` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7873` n `52` status `ready` deltaP `13.807` edge `0.1003` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.641` n `52` status `ready` deltaP `11.2621` edge `0.1014` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.606` n `52` status `ready` deltaP `17.6361` edge `0.2275` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0434` n `52` status `ready` deltaP `9.0056` edge `0.0737` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.266` n `52` status `ready` deltaP `5.0438` edge `0.0174` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1615` n `52` status `ready` deltaP `6.8402` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1234` n `52` status `ready` deltaP `3.0977` edge `0.0094` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3837` n `52` status `ready` deltaP `5.8748` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2759` n `52` status `ready` deltaP `-9.7651` edge `-0.046` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0057` n `52` status `ready` deltaP `-20.2591` edge `-0.0499` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.9453` n `52` status `ready` deltaP `-22.0352` edge `-0.0715` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2618` n `52` status `ready` deltaP `-33.22` edge `-0.2196` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8024` n `52` status `ready` deltaP `-9.3082` edge `-0.3275` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1624` n `52` status `ready` deltaP `-23.9049` edge `-0.3039` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.9499` n `52` status `ready` deltaP `-16.1191` edge `-1.2692` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
