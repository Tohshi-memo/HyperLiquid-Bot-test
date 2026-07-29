# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T20:52:29.700299+00:00`
- Price records: `672`
- Market context records: `8339`
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

- `news_risk_high->unknown_24h` score `6250.9711` n `52` status `ready` deltaP `35.016` edge `520.7229` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.0536` n `52` status `ready` deltaP `25.3049` edge `0.4788` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9496` n `52` status `ready` deltaP `20.8314` edge `0.1378` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5577` n `52` status `ready` deltaP `21.4939` edge `0.0889` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0978` n `52` status `ready` deltaP `9.9789` edge `0.2718` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8953` n `52` status `ready` deltaP `14.1064` edge `0.1073` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7406` n `52` status `ready` deltaP `11.7112` edge `0.1067` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6106` n `52` status `ready` deltaP `17.6361` edge `0.2281` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8146` n `52` status `ready` deltaP `7.4813` edge `0.0648` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3115` n `52` status `ready` deltaP `5.1935` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1203` n `52` status `ready` deltaP `6.0917` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1222` n `52` status `ready` deltaP `3.0977` edge `0.0095` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4477` n `52` status `ready` deltaP `4.8077` edge `0.0063` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3059` n `52` status `ready` deltaP `-10.0645` edge `-0.0465` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0769` n `52` status `ready` deltaP `-20.9535` edge `-0.0512` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.311` n `52` status `ready` deltaP `-23.7713` edge `-0.0904` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1855` n `52` status `ready` deltaP `-32.6102` edge `-0.2173` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.896` n `52` status `ready` deltaP `-9.3082` edge `-0.3353` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1571` n `52` status `ready` deltaP `-24.0785` edge `-0.3023` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3491` n `52` status `ready` deltaP `-16.6399` edge `-1.299` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
