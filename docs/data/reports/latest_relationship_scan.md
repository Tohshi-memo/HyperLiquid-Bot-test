# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T07:52:36.484279+00:00`
- Price records: `672`
- Market context records: `8389`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5790`

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

- `news_risk_high->unknown_24h` score `6252.3775` n `52` status `ready` deltaP `36.2313` edge `520.832` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6139` n `52` status `ready` deltaP `27.1341` edge `0.5133` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9483` n `52` status `ready` deltaP `21.2805` edge `0.1347` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7126` n `52` status `ready` deltaP `22.561` edge `0.0947` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9824` n `52` status `ready` deltaP `9.0643` edge `0.2631` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6699` n `52` status `ready` deltaP `12.9088` edge `0.0965` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6122` n `52` status `ready` deltaP `11.2621` edge `0.099` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4723` n `52` status `ready` deltaP `17.3312` edge `0.2124` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8246` n `52` status `ready` deltaP `7.7861` edge `0.0636` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2768` n `52` status `ready` deltaP `4.8941` edge `0.0193` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1374` n `52` status `ready` deltaP `6.3911` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1485` n `52` status `ready` deltaP `2.948` edge `0.0083` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4255` n `52` status `ready` deltaP `5.265` edge `0.0061` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1406` n `52` status `ready` deltaP `-8.4178` edge `-0.0437` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6825` n `52` status `ready` deltaP `-27.2035` edge `-0.06` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.6987` n `52` status `ready` deltaP `-29.3269` edge `-0.169` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7532` n `52` status `ready` deltaP `-28.6468` edge `-0.2077` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.98` n `52` status `ready` deltaP `-9.3082` edge `-0.3423` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3239` n `52` status `ready` deltaP `-25.2938` edge `-0.3081` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.8959` n `52` status `ready` deltaP `-23.2105` edge `-0.9657` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
