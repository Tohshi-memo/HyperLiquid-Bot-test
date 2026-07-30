# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T01:22:28.636168+00:00`
- Price records: `672`
- Market context records: `8361`
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

- `news_risk_high->unknown_24h` score `6252.0962` n `52` status `ready` deltaP `35.1896` edge `520.8155` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4576` n `52` status `ready` deltaP `25.9146` edge `0.5084` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9028` n `52` status `ready` deltaP `20.8314` edge `0.1339` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7308` n `52` status `ready` deltaP `22.7134` edge `0.0952` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.06` n `52` status `ready` deltaP `9.5216` edge `0.27` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7742` n `52` status `ready` deltaP `13.3579` edge `0.1022` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7237` n `52` status `ready` deltaP `11.8609` edge `0.1043` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5454` n `52` status `ready` deltaP `17.0263` edge `0.2238` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8316` n `52` status `ready` deltaP `7.6337` edge `0.0652` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2528` n `52` status `ready` deltaP `4.5947` edge `0.0193` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0712` n `52` status `ready` deltaP `5.1935` edge `0.0026` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1701` n `52` status `ready` deltaP `2.6486` edge `0.0085` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5632` n `52` status `ready` deltaP `2.9784` edge `0.0037` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1933` n `52` status `ready` deltaP `-9.0166` edge `-0.0441` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.3037` n `52` status `ready` deltaP `-23.3841` edge `-0.0539` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.9522` n `52` status `ready` deltaP `-26.8963` edge `-0.123` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9585` n `52` status `ready` deltaP `-30.6285` edge `-0.2116` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8924` n `52` status `ready` deltaP `-9.3082` edge `-0.335` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0215` n `52` status `ready` deltaP `-24.0785` edge `-0.291` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.9493` n `52` status `ready` deltaP `-16.9871` edge `-1.3467` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
