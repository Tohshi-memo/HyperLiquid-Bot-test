# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T00:52:25.881754+00:00`
- Price records: `672`
- Market context records: `8358`
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

- `news_risk_high->unknown_24h` score `6252.0878` n `52` status `ready` deltaP `35.1896` edge `520.8148` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5612` n `52` status `ready` deltaP `26.2195` edge `0.515` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.916` n `52` status `ready` deltaP `20.8314` edge `0.135` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7684` n `52` status `ready` deltaP `23.0183` edge `0.0963` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1133` n `52` status `ready` deltaP `9.8264` edge `0.2748` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.809` n `52` status `ready` deltaP `13.6573` edge `0.1031` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7333` n `52` status `ready` deltaP `11.8609` edge `0.1051` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6049` n `52` status `ready` deltaP `17.3312` edge `0.2294` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.834` n `52` status `ready` deltaP `7.6337` edge `0.0654` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2552` n `52` status `ready` deltaP `4.5947` edge `0.0195` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0806` n `52` status `ready` deltaP `5.3432` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1713` n `52` status `ready` deltaP `2.6486` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5624` n `52` status `ready` deltaP `2.9784` edge `0.0038` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2064` n `52` status `ready` deltaP `-9.1663` edge `-0.0442` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2723` n `52` status `ready` deltaP `-23.0369` edge `-0.0536` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.8741` n `52` status `ready` deltaP `-26.5491` edge `-0.1188` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9913` n `52` status `ready` deltaP `-30.9334` edge `-0.2123` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8996` n `52` status `ready` deltaP `-9.3082` edge `-0.3356` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0215` n `52` status `ready` deltaP `-24.0785` edge `-0.291` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.8545` n `52` status `ready` deltaP `-16.9871` edge `-1.3388` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
