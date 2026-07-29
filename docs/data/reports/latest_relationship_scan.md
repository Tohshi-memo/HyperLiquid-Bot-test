# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T22:52:33.092611+00:00`
- Price records: `672`
- Market context records: `8349`
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

- `news_risk_high->unknown_24h` score `6252.0242` n `52` status `ready` deltaP `35.1896` edge `520.8095` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5411` n `52` status `ready` deltaP `26.5244` edge `0.5113` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.904` n `52` status `ready` deltaP `20.6817` edge `0.135` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7368` n `52` status `ready` deltaP `22.7134` edge `0.0957` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2209` n `52` status `ready` deltaP `10.7411` edge `0.2825` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8209` n `52` status `ready` deltaP `13.807` edge `0.1031` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.7077` n `52` status `ready` deltaP `18.0934` edge `0.2375` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.7058` n `52` status `ready` deltaP `11.7112` edge `0.1038` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `0.8024` n `52` status `ready` deltaP `7.3288` edge `0.0648` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2492` n `52` status `ready` deltaP `4.5947` edge `0.019` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0549` n `52` status `ready` deltaP `4.8941` edge `0.0025` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2156` n `52` status `ready` deltaP `2.1995` edge `0.0077` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5236` n `52` status `ready` deltaP `3.5882` edge `0.0047` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2472` n `52` status `ready` deltaP `-9.6154` edge `-0.0446` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2048` n `52` status `ready` deltaP `-22.3424` edge `-0.0526` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.5889` n `52` status `ready` deltaP `-25.1602` edge `-0.1043` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1091` n `52` status `ready` deltaP `-32.0005` edge `-0.215` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9164` n `52` status `ready` deltaP `-9.3082` edge `-0.337` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0815` n `52` status `ready` deltaP `-24.0785` edge `-0.296` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.5291` n `52` status `ready` deltaP `-16.6399` edge `-1.314` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
