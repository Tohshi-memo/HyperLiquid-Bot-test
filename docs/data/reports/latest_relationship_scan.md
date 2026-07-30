# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T20:51:31.076993+00:00`
- Price records: `672`
- Market context records: `8446`
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

- `news_risk_high->unknown_24h` score `6259.5821` n `52` status `ready` deltaP `44.0438` edge `521.3803` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.0717` n `52` status `ready` deltaP `22.8659` edge `0.3299` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9292` n `58` status `ready` deltaP `21.0717` edge `0.1345` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.0908` n `52` status `ready` deltaP `18.5976` edge `0.0693` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.8063` n `58` status `ready` deltaP `14.6139` edge `0.0965` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2642` n `58` status `ready` deltaP `9.5963` edge `0.0811` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1162` n `52` status `ready` deltaP `3.8813` edge `0.1866` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9359` n `52` status `ready` deltaP `12.9105` edge `0.1731` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6833` n `58` status `ready` deltaP `11.6147` edge `0.0076` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4025` n `58` status `ready` deltaP `6.3752` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0316` n `52` status `ready` deltaP `1.6886` edge `0.0329` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.18` n `58` status `ready` deltaP `2.8547` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3195` n `52` status `ready` deltaP `6.1797` edge `0.0136` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.6186` n `58` status `ready` deltaP `-3.4535` edge `-0.0333` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6485` n `52` status `ready` deltaP `-27.7244` edge `-0.0537` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4614` n `52` status `ready` deltaP `-26.6651` edge `-0.1966` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.9034` n `52` status `ready` deltaP `-35.0561` edge `-0.2312` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.769` n `52` status `ready` deltaP `-12.7804` edge `-0.3849` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.2499` n `52` status `ready` deltaP `-30.3285` edge `-0.3517` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.7277` n `52` status `ready` deltaP `-25.6677` edge `-1.6037` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
