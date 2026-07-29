# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T16:07:39.363404+00:00`
- Price records: `672`
- Market context records: `8318`
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

- `news_risk_high->unknown_24h` score `6250.9243` n `52` status `ready` deltaP `35.016` edge `520.719` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8734` n `52` status `ready` deltaP `25.1524` edge `0.4648` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9471` n `52` status `ready` deltaP `21.4302` edge `0.1336` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.609` n `52` status `ready` deltaP `22.2561` edge `0.0881` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0924` n `52` status `ready` deltaP `9.9789` edge `0.2711` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8773` n `52` status `ready` deltaP `14.2561` edge `0.1048` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6998` n `52` status `ready` deltaP `11.5615` edge `0.1043` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6508` n `52` status `ready` deltaP `18.0934` edge `0.2302` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2071` n `52` status `ready` deltaP `10.3776` edge `0.0782` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3307` n `52` status `ready` deltaP `5.6426` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1623` n `52` status `ready` deltaP `6.8402` edge `0.0033` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0108` n `52` status `ready` deltaP `4.2953` edge `0.0126` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4502` n `52` status `ready` deltaP `4.6553` edge `0.007` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3239` n `52` status `ready` deltaP `-10.2142` edge `-0.047` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0033` n `52` status `ready` deltaP `-20.2591` edge `-0.0497` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.7513` n `52` status `ready` deltaP `-21.5144` edge `-0.0588` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2486` n `52` status `ready` deltaP `-33.22` edge `-0.2185` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7472` n `52` status `ready` deltaP `-9.3082` edge `-0.3229` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1636` n `52` status `ready` deltaP `-23.9049` edge `-0.304` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.5451` n `52` status `ready` deltaP `-15.4246` edge `-1.2401` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
