# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T08:52:25.511764+00:00`
- Price records: `672`
- Market context records: `8393`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5790`

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

- `news_risk_high->unknown_24h` score `6252.4859` n `52` status `ready` deltaP `36.9258` edge `520.8364` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6043` n `52` status `ready` deltaP `27.1341` edge `0.5125` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9723` n `52` status `ready` deltaP `21.4302` edge `0.1357` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7284` n `52` status `ready` deltaP `22.7134` edge `0.095` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9997` n `52` status `ready` deltaP `9.2167` edge `0.2643` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.713` n `52` status `ready` deltaP `13.2082` edge `0.0981` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6482` n `52` status `ready` deltaP `11.5615` edge `0.1` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4865` n `52` status `ready` deltaP `17.4836` edge `0.2132` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7578` n `52` status `ready` deltaP `7.1764` edge `0.0621` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2888` n `52` status `ready` deltaP `5.0438` edge `0.0193` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1125` n `52` status `ready` deltaP `5.942` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1869` n `52` status `ready` deltaP `2.6486` edge `0.0071` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4429` n `52` status `ready` deltaP `4.9601` edge `0.0059` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1226` n `52` status `ready` deltaP `-8.2681` edge `-0.0432` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6921` n `52` status `ready` deltaP `-27.2035` edge `-0.0608` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.7907` n `52` status `ready` deltaP `-29.8477` edge `-0.1732` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7556` n `52` status `ready` deltaP `-28.6468` edge `-0.2079` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.0738` n `52` status `ready` deltaP `-9.6554` edge `-0.3478` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3227` n `52` status `ready` deltaP `-25.2938` edge `-0.308` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.7699` n `52` status `ready` deltaP `-23.2105` edge `-0.9552` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
