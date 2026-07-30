# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T09:22:29.309501+00:00`
- Price records: `672`
- Market context records: `8395`
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

- `news_risk_high->unknown_24h` score `6252.5233` n `52` status `ready` deltaP `37.273` edge `520.8372` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5199` n `52` status `ready` deltaP `26.8293` edge `0.5075` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9627` n `52` status `ready` deltaP `21.4302` edge `0.1349` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6956` n `52` status `ready` deltaP `22.4085` edge `0.0943` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9715` n `52` status `ready` deltaP `9.0643` edge `0.2617` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.707` n `52` status `ready` deltaP `13.2082` edge `0.0976` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6386` n `52` status `ready` deltaP `11.5615` edge `0.0992` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4637` n `52` status `ready` deltaP `17.3312` edge `0.2113` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.713` n `52` status `ready` deltaP `6.8715` edge `0.0604` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2876` n `52` status `ready` deltaP `5.0438` edge `0.0192` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0961` n `52` status `ready` deltaP `5.6426` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2037` n `52` status `ready` deltaP `2.4989` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4596` n `52` status `ready` deltaP `4.6553` edge `0.0058` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0914` n `52` status `ready` deltaP `-7.9687` edge `-0.0426` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.712` n `52` status `ready` deltaP `-27.3771` edge `-0.0613` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.8485` n `52` status `ready` deltaP `-30.195` edge `-0.1757` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7314` n `52` status `ready` deltaP `-28.4944` edge `-0.2069` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.1164` n `52` status `ready` deltaP `-9.829` edge `-0.3502` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3227` n `52` status `ready` deltaP `-25.2938` edge `-0.308` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.7099` n `52` status `ready` deltaP `-23.2105` edge `-0.9502` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
