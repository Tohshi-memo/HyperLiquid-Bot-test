# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T06:37:29.475205+00:00`
- Price records: `672`
- Market context records: `8383`
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

- `news_risk_high->unknown_24h` score `6252.2639` n `52` status `ready` deltaP `35.7105` edge `520.826` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4918` n `52` status `ready` deltaP `26.372` edge `0.5082` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9352` n `52` status `ready` deltaP `21.1308` edge `0.1346` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6604` n `52` status `ready` deltaP `22.1037` edge `0.0934` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9225` n `52` status `ready` deltaP `8.3021` edge `0.2605` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7106` n `52` status `ready` deltaP `13.2082` edge `0.0979` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6626` n `52` status `ready` deltaP `11.5615` edge `0.1012` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4448` n `52` status `ready` deltaP `17.0263` edge `0.2109` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8402` n `52` status `ready` deltaP `7.7861` edge `0.0649` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2768` n `52` status `ready` deltaP `4.8941` edge `0.0193` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1203` n `52` status `ready` deltaP `6.0917` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0647` n `52` status `ready` deltaP `3.6965` edge `0.0103` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4381` n `52` status `ready` deltaP `5.1126` edge `0.0055` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1921` n `52` status `ready` deltaP `-8.8669` edge `-0.045` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.659` n `52` status `ready` deltaP `-27.0299` edge `-0.0592` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.6219` n `52` status `ready` deltaP `-29.3269` edge `-0.1626` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7424` n `52` status `ready` deltaP `-28.6468` edge `-0.2068` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9152` n `52` status `ready` deltaP `-9.3082` edge `-0.3369` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3179` n `52` status `ready` deltaP `-25.2938` edge `-0.3076` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0267` n `52` status `ready` deltaP `-23.2105` edge `-0.9766` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
