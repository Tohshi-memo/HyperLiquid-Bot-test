# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T18:07:40.413378+00:00`
- Price records: `672`
- Market context records: `8327`
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

- `news_risk_high->unknown_24h` score `6250.9147` n `52` status `ready` deltaP `35.016` edge `520.7182` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.0402` n `52` status `ready` deltaP `25.1524` edge `0.4787` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7757` n `52` status `ready` deltaP `20.532` edge `0.1253` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6148` n `52` status `ready` deltaP `22.1037` edge `0.0896` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0798` n `52` status `ready` deltaP `9.8264` edge `0.2705` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8197` n `52` status `ready` deltaP `13.9567` edge `0.102` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6698` n `52` status `ready` deltaP `11.4118` edge `0.1028` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6201` n `52` status `ready` deltaP `17.7885` edge `0.2283` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.064` n `52` status `ready` deltaP `9.1581` edge `0.0744` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2791` n `52` status `ready` deltaP `5.1935` edge `0.0175` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1615` n `52` status `ready` deltaP `6.8402` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1078` n `52` status `ready` deltaP `3.2474` edge `0.0097` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3837` n `52` status `ready` deltaP `5.8748` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2759` n `52` status `ready` deltaP `-9.7651` edge `-0.046` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0045` n `52` status `ready` deltaP `-20.2591` edge `-0.0498` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.9087` n `52` status `ready` deltaP `-21.8616` edge `-0.0696` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2606` n `52` status `ready` deltaP `-33.22` edge `-0.2195` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7952` n `52` status `ready` deltaP `-9.3082` edge `-0.3269` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1588` n `52` status `ready` deltaP `-23.9049` edge `-0.3036` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.8808` n `52` status `ready` deltaP `-15.9455` edge `-1.2646` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
