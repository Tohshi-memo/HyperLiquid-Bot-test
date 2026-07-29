# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T20:22:27.796425+00:00`
- Price records: `672`
- Market context records: `8336`
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

- `news_risk_high->unknown_24h` score `6250.9543` n `52` status `ready` deltaP `35.016` edge `520.7215` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.9704` n `52` status `ready` deltaP `25.0` edge `0.4739` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8645` n `52` status `ready` deltaP `20.532` edge `0.1327` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5225` n `52` status `ready` deltaP `21.189` edge `0.088` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0648` n `52` status `ready` deltaP `9.674` edge `0.2696` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8389` n `52` status `ready` deltaP `13.807` edge `0.1046` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7046` n `52` status `ready` deltaP `11.4118` edge `0.1057` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5745` n `52` status `ready` deltaP `17.3312` edge `0.2255` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8522` n `52` status `ready` deltaP `7.7861` edge `0.0659` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.278` n `52` status `ready` deltaP `4.8941` edge `0.0194` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1195` n `52` status `ready` deltaP `6.0917` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1497` n `52` status `ready` deltaP `2.7983` edge `0.0092` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4375` n `52` status `ready` deltaP `4.9601` edge `0.0066` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3191` n `52` status `ready` deltaP `-10.2142` edge `-0.0466` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0443` n `52` status `ready` deltaP `-20.6063` edge `-0.0508` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.2449` n `52` status `ready` deltaP `-23.4241` edge `-0.0872` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1927` n `52` status `ready` deltaP `-32.6102` edge `-0.2179` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8732` n `52` status `ready` deltaP `-9.3082` edge `-0.3334` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1739` n `52` status `ready` deltaP `-24.0785` edge `-0.3037` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3047` n `52` status `ready` deltaP `-16.6399` edge `-1.2953` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
