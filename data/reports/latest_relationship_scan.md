# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T23:07:35.757072+00:00`
- Price records: `672`
- Market context records: `8350`
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

- `news_risk_high->unknown_24h` score `6252.0302` n `52` status `ready` deltaP `35.1896` edge `520.81` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5891` n `52` status `ready` deltaP `26.5244` edge `0.5153` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8789` n `52` status `ready` deltaP `20.532` edge `0.1339` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7574` n `52` status `ready` deltaP `22.8659` edge `0.0964` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2248` n `52` status `ready` deltaP `10.7411` edge `0.283` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8006` n `52` status `ready` deltaP `13.6573` edge `0.1024` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.7124` n `52` status `ready` deltaP `18.0934` edge `0.2381` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.6902` n `52` status `ready` deltaP `11.5615` edge `0.1035` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `0.8182` n `52` status `ready` deltaP `7.4813` edge `0.0651` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2349` n `52` status `ready` deltaP `4.445` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0549` n `52` status `ready` deltaP `4.8941` edge `0.0025` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2324` n `52` status `ready` deltaP `2.0498` edge `0.0073` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5331` n `52` status `ready` deltaP `3.4357` edge `0.0045` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2472` n `52` status `ready` deltaP `-9.6154` edge `-0.0446` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2211` n `52` status `ready` deltaP `-22.516` edge `-0.0528` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.628` n `52` status `ready` deltaP `-25.3338` edge `-0.1064` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1079` n `52` status `ready` deltaP `-32.0005` edge `-0.2149` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.914` n `52` status `ready` deltaP `-9.3082` edge `-0.3368` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0779` n `52` status `ready` deltaP `-24.0785` edge `-0.2957` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.5874` n `52` status `ready` deltaP `-16.8135` edge `-1.3177` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
