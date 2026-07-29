# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T22:43:42.785873+00:00`
- Price records: `672`
- Market context records: `8348`
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

- `news_risk_high->unknown_24h` score `6252.0158` n `52` status `ready` deltaP `35.1896` edge `520.8088` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.469` n `52` status `ready` deltaP `26.372` edge `0.5063` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.94` n `52` status `ready` deltaP `20.8314` edge `0.137` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7114` n `52` status `ready` deltaP `22.561` edge `0.0946` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.21` n `52` status `ready` deltaP `10.7411` edge `0.2811` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8449` n `52` status `ready` deltaP `13.9567` edge `0.1041` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.713` n `52` status `ready` deltaP `11.7112` edge `0.1044` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6992` n `52` status `ready` deltaP `18.0934` edge `0.2364` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7842` n `52` status `ready` deltaP `7.1764` edge `0.0643` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.266` n `52` status `ready` deltaP `4.7444` edge `0.0194` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0634` n `52` status `ready` deltaP `5.0438` edge `0.0026` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2` n `52` status `ready` deltaP `2.3492` edge `0.008` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5142` n `52` status `ready` deltaP `3.7406` edge `0.0049` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2496` n `52` status `ready` deltaP `-9.6154` edge `-0.0448` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.1885` n `52` status `ready` deltaP `-22.1688` edge `-0.0524` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.5523` n `52` status `ready` deltaP `-24.9866` edge `-0.1024` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1225` n `52` status `ready` deltaP `-32.1529` edge `-0.2151` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9188` n `52` status `ready` deltaP `-9.3082` edge `-0.3372` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0863` n `52` status `ready` deltaP `-24.0785` edge `-0.2964` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.4883` n `52` status `ready` deltaP `-16.6399` edge `-1.3106` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
