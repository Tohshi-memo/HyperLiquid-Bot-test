# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T22:22:26.402083+00:00`
- Price records: `672`
- Market context records: `8346`
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

- `news_risk_high->unknown_24h` score `6252.0074` n `52` status `ready` deltaP `35.1896` edge `520.8081` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4208` n `52` status `ready` deltaP `26.2195` edge `0.5033` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9808` n `52` status `ready` deltaP `20.9811` edge `0.1394` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6896` n `52` status `ready` deltaP `22.4085` edge `0.0938` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2077` n `52` status `ready` deltaP `10.7411` edge `0.2808` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8701` n `52` status `ready` deltaP `14.1064` edge `0.1052` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7345` n `52` status `ready` deltaP `11.8609` edge `0.1052` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6984` n `52` status `ready` deltaP `18.0934` edge `0.2363` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7842` n `52` status `ready` deltaP `7.1764` edge `0.0643` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2828` n `52` status `ready` deltaP `4.8941` edge `0.0198` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0712` n `52` status `ready` deltaP `5.1935` edge `0.0026` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1833` n `52` status `ready` deltaP `2.4989` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5039` n `52` status `ready` deltaP `3.8931` edge `0.0052` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2663` n `52` status `ready` deltaP `-9.7651` edge `-0.0452` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.1722` n `52` status `ready` deltaP `-21.9952` edge `-0.0522` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.5144` n `52` status `ready` deltaP `-24.813` edge `-0.1004` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1395` n `52` status `ready` deltaP `-32.3053` edge `-0.2155` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9248` n `52` status `ready` deltaP `-9.3082` edge `-0.3377` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0935` n `52` status `ready` deltaP `-24.0785` edge `-0.297` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.4523` n `52` status `ready` deltaP `-16.6399` edge `-1.3076` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
