# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T12:37:31.051484+00:00`
- Price records: `672`
- Market context records: `8410`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6252.7842` n `52` status `ready` deltaP `39.5299` edge `520.8439` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.7338` n `52` status `ready` deltaP `24.8476` edge `0.4552` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6438` n `52` status `ready` deltaP `19.9332` edge `0.1183` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.4147` n `52` status `ready` deltaP `20.4268` edge `0.0841` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6244` n `52` status `ready` deltaP `12.4597` edge `0.0957` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.6165` n `52` status `ready` deltaP `7.0825` edge `0.2294` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.5295` n `52` status `ready` deltaP `10.813` edge `0.0951` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2635` n `52` status `ready` deltaP `15.6544` edge `0.1968` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.3829` n `52` status `ready` deltaP `4.8898` edge `0.0461` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.1474` n `52` status `ready` deltaP `3.6965` edge `0.0165` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1055` n `52` status `ready` deltaP `5.7923` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.3259` n `52` status `ready` deltaP `1.3013` edge `0.0045` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4746` n `52` status `ready` deltaP `4.3504` edge `0.0059` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9393` n `52` status `ready` deltaP `-6.4717` edge `-0.0399` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7661` n `52` status `ready` deltaP `-27.7244` edge `-0.0635` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.2415` n `52` status `ready` deltaP `-32.4519` edge `-0.1934` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.4444` n `52` status `ready` deltaP `-26.5126` edge `-0.1962` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3515` n `52` status `ready` deltaP `-25.2938` edge `-0.3104` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4343` n `52` status `ready` deltaP `-11.9124` edge `-0.3628` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5707` n `52` status `ready` deltaP `-23.2105` edge `-0.9386` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
