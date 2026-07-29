# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T19:52:25.598748+00:00`
- Price records: `672`
- Market context records: `8334`
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

- `news_risk_high->unknown_24h` score `6250.9387` n `52` status `ready` deltaP `35.016` edge `520.7202` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.939` n `52` status `ready` deltaP `24.8476` edge `0.4723` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7457` n `52` status `ready` deltaP `20.2326` edge `0.1248` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5165` n `52` status `ready` deltaP `21.189` edge `0.0875` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0452` n `52` status `ready` deltaP `9.5216` edge `0.2681` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7682` n `52` status `ready` deltaP `13.5076` edge `0.1007` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6446` n `52` status `ready` deltaP `11.1124` edge `0.1027` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5667` n `52` status `ready` deltaP `17.3312` edge `0.2245` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.891` n `52` status `ready` deltaP `8.091` edge `0.0671` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2312` n `52` status `ready` deltaP `4.5947` edge `0.0175` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.128` n `52` status `ready` deltaP `6.2414` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1905` n `52` status `ready` deltaP `2.4989` edge `0.0078` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4193` n `52` status `ready` deltaP `5.265` edge `0.0069` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2903` n `52` status `ready` deltaP `-9.9148` edge `-0.0462` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0129` n `52` status `ready` deltaP `-20.2591` edge `-0.0505` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.1811` n `52` status `ready` deltaP `-23.0769` edge `-0.0842` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2084` n `52` status `ready` deltaP `-32.7626` edge `-0.2182` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8504` n `52` status `ready` deltaP `-9.3082` edge `-0.3315` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1895` n `52` status `ready` deltaP `-24.0785` edge `-0.305` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.2615` n `52` status `ready` deltaP `-16.6399` edge `-1.2917` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
