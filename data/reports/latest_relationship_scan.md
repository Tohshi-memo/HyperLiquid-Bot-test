# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T12:52:26.510259+00:00`
- Price records: `672`
- Market context records: `8411`
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

- `news_risk_high->unknown_24h` score `6252.8053` n `52` status `ready` deltaP `39.7035` edge `520.8445` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.6592` n `52` status `ready` deltaP `24.6951` edge `0.45` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6018` n `52` status `ready` deltaP `19.7835` edge `0.1158` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.3917` n `52` status `ready` deltaP `20.2744` edge `0.0832` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6172` n `52` status `ready` deltaP `12.4597` edge `0.0951` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.5883` n `52` status `ready` deltaP `6.9301` edge `0.2268` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.5187` n `52` status `ready` deltaP `10.813` edge `0.0942` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2549` n `52` status `ready` deltaP `15.6544` edge `0.1957` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.3623` n `52` status `ready` deltaP `4.7374` edge `0.0454` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.1294` n `52` status `ready` deltaP `3.5468` edge `0.016` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.114` n `52` status `ready` deltaP `5.942` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.3307` n `52` status `ready` deltaP `1.3013` edge `0.0041` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4739` n `52` status `ready` deltaP `4.3504` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9381` n `52` status `ready` deltaP `-6.4717` edge `-0.0398` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7685` n `52` status `ready` deltaP `-27.7244` edge `-0.0637` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.271` n `52` status `ready` deltaP `-32.6255` edge `-0.1947` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.4227` n `52` status `ready` deltaP `-26.3602` edge `-0.1954` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3563` n `52` status `ready` deltaP `-25.2938` edge `-0.3108` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4379` n `52` status `ready` deltaP `-11.9124` edge `-0.3631` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5791` n `52` status `ready` deltaP `-23.2105` edge `-0.9393` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
