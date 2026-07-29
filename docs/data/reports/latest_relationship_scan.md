# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T17:07:25.573669+00:00`
- Price records: `672`
- Market context records: `8322`
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

- `news_risk_high->unknown_24h` score `6250.9063` n `52` status `ready` deltaP `35.016` edge `520.7175` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.991` n `52` status `ready` deltaP `25.1524` edge `0.4746` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.916` n `52` status `ready` deltaP `21.1308` edge `0.133` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6246` n `52` status `ready` deltaP `22.2561` edge `0.0894` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1112` n `52` status `ready` deltaP `10.1313` edge `0.2725` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9144` n `52` status `ready` deltaP `14.5555` edge `0.1059` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7561` n `52` status `ready` deltaP `12.0106` edge `0.106` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6516` n `52` status `ready` deltaP `18.0934` edge `0.2303` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1415` n `52` status `ready` deltaP `9.7678` edge `0.0768` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3426` n `52` status `ready` deltaP `5.7923` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1623` n `52` status `ready` deltaP `6.8402` edge `0.0033` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0383` n `52` status `ready` deltaP `3.8462` edge `0.0115` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4162` n `52` status `ready` deltaP `5.265` edge `0.0073` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2927` n `52` status `ready` deltaP `-9.9148` edge `-0.0464` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0021` n `52` status `ready` deltaP `-20.2591` edge `-0.0496` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.8065` n `52` status `ready` deltaP `-21.5144` edge `-0.0634` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2534` n `52` status `ready` deltaP `-33.22` edge `-0.2189` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7784` n `52` status `ready` deltaP `-9.3082` edge `-0.3255` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1528` n `52` status `ready` deltaP `-23.9049` edge `-0.3031` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.6363` n `52` status `ready` deltaP `-15.4246` edge `-1.2477` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
