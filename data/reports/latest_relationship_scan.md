# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T01:07:30.930442+00:00`
- Price records: `672`
- Market context records: `8466`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6264.4805` n `52` status `ready` deltaP `44.0438` edge `521.7885` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.4486` n `60` status `ready` deltaP `23.6077` edge `0.4397` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8265` n `61` status `ready` deltaP `20.3127` edge `0.131` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.3097` n `60` status `ready` deltaP `19.3394` edge `0.0826` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5589` n `61` status `ready` deltaP `12.4521` edge `0.0903` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.2806` n `60` status `ready` deltaP `17.124` edge `0.1892` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.2739` n `60` status `ready` deltaP `7.0935` edge `0.1854` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2219` n `61` status `ready` deltaP `9.3084` edge `0.0795` maxDD `-1.1783`
- `news_risk_high->fx_1h` score `0.4663` n `61` status `ready` deltaP `9.1734` edge `0.0058` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4335` n `61` status `ready` deltaP `7.0629` edge `0.0179` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `0.0442` n `60` status `ready` deltaP `11.5854` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0236` n `61` status `ready` deltaP `4.6751` edge `0.0072` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.3581` n `60` status `ready` deltaP `-1.1179` edge `0.0244` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.5103` n `61` status `ready` deltaP `-2.4443` edge `-0.031` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5825` n `52` status `ready` deltaP `-27.7244` edge `-0.0482` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4386` n `60` status `ready` deltaP `-18.7094` edge `-0.1644` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.224` n `52` status `ready` deltaP `-36.6186` edge `-0.2475` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8994` n `52` status `ready` deltaP `-13.3013` edge `-0.3923` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.0044` n `52` status `ready` deltaP `-33.2799` edge `-0.3949` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.9647` n `52` status `ready` deltaP `-28.6191` edge `-1.6871` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
