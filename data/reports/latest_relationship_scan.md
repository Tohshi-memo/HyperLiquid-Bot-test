# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T18:52:34.437441+00:00`
- Price records: `672`
- Market context records: `8330`
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

- `news_risk_high->unknown_24h` score `6250.9207` n `52` status `ready` deltaP `35.016` edge `520.7187` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.969` n `52` status `ready` deltaP `24.8476` edge `0.4748` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6833` n `52` status `ready` deltaP `20.0829` edge `0.1206` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5639` n `52` status `ready` deltaP `21.6463` edge `0.0884` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0318` n `52` status `ready` deltaP `9.3691` edge `0.2674` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7358` n `52` status `ready` deltaP `13.5076` edge `0.098` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5883` n `52` status `ready` deltaP `10.9627` edge `0.099` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5729` n `52` status `ready` deltaP `17.3312` edge `0.2253` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9914` n `52` status `ready` deltaP `8.7008` edge `0.0714` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2324` n `52` status `ready` deltaP `4.7444` edge `0.0166` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1615` n `52` status `ready` deltaP `6.8402` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1629` n `52` status `ready` deltaP `2.7983` edge `0.0081` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3837` n `52` status `ready` deltaP `5.8748` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2747` n `52` status `ready` deltaP `-9.7651` edge `-0.0459` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0069` n `52` status `ready` deltaP `-20.2591` edge `-0.05` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.0259` n `52` status `ready` deltaP `-22.3825` edge `-0.0759` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2448` n `52` status `ready` deltaP `-33.0675` edge `-0.2192` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8096` n `52` status `ready` deltaP `-9.3082` edge `-0.3281` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1883` n `52` status `ready` deltaP `-24.0785` edge `-0.3049` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.1012` n `52` status `ready` deltaP `-16.4663` edge `-1.2795` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
