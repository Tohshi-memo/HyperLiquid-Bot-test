# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T19:07:31.350625+00:00`
- Price records: `672`
- Market context records: `8331`
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

- `news_risk_high->unknown_24h` score `6250.9231` n `52` status `ready` deltaP `35.016` edge `520.7189` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.9438` n `52` status `ready` deltaP `24.8476` edge `0.4727` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6761` n `52` status `ready` deltaP `20.0829` edge `0.12` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5457` n `52` status `ready` deltaP `21.4939` edge `0.0879` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0184` n `52` status `ready` deltaP `9.2167` edge `0.2667` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.737` n `52` status `ready` deltaP `13.5076` edge `0.0981` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5907` n `52` status `ready` deltaP `10.9627` edge `0.0992` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.558` n `52` status `ready` deltaP `17.1787` edge `0.2244` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9636` n `52` status `ready` deltaP `8.5483` edge `0.0701` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.218` n `52` status `ready` deltaP `4.5947` edge `0.0164` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.153` n `52` status `ready` deltaP `6.6905` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1785` n `52` status `ready` deltaP `2.6486` edge `0.0078` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3924` n `52` status `ready` deltaP `5.7223` edge `0.0073` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2628` n `52` status `ready` deltaP `-9.6154` edge `-0.0459` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0081` n `52` status `ready` deltaP `-20.2591` edge `-0.0501` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.0686` n `52` status `ready` deltaP `-22.5561` edge `-0.0783` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2278` n `52` status `ready` deltaP `-32.9151` edge `-0.2188` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8156` n `52` status `ready` deltaP `-9.3082` edge `-0.3286` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1931` n `52` status `ready` deltaP `-24.0785` edge `-0.3053` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.1691` n `52` status `ready` deltaP `-16.6399` edge `-1.284` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
