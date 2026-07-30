# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T21:07:37.706332+00:00`
- Price records: `672`
- Market context records: `8447`
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

- `news_risk_high->unknown_24h` score `6259.8665` n `52` status `ready` deltaP `44.0438` edge `521.404` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.0283` n `52` status `ready` deltaP `22.7134` edge `0.3273` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9125` n `58` status `ready` deltaP `20.922` edge `0.1341` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.075` n `52` status `ready` deltaP `18.4451` edge `0.069` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.8063` n `58` status `ready` deltaP `14.6139` edge `0.0965` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2642` n `58` status `ready` deltaP `9.5963` edge `0.0811` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1012` n `52` status `ready` deltaP `3.7289` edge `0.1857` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9178` n `52` status `ready` deltaP `12.758` edge `0.1718` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6713` n `58` status `ready` deltaP `11.465` edge `0.0076` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4025` n `58` status `ready` deltaP `6.3752` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0462` n `52` status `ready` deltaP `1.5361` edge `0.0327` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1668` n `58` status `ready` deltaP `3.0044` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3195` n `52` status `ready` deltaP `6.1797` edge `0.0136` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.6186` n `58` status `ready` deltaP `-3.4535` edge `-0.0333` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6437` n `52` status `ready` deltaP `-27.7244` edge `-0.0533` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4468` n `52` status `ready` deltaP `-26.5126` edge `-0.1964` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.9317` n `52` status `ready` deltaP `-35.2297` edge `-0.2324` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7738` n `52` status `ready` deltaP `-12.7804` edge `-0.3853` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.2938` n `52` status `ready` deltaP `-30.5021` edge `-0.3542` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.816` n `52` status `ready` deltaP `-25.8413` edge `-1.6099` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
