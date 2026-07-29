# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T22:07:25.267624+00:00`
- Price records: `672`
- Market context records: `8345`
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

- `news_risk_high->unknown_24h` score `6251.9978` n `52` status `ready` deltaP `35.1896` edge `520.8073` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.3714` n `52` status `ready` deltaP `26.0671` edge `0.5002` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0168` n `52` status `ready` deltaP `21.1308` edge `0.1414` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.669` n `52` status `ready` deltaP `22.2561` edge `0.0931` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2045` n `52` status `ready` deltaP `10.7411` edge `0.2804` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9013` n `52` status `ready` deltaP `14.2561` edge `0.1068` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7645` n `52` status `ready` deltaP `12.0106` edge `0.1067` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6945` n `52` status `ready` deltaP `18.0934` edge `0.2358` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7842` n `52` status `ready` deltaP `7.1764` edge `0.0643` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2996` n `52` status `ready` deltaP `5.0438` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0798` n `52` status `ready` deltaP `5.3432` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1665` n `52` status `ready` deltaP `2.6486` edge `0.0088` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4944` n `52` status `ready` deltaP `4.0455` edge `0.0054` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2831` n `52` status `ready` deltaP `-9.9148` edge `-0.0456` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.1559` n `52` status `ready` deltaP `-21.8216` edge `-0.052` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.4777` n `52` status `ready` deltaP `-24.6394` edge `-0.0985` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1565` n `52` status `ready` deltaP `-32.4578` edge `-0.2159` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.926` n `52` status `ready` deltaP `-9.3082` edge `-0.3378` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1007` n `52` status `ready` deltaP `-24.0785` edge `-0.2976` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.4199` n `52` status `ready` deltaP `-16.6399` edge `-1.3049` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
