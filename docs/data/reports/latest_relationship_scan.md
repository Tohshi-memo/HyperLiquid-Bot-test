# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T04:52:28.733794+00:00`
- Price records: `672`
- Market context records: `8376`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6252.1502` n `52` status `ready` deltaP `35.1896` edge `520.82` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2446` n `52` status `ready` deltaP `25.4573` edge `0.4937` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9639` n `52` status `ready` deltaP `21.2805` edge `0.136` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6218` n `52` status `ready` deltaP `21.9512` edge `0.0912` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8691` n `52` status `ready` deltaP `7.8447` edge `0.2567` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7118` n `52` status `ready` deltaP `13.2082` edge `0.098` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7033` n `52` status `ready` deltaP `12.0106` edge `0.1016` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3691` n `52` status `ready` deltaP `16.1117` edge `0.2073` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8366` n `52` status `ready` deltaP `7.7861` edge `0.0646` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2636` n `52` status `ready` deltaP `4.7444` edge `0.0192` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0953` n `52` status `ready` deltaP `5.6426` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0778` n `52` status `ready` deltaP `3.5468` edge `0.0102` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.503` n `52` status `ready` deltaP `4.0455` edge `0.0043` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1741` n `52` status `ready` deltaP `-8.8669` edge `-0.0435` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5426` n `52` status `ready` deltaP `-25.8146` edge `-0.0576` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.4851` n `52` status `ready` deltaP `-29.3269` edge `-0.1512` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7376` n `52` status `ready` deltaP `-28.6468` edge `-0.2064` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8684` n `52` status `ready` deltaP `-9.3082` edge `-0.333` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.2603` n `52` status `ready` deltaP `-25.2938` edge `-0.3028` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0819` n `52` status `ready` deltaP `-23.2105` edge `-0.9812` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
