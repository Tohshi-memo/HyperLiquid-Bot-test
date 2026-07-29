# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T14:07:25.606789+00:00`
- Price records: `672`
- Market context records: `8309`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6250.9538` n `52` status `ready` deltaP `35.1896` edge `520.7203` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.5792` n `52` status `ready` deltaP `25.0` edge `0.4413` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7205` n `52` status `ready` deltaP `20.532` edge `0.1207` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.4941` n `52` status `ready` deltaP `21.4939` edge `0.0836` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9975` n `52` status `ready` deltaP `9.3691` edge `0.263` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7874` n `52` status `ready` deltaP `13.6573` edge `0.1013` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6218` n `52` status `ready` deltaP `11.1124` edge `0.1008` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5881` n `52` status `ready` deltaP `17.7885` edge `0.2242` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2083` n `52` status `ready` deltaP `10.3776` edge `0.0783` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2204` n `52` status `ready` deltaP `4.5947` edge `0.0166` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1615` n `52` status `ready` deltaP `6.8402` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0096` n `52` status `ready` deltaP `4.2953` edge `0.0125` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4589` n `52` status `ready` deltaP `4.5028` edge `0.0069` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2711` n `52` status `ready` deltaP `-9.7651` edge `-0.0456` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.9997` n `52` status `ready` deltaP `-20.2591` edge `-0.0494` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.6306` n `52` status `ready` deltaP `-21.3408` edge `-0.0499` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1886` n `52` status `ready` deltaP `-33.22` edge `-0.2135` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7292` n `52` status `ready` deltaP `-9.3082` edge `-0.3214` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.184` n `52` status `ready` deltaP `-23.9049` edge `-0.3057` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.2459` n `52` status `ready` deltaP `-14.7302` edge `-1.2198` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
