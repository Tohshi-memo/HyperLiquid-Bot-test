# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T20:07:35.433936+00:00`
- Price records: `672`
- Market context records: `8335`
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

- `news_risk_high->unknown_24h` score `6250.9471` n `52` status `ready` deltaP `35.016` edge `520.7209` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.9438` n `52` status `ready` deltaP `24.8476` edge `0.4727` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8129` n `52` status `ready` deltaP `20.3823` edge `0.1294` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5189` n `52` status `ready` deltaP `21.189` edge `0.0877` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0499` n `52` status `ready` deltaP `9.5216` edge `0.2687` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8054` n `52` status `ready` deltaP `13.6573` edge `0.1028` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6782` n `52` status `ready` deltaP `11.2621` edge `0.1045` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5683` n `52` status `ready` deltaP `17.3312` edge `0.2247` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8704` n `52` status `ready` deltaP `7.9386` edge `0.0664` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2564` n `52` status `ready` deltaP `4.7444` edge `0.0186` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.128` n `52` status `ready` deltaP `6.2414` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1689` n `52` status `ready` deltaP `2.6486` edge `0.0086` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4288` n `52` status `ready` deltaP `5.1126` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3059` n `52` status `ready` deltaP `-10.0645` edge `-0.0465` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0292` n `52` status `ready` deltaP `-20.4327` edge `-0.0507` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.213` n `52` status `ready` deltaP `-23.2505` edge `-0.0857` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1939` n `52` status `ready` deltaP `-32.6102` edge `-0.218` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8612` n `52` status `ready` deltaP `-9.3082` edge `-0.3324` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1823` n `52` status `ready` deltaP `-24.0785` edge `-0.3044` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.2855` n `52` status `ready` deltaP `-16.6399` edge `-1.2937` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
