# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T20:22:31.190900+00:00`
- Price records: `672`
- Market context records: `8444`
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

- `news_risk_high->unknown_24h` score `6259.0109` n `52` status `ready` deltaP `44.0438` edge `521.3327` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.1247` n `52` status `ready` deltaP `23.0183` edge `0.3333` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8162` n `57` status `ready` deltaP `20.6482` edge `0.1279` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1101` n `52` status `ready` deltaP `18.75` edge `0.0699` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.7351` n `57` status `ready` deltaP `13.7987` edge `0.096` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.3693` n `57` status `ready` deltaP `10.3556` edge `0.0848` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1185` n `52` status `ready` deltaP `3.8813` edge `0.1869` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9532` n `52` status `ready` deltaP `13.0629` edge `0.1743` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6371` n `57` status `ready` deltaP `11.0384` edge `0.0076` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.3336` n `57` status `ready` deltaP `5.6492` edge `0.019` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0146` n `52` status `ready` deltaP `1.841` edge `0.0333` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1181` n `57` status `ready` deltaP `3.5534` edge `0.0068` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3108` n `52` status `ready` deltaP `6.3321` edge `0.0137` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.7333` n `57` status `ready` deltaP `-4.4516` edge `-0.0362` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6569` n `52` status `ready` deltaP `-27.7244` edge `-0.0544` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4906` n `52` status `ready` deltaP `-26.97` edge `-0.197` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.8607` n `52` status `ready` deltaP `-34.8825` edge `-0.2288` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.757` n `52` status `ready` deltaP `-12.7804` edge `-0.3839` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.1633` n `52` status `ready` deltaP `-29.9813` edge `-0.3468` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.5872` n `52` status `ready` deltaP `-25.3205` edge `-1.5943` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
