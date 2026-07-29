# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T17:55:14.773887+00:00`
- Price records: `672`
- Market context records: `8326`
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

- `news_risk_high->unknown_24h` score `6234.4407` n `52` status `ready` deltaP `35.016` edge `519.3453` maxDD `-2.0278`
- `news_risk_high->equity_4h` score `7.0426` n `52` status `ready` deltaP `25.1524` edge `0.4789` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8152` n `52` status `ready` deltaP `20.6817` edge `0.1276` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6294` n `52` status `ready` deltaP `22.2561` edge `0.0898` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0939` n `52` status `ready` deltaP `9.9789` edge `0.2713` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8545` n `52` status `ready` deltaP `14.1064` edge `0.1039` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6974` n `52` status `ready` deltaP `11.5615` edge `0.1041` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6366` n `52` status `ready` deltaP `17.9409` edge `0.2294` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1766` n `52` status `ready` deltaP `9.3105` edge `0.0838` maxDD `-0.8259`
- `news_risk_high->index_1h` score `0.2959` n `52` status `ready` deltaP `5.3432` edge `0.0179` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1615` n `52` status `ready` deltaP `6.8402` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0847` n `52` status `ready` deltaP `3.3971` edge `0.0114` maxDD `-0.6221`
- `news_risk_high->fx_4h` score `-0.3916` n `52` status `ready` deltaP `5.7223` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2759` n `52` status `ready` deltaP `-9.7651` edge `-0.046` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0033` n `52` status `ready` deltaP `-20.2591` edge `-0.0497` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.1425` n `52` status `ready` deltaP `-21.688` edge `-0.0752` maxDD `-12.0336`
- `news_risk_high->commodity_4h` score `-9.2582` n `52` status `ready` deltaP `-33.22` edge `-0.2193` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7892` n `52` status `ready` deltaP `-9.3082` edge `-0.3264` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1552` n `52` status `ready` deltaP `-23.9049` edge `-0.3033` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.8141` n `52` status `ready` deltaP `-15.7719` edge `-1.2602` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
