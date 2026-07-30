# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T17:07:24.512683+00:00`
- Price records: `672`
- Market context records: `8430`
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

- `news_risk_high->unknown_24h` score `6255.0963` n `52` status `ready` deltaP `42.4813` edge `521.0169` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.3591` n `52` status `ready` deltaP `23.3232` edge `0.3508` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3271` n `52` status `ready` deltaP `19.3344` edge `0.0959` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.116` n `52` status `ready` deltaP `18.5976` edge `0.0714` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5895` n `52` status `ready` deltaP `12.6094` edge `0.0918` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2765` n `52` status `ready` deltaP `9.316` edge `0.084` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.2291` n `52` status `ready` deltaP `4.6435` edge `0.196` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.0021` n `52` status `ready` deltaP `13.6726` edge `0.1765` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1491` n `52` status `ready` deltaP `6.3911` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0822` n `52` status `ready` deltaP `2.4508` edge `0.0373` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.0132` n `52` status `ready` deltaP `2.4989` edge `0.0133` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3495` n `52` status `ready` deltaP `5.7223` edge `0.0128` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4254` n `52` status `ready` deltaP `0.5528` edge `0.0012` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.9177` n `52` status `ready` deltaP `-6.1723` edge `-0.0401` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7169` n `52` status `ready` deltaP `-27.7244` edge `-0.0594` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.436` n `52` status `ready` deltaP `-26.5126` edge `-0.1955` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.716` n `52` status `ready` deltaP `-34.7088` edge `-0.2179` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.6003` n `52` status `ready` deltaP `-12.6068` edge `-0.372` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.768` n `52` status `ready` deltaP `-27.7244` edge `-0.3289` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-36.6822` n `52` status `ready` deltaP `-25.8146` edge `-1.0972` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
