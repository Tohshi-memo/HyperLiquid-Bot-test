# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T06:22:32.100448+00:00`
- Price records: `672`
- Market context records: `8382`
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

- `news_risk_high->unknown_24h` score `6252.2519` n `52` status `ready` deltaP `35.7105` edge `520.825` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4676` n `52` status `ready` deltaP `26.2195` edge `0.5072` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9376` n `52` status `ready` deltaP `21.1308` edge `0.1348` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.658` n `52` status `ready` deltaP `22.1037` edge `0.0932` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9099` n `52` status `ready` deltaP `8.1496` edge `0.2599` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7094` n `52` status `ready` deltaP `13.2082` edge `0.0978` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.647` n `52` status `ready` deltaP `11.4118` edge `0.1009` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4337` n `52` status `ready` deltaP `16.8739` edge `0.2105` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8414` n `52` status `ready` deltaP `7.7861` edge `0.065` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2768` n `52` status `ready` deltaP `4.8941` edge `0.0193` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1117` n `52` status `ready` deltaP `5.942` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0635` n `52` status `ready` deltaP `3.6965` edge `0.0104` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4476` n `52` status `ready` deltaP `4.9601` edge `0.0053` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1921` n `52` status `ready` deltaP `-8.8669` edge `-0.045` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6439` n `52` status `ready` deltaP `-26.8563` edge `-0.0591` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.6039` n `52` status `ready` deltaP `-29.3269` edge `-0.1611` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7388` n `52` status `ready` deltaP `-28.6468` edge `-0.2065` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9044` n `52` status `ready` deltaP `-9.3082` edge `-0.336` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3143` n `52` status `ready` deltaP `-25.2938` edge `-0.3073` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0423` n `52` status `ready` deltaP `-23.2105` edge `-0.9779` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
