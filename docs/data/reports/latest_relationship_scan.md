# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T03:07:39.295424+00:00`
- Price records: `672`
- Market context records: `8261`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7733.8166` n `44` status `ready` deltaP `39.0625` edge `644.2243` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1099` n `54` status `ready` deltaP `26.3832` edge `0.4763` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1889` n `54` status `ready` deltaP `22.4274` edge `0.1471` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7043` n `54` status `ready` deltaP `22.8771` edge `0.0919` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2247` n `54` status `ready` deltaP `10.7837` edge `0.2827` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8818` n `54` status `ready` deltaP `15.0033` edge `0.1002` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6797` n `54` status `ready` deltaP `11.0557` edge `0.106` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3434` n `54` status `ready` deltaP `16.6215` edge `0.2006` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1666` n `54` status `ready` deltaP `10.5013` edge `0.074` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.531` n `54` status `ready` deltaP `7.5017` edge `0.0231` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2156` n `54` status `ready` deltaP `7.8953` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0616` n `54` status `ready` deltaP `3.4043` edge `0.0125` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4151` n `54` status `ready` deltaP `5.3748` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1588` n `54` status `ready` deltaP `-8.8102` edge `-0.0426` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.165` n `44` status `ready` deltaP `-18.8605` edge `-0.0441` maxDD `-4.18`
- `news_risk_high->metal_24h` score `-5.6161` n `44` status `ready` deltaP `-19.7917` edge `-0.0799` maxDD `-10.1596`
- `news_risk_high->commodity_4h` score `-9.0755` n `54` status `ready` deltaP `-33.0962` edge `-0.2049` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.7313` n `44` status `ready` deltaP `-24.5739` edge `-0.3473` maxDD `-24.6521`
- `news_risk_high->commodity_24h` score `-13.4277` n `44` status `ready` deltaP `-15.0568` edge `-0.4355` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.1539` n `44` status `ready` deltaP `-23.7058` edge `-1.1812` maxDD `-107.8866`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
