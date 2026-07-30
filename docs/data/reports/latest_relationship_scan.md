# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T10:37:27.458987+00:00`
- Price records: `672`
- Market context records: `8401`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6252.6203` n `52` status `ready` deltaP `38.141` edge `520.8395` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2766` n `52` status `ready` deltaP `26.0671` edge `0.4923` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9052` n `52` status `ready` deltaP `21.1308` edge `0.1321` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6023` n `52` status `ready` deltaP `21.6463` edge `0.0916` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.846` n `52` status `ready` deltaP `8.3021` edge `0.2507` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6639` n `52` status `ready` deltaP `12.7591` edge `0.097` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6002` n `52` status `ready` deltaP `11.2621` edge `0.098` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3773` n `52` status `ready` deltaP `16.569` edge `0.2053` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.5812` n `52` status `ready` deltaP `6.1093` edge `0.0545` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2588` n `52` status `ready` deltaP `4.7444` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0891` n `52` status `ready` deltaP `5.4929` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2516` n `52` status `ready` deltaP `2.0498` edge `0.0057` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4841` n `52` status `ready` deltaP `4.1979` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0363` n `52` status `ready` deltaP `-7.3699` edge `-0.042` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7529` n `52` status `ready` deltaP `-27.7244` edge `-0.0624` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.9984` n `52` status `ready` deltaP `-31.063` edge `-0.1824` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.6284` n `52` status `ready` deltaP `-27.7322` edge `-0.2034` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.2687` n `52` status `ready` deltaP `-10.6971` edge `-0.3571` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3251` n `52` status `ready` deltaP `-25.2938` edge `-0.3082` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.5851` n `52` status `ready` deltaP `-23.2105` edge `-0.9398` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
