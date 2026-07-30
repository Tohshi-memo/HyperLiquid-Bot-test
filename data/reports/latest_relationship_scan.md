# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T22:37:29.165812+00:00`
- Price records: `672`
- Market context records: `8454`
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

- `news_risk_high->unknown_24h` score `6261.5837` n `52` status `ready` deltaP `44.0438` edge `521.5471` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.3916` n `54` status `ready` deltaP `22.7247` edge `0.3575` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9686` n `60` status `ready` deltaP `20.8284` edge `0.1394` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1035` n `54` status `ready` deltaP `18.4564` edge `0.0713` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.7094` n `60` status `ready` deltaP `13.7625` edge `0.0941` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.1814` n `60` status `ready` deltaP `8.8024` edge `0.0795` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1589` n `54` status `ready` deltaP `4.8386` edge `0.1857` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9499` n `54` status `ready` deltaP `13.4203` edge `0.1715` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6435` n `60` status `ready` deltaP `11.1776` edge `0.0072` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4697` n `60` status `ready` deltaP `7.1557` edge `0.0203` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0009` n `54` status `ready` deltaP `2.1172` edge `0.0326` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.0842` n `60` status `ready` deltaP `3.992` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.2363` n `54` status `ready` deltaP `7.5542` edge `0.0151` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.4692` n `60` status `ready` deltaP `-1.8563` edge `-0.0315` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6149` n `52` status `ready` deltaP `-27.7244` edge `-0.0509` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.081` n `54` status `ready` deltaP `-23.4699` edge `-0.1862` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.1002` n `52` status `ready` deltaP `-36.2713` edge `-0.2395` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8092` n `52` status `ready` deltaP `-12.954` edge `-0.3871` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.5655` n `52` status `ready` deltaP `-31.5438` edge `-0.3699` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.2822` n `52` status `ready` deltaP `-26.883` edge `-1.6418` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
