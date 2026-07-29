# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T21:37:33.258505+00:00`
- Price records: `672`
- Market context records: `8342`
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

- `news_risk_high->unknown_24h` score `6250.9975` n `52` status `ready` deltaP `35.016` edge `520.7251` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.239` n `52` status `ready` deltaP `25.7622` edge `0.4912` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0347` n `52` status `ready` deltaP `21.2805` edge `0.1419` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.623` n `52` status `ready` deltaP `21.9512` edge `0.0913` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1637` n `52` status `ready` deltaP `10.4362` edge `0.2772` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.942` n `52` status `ready` deltaP `14.4058` edge `0.1092` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7825` n `52` status `ready` deltaP `12.0106` edge `0.1082` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6719` n `52` status `ready` deltaP `18.0934` edge `0.2329` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7708` n `52` status `ready` deltaP `7.0239` edge `0.0642` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3139` n `52` status `ready` deltaP `5.1935` edge `0.0204` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0961` n `52` status `ready` deltaP `5.6426` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1497` n `52` status `ready` deltaP `2.7983` edge `0.0092` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4754` n `52` status `ready` deltaP `4.3504` edge `0.0058` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3035` n `52` status `ready` deltaP `-10.0645` edge `-0.0463` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.1233` n `52` status `ready` deltaP `-21.4744` edge `-0.0516` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.4115` n `52` status `ready` deltaP `-24.2922` edge `-0.0953` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1771` n `52` status `ready` deltaP `-32.6102` edge `-0.2166` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9212` n `52` status `ready` deltaP `-9.3082` edge `-0.3374` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1223` n `52` status `ready` deltaP `-24.0785` edge `-0.2994` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3803` n `52` status `ready` deltaP `-16.6399` edge `-1.3016` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
