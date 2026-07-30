# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T23:38:00.744808+00:00`
- Price records: `672`
- Market context records: `8459`
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

- `news_risk_high->unknown_24h` score `6262.7429` n `52` status `ready` deltaP `44.0438` edge `521.6437` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.1272` n `58` status `ready` deltaP `23.7752` edge `0.4118` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9776` n `61` status `ready` deltaP `21.0612` edge `0.1386` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2199` n `58` status `ready` deltaP `19.5069` edge `0.074` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5757` n `61` status `ready` deltaP `12.4521` edge `0.0917` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.2835` n `58` status `ready` deltaP `7.0385` edge `0.187` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.21` n `61` status `ready` deltaP `9.1587` edge `0.0795` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1144` n `58` status `ready` deltaP `15.5172` edge `0.1786` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.5526` n `61` status `ready` deltaP `10.0716` edge `0.007` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.5378` n `61` status `ready` deltaP `7.9611` edge `0.0206` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.0392` n `61` status `ready` deltaP `4.5254` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.0469` n `58` status `ready` deltaP `10.7759` edge `0.0179` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.113` n `58` status `ready` deltaP `1.046` edge `0.0304` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.4863` n `61` status `ready` deltaP `-2.1449` edge `-0.031` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5957` n `52` status `ready` deltaP `-27.7244` edge `-0.0493` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4024` n `58` status `ready` deltaP `-18.0772` edge `-0.1656` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.1664` n `52` status `ready` deltaP `-36.6186` edge `-0.2427` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8308` n `52` status `ready` deltaP `-12.954` edge `-0.3889` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.7303` n `52` status `ready` deltaP `-32.2383` edge `-0.379` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.5849` n `52` status `ready` deltaP `-27.5774` edge `-1.6624` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
