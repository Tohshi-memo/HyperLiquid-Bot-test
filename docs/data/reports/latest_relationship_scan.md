# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T21:52:25.770238+00:00`
- Price records: `672`
- Market context records: `8344`
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

- `news_risk_high->unknown_24h` score `6251.9846` n `52` status `ready` deltaP `35.1896` edge `520.8062` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.304` n `52` status `ready` deltaP `25.9146` edge `0.4956` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0408` n `52` status `ready` deltaP `21.2805` edge `0.1424` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.646` n `52` status `ready` deltaP `22.1037` edge `0.0922` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1849` n `52` status `ready` deltaP `10.5886` edge `0.2789` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9348` n `52` status `ready` deltaP `14.4058` edge `0.1086` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7813` n `52` status `ready` deltaP `12.0106` edge `0.1081` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6836` n `52` status `ready` deltaP `18.0934` edge `0.2344` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7684` n `52` status `ready` deltaP `7.0239` edge `0.064` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3139` n `52` status `ready` deltaP `5.1935` edge `0.0204` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0876` n `52` status `ready` deltaP `5.4929` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1509` n `52` status `ready` deltaP `2.7983` edge `0.0091` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4849` n `52` status `ready` deltaP `4.1979` edge `0.0056` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3011` n `52` status `ready` deltaP `-10.0645` edge `-0.0461` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.1396` n `52` status `ready` deltaP `-21.648` edge `-0.0518` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.4434` n `52` status `ready` deltaP `-24.4658` edge `-0.0968` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1747` n `52` status `ready` deltaP `-32.6102` edge `-0.2164` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.926` n `52` status `ready` deltaP `-9.3082` edge `-0.3378` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1103` n `52` status `ready` deltaP `-24.0785` edge `-0.2984` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3947` n `52` status `ready` deltaP `-16.6399` edge `-1.3028` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
