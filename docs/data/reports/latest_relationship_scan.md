# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T21:07:47.098461+00:00`
- Price records: `672`
- Market context records: `8340`
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

- `news_risk_high->unknown_24h` score `6250.9795` n `52` status `ready` deltaP `35.016` edge `520.7236` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1078` n `52` status `ready` deltaP `25.4573` edge `0.4823` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9772` n `52` status `ready` deltaP `20.9811` edge `0.1391` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5783` n `52` status `ready` deltaP `21.6463` edge `0.0896` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1229` n `52` status `ready` deltaP `10.1313` edge `0.274` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9217` n `52` status `ready` deltaP `14.2561` edge `0.1085` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7466` n `52` status `ready` deltaP `11.7112` edge `0.1072` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6342` n `52` status `ready` deltaP `17.7885` edge `0.2301` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8` n `52` status `ready` deltaP `7.3288` edge `0.0646` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3115` n `52` status `ready` deltaP `5.1935` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1117` n `52` status `ready` deltaP `5.942` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1353` n `52` status `ready` deltaP `2.948` edge `0.0094` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4565` n `52` status `ready` deltaP `4.6553` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3059` n `52` status `ready` deltaP `-10.0645` edge `-0.0465` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.092` n `52` status `ready` deltaP `-21.1271` edge `-0.0513` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.3453` n `52` status `ready` deltaP `-23.945` edge `-0.0921` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1819` n `52` status `ready` deltaP `-32.6102` edge `-0.217` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9056` n `52` status `ready` deltaP `-9.3082` edge `-0.3361` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1463` n `52` status `ready` deltaP `-24.0785` edge `-0.3014` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3551` n `52` status `ready` deltaP `-16.6399` edge `-1.2995` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
