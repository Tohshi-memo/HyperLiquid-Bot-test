# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T13:22:27.819101+00:00`
- Price records: `672`
- Market context records: `8413`
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

- `news_risk_high->unknown_24h` score `6252.8511` n `52` status `ready` deltaP `40.0508` edge `520.846` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.551` n `52` status `ready` deltaP `24.5427` edge `0.442` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.5478` n `52` status `ready` deltaP `19.6338` edge `0.1123` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.3505` n `52` status `ready` deltaP `19.9695` edge `0.0818` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6088` n `52` status `ready` deltaP `12.4597` edge `0.0944` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.5381` n `52` status `ready` deltaP `6.6252` edge `0.2224` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.5031` n `52` status `ready` deltaP `10.813` edge `0.0929` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2401` n `52` status `ready` deltaP `15.6544` edge `0.1938` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.3259` n `52` status `ready` deltaP `4.4325` edge `0.0444` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1218` n `52` status `ready` deltaP `6.0917` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.1114` n `52` status `ready` deltaP `3.3971` edge `0.0155` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3475` n `52` status `ready` deltaP `1.1516` edge `0.0037` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4723` n `52` status `ready` deltaP `4.3504` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9369` n `52` status `ready` deltaP `-6.4717` edge `-0.0397` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7721` n `52` status `ready` deltaP `-27.7244` edge `-0.064` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.3251` n `52` status `ready` deltaP `-32.9727` edge `-0.1969` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.3839` n `52` status `ready` deltaP `-26.0553` edge `-0.1942` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3635` n `52` status `ready` deltaP `-25.2938` edge `-0.3114` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4451` n `52` status `ready` deltaP `-11.9124` edge `-0.3637` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5911` n `52` status `ready` deltaP `-23.2105` edge `-0.9403` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
