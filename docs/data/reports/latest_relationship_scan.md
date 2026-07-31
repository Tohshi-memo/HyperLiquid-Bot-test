# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T00:37:28.948054+00:00`
- Price records: `672`
- Market context records: `8463`
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

- `news_risk_high->unknown_24h` score `6263.9033` n `52` status `ready` deltaP `44.0438` edge `521.7404` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9284` n `58` status `ready` deltaP `23.1655` edge `0.3993` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8721` n `61` status `ready` deltaP `20.4624` edge `0.1338` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1339` n `58` status `ready` deltaP `18.8972` edge `0.0709` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5661` n `61` status `ready` deltaP `12.4521` edge `0.0909` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.3064` n `58` status `ready` deltaP `7.3434` edge `0.1879` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2052` n `61` status `ready` deltaP `9.1587` edge `0.0791` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1561` n `58` status `ready` deltaP `15.9745` edge `0.1809` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.4963` n `61` status `ready` deltaP `9.4728` edge `0.0063` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4694` n `61` status `ready` deltaP `7.3623` edge `0.0189` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.026` n `61` status `ready` deltaP `4.6751` edge `0.007` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.0896` n `58` status `ready` deltaP `10.1661` edge `0.0165` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.1372` n `58` status `ready` deltaP `0.8936` edge `0.0294` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.5115` n `61` status `ready` deltaP `-2.4443` edge `-0.0311` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5849` n `52` status `ready` deltaP `-27.7244` edge `-0.0484` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4048` n `58` status `ready` deltaP `-18.0772` edge `-0.1658` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2072` n `52` status `ready` deltaP `-36.6186` edge `-0.2461` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8898` n `52` status `ready` deltaP `-13.3013` edge `-0.3915` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.9118` n `52` status `ready` deltaP `-32.9327` edge `-0.3895` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.8433` n `52` status `ready` deltaP `-28.2719` edge `-1.6793` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
