# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T23:07:30.917279+00:00`
- Price records: `672`
- Market context records: `8456`
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

- `news_risk_high->unknown_24h` score `6262.1633` n `52` status `ready` deltaP `44.0438` edge `521.5954` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8404` n `56` status `ready` deltaP `23.2796` edge `0.3912` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9932` n `61` status `ready` deltaP `21.2109` edge `0.1389` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1803` n `56` status `ready` deltaP `19.0113` edge `0.074` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6069` n `61` status `ready` deltaP `12.7515` edge `0.0923` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2387` n `61` status `ready` deltaP `9.4581` edge `0.0799` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.2375` n `56` status `ready` deltaP `5.9887` edge `0.1881` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.0358` n `56` status `ready` deltaP `14.5906` edge `0.1747` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.5778` n `61` status `ready` deltaP `10.371` edge `0.0071` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.5234` n `61` status `ready` deltaP `7.8114` edge `0.0204` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `0.099` n `56` status `ready` deltaP `3.2012` edge `0.0337` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.0392` n `61` status `ready` deltaP `4.5254` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.1373` n `56` status `ready` deltaP `9.2335` edge `0.0166` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.5115` n `61` status `ready` deltaP `-2.4443` edge `-0.0311` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6041` n `52` status `ready` deltaP `-27.7244` edge `-0.05` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.7355` n `56` status `ready` deltaP `-20.6664` edge `-0.1761` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.1194` n `52` status `ready` deltaP `-36.2713` edge `-0.2411` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.82` n `52` status `ready` deltaP `-12.954` edge `-0.388` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.6485` n `52` status `ready` deltaP `-31.891` edge `-0.3745` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.4383` n `52` status `ready` deltaP `-27.2302` edge `-1.6525` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
