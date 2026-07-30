# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T04:37:31.132418+00:00`
- Price records: `672`
- Market context records: `8375`
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

- `news_risk_high->unknown_24h` score `6252.1454` n `52` status `ready` deltaP `35.1896` edge `520.8196` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2192` n `52` status `ready` deltaP `25.3049` edge `0.4926` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9388` n `52` status `ready` deltaP `21.1308` edge `0.1349` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6206` n `52` status `ready` deltaP `21.9512` edge `0.0911` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8809` n `52` status `ready` deltaP `7.9972` edge `0.2572` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6891` n `52` status `ready` deltaP `13.0585` edge `0.0971` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6841` n `52` status `ready` deltaP `11.8609` edge `0.101` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.373` n `52` status `ready` deltaP `16.1117` edge `0.2078` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8402` n `52` status `ready` deltaP `7.7861` edge `0.0649` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2492` n `52` status `ready` deltaP `4.5947` edge `0.019` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0868` n `52` status `ready` deltaP `5.4929` edge `0.0026` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.079` n `52` status `ready` deltaP `3.5468` edge `0.0101` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5117` n `52` status `ready` deltaP `3.8931` edge `0.0042` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1609` n `52` status `ready` deltaP `-8.7172` edge `-0.0434` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5239` n `52` status `ready` deltaP `-25.641` edge `-0.0572` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.4484` n `52` status `ready` deltaP `-29.1533` edge `-0.1493` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7546` n `52` status `ready` deltaP `-28.7992` edge `-0.2068` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.866` n `52` status `ready` deltaP `-9.3082` edge `-0.3328` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.2344` n `52` status `ready` deltaP `-25.1202` edge `-0.3018` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0771` n `52` status `ready` deltaP `-23.2105` edge `-0.9808` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
