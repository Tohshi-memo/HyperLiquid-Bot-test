# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T02:37:26.493036+00:00`
- Price records: `672`
- Market context records: `8472`
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

- `news_risk_high->unknown_24h` score `6266.2229` n `52` status `ready` deltaP `44.0438` edge `521.9337` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.3247` n `61` status `ready` deltaP `23.0483` edge `0.4331` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2553` n `61` status `ready` deltaP `18.78` edge `0.0818` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8164` n `64` status `ready` deltaP `16.701` edge `0.0877` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.2507` n `61` status `ready` deltaP `16.4884` edge `0.1896` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.2156` n `61` status `ready` deltaP `6.6923` edge `0.1806` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `0.5809` n `64` status `ready` deltaP `9.9083` edge `0.0611` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.308` n `64` status `ready` deltaP `6.7646` edge `0.0456` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1259` n `64` status `ready` deltaP `6.0348` edge `0.004` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0608` n `61` status `ready` deltaP `11.6429` edge `0.0232` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.041` n `64` status `ready` deltaP `4.2197` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2689` n `64` status `ready` deltaP `1.9087` edge `0.0052` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4798` n `61` status `ready` deltaP `-2.0742` edge `0.0211` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5141` n `64` status `ready` deltaP `-2.5075` edge `-0.0309` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5645` n `52` status `ready` deltaP `-27.7244` edge `-0.0467` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4248` n `61` status `ready` deltaP `-18.5526` edge `-0.1643` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2528` n `52` status `ready` deltaP `-36.6186` edge `-0.2499` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9114` n `52` status `ready` deltaP `-13.3013` edge `-0.3933` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.2413` n `52` status `ready` deltaP `-34.3216` edge `-0.4077` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.2544` n `52` status `ready` deltaP `-29.6607` edge `-1.7043` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
