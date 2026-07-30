# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T02:37:25.436327+00:00`
- Price records: `672`
- Market context records: `8366`
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

- `news_risk_high->unknown_24h` score `6252.1106` n `52` status `ready` deltaP `35.1896` edge `520.8167` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1974` n `52` status `ready` deltaP `25.1524` edge `0.4918` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7757` n `52` status `ready` deltaP `20.2326` edge `0.1273` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6266` n `52` status `ready` deltaP `21.9512` edge `0.0916` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9556` n `52` status `ready` deltaP `8.7594` edge `0.2617` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6399` n `52` status `ready` deltaP `12.6094` edge `0.096` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.611` n `52` status `ready` deltaP `11.2621` edge `0.0989` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4278` n `52` status `ready` deltaP `16.2641` edge `0.2138` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8208` n `52` status `ready` deltaP `7.6337` edge `0.0643` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.1833` n `52` status `ready` deltaP `3.9959` edge `0.0175` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0447` n `52` status `ready` deltaP `4.7444` edge `0.0022` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1749` n `52` status `ready` deltaP `2.6486` edge `0.0081` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5798` n `52` status `ready` deltaP `2.6736` edge `0.0036` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1477` n `52` status `ready` deltaP `-8.5675` edge `-0.0433` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.3876` n `52` status `ready` deltaP `-24.2521` edge `-0.0551` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.1465` n `52` status `ready` deltaP `-27.7644` edge `-0.1334` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8735` n `52` status `ready` deltaP `-29.8663` edge `-0.2096` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8804` n `52` status `ready` deltaP `-9.3082` edge `-0.334` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0949` n `52` status `ready` deltaP `-24.4258` edge `-0.2948` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0363` n `52` status `ready` deltaP `-23.2105` edge `-0.9774` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
