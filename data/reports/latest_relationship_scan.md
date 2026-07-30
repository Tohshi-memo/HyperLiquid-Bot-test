# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T20:07:33.376849+00:00`
- Price records: `672`
- Market context records: `8443`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5785`

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

- `news_risk_high->unknown_24h` score `6258.7217` n `52` status `ready` deltaP `44.0438` edge `521.3086` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.1391` n `52` status `ready` deltaP `23.0183` edge `0.3345` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6995` n `56` status `ready` deltaP `20.2096` edge `0.1211` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1113` n `52` status `ready` deltaP `18.75` edge `0.07` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6571` n `56` status `ready` deltaP `13.1095` edge `0.0941` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.4618` n `56` status `ready` deltaP `11.3024` edge `0.0862` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1209` n `52` status `ready` deltaP `3.8813` edge `0.1872` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9658` n `52` status `ready` deltaP `13.2153` edge `0.1749` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.571` n `56` status `ready` deltaP `10.2866` edge `0.0071` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.2615` n `56` status `ready` deltaP `4.8974` edge `0.018` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0134` n `52` status `ready` deltaP `1.841` edge `0.0334` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1795` n `56` status `ready` deltaP `2.8016` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3108` n `52` status `ready` deltaP `6.3321` edge `0.0137` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.8304` n `56` status `ready` deltaP `-5.3358` edge `-0.0384` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6617` n `52` status `ready` deltaP `-27.7244` edge `-0.0548` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4906` n `52` status `ready` deltaP `-26.97` edge `-0.197` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.8439` n `52` status `ready` deltaP `-34.8825` edge `-0.2274` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7486` n `52` status `ready` deltaP `-12.7804` edge `-0.3832` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.1194` n `52` status `ready` deltaP `-29.8077` edge `-0.3443` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.5133` n `52` status `ready` deltaP `-25.1469` edge `-1.5893` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
