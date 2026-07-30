# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T20:37:27.221966+00:00`
- Price records: `672`
- Market context records: `8445`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5785`

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

- `news_risk_high->unknown_24h` score `6259.2977` n `52` status `ready` deltaP `44.0438` edge `521.3566` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.1115` n `52` status `ready` deltaP `23.0183` edge `0.3322` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.934` n `58` status `ready` deltaP `21.0717` edge `0.1349` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.109` n `52` status `ready` deltaP `18.75` edge `0.0698` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.7919` n `58` status `ready` deltaP `14.4642` edge `0.0963` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2474` n `58` status `ready` deltaP `9.4466` edge `0.0807` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1296` n `52` status `ready` deltaP `4.0338` edge `0.1873` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9532` n `52` status `ready` deltaP `13.0629` edge `0.1743` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6952` n `58` status `ready` deltaP `11.7644` edge `0.0076` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4025` n `58` status `ready` deltaP `6.3752` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.017` n `52` status `ready` deltaP `1.841` edge `0.0331` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1944` n `58` status `ready` deltaP `2.705` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3195` n `52` status `ready` deltaP `6.1797` edge `0.0136` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.621` n `58` status `ready` deltaP `-3.4535` edge `-0.0335` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6533` n `52` status `ready` deltaP `-27.7244` edge `-0.0541` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4772` n `52` status `ready` deltaP `-26.8175` edge `-0.1969` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.8751` n `52` status `ready` deltaP `-34.8825` edge `-0.23` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7654` n `52` status `ready` deltaP `-12.7804` edge `-0.3846` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.2048` n `52` status `ready` deltaP `-30.1549` edge `-0.3491` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.6491` n `52` status `ready` deltaP `-25.4941` edge `-1.5983` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
