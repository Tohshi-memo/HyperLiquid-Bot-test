# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T09:07:47.746046+00:00`
- Price records: `672`
- Market context records: `8394`
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

- `news_risk_high->unknown_24h` score `6252.5034` n `52` status `ready` deltaP `37.0994` edge `520.8367` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5657` n `52` status `ready` deltaP `26.9817` edge `0.5103` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9687` n `52` status `ready` deltaP `21.4302` edge `0.1354` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7126` n `52` status `ready` deltaP `22.561` edge `0.0947` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.995` n `52` status `ready` deltaP `9.2167` edge `0.2637` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7106` n `52` status `ready` deltaP `13.2082` edge `0.0979` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6446` n `52` status `ready` deltaP `11.5615` edge `0.0997` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4818` n `52` status `ready` deltaP `17.4836` edge `0.2126` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.736` n `52` status `ready` deltaP `7.0239` edge `0.0613` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2876` n `52` status `ready` deltaP `5.0438` edge `0.0192` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1047` n `52` status `ready` deltaP `5.7923` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1893` n `52` status `ready` deltaP `2.6486` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4509` n `52` status `ready` deltaP `4.8077` edge `0.0059` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1082` n `52` status `ready` deltaP `-8.1184` edge `-0.043` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6945` n `52` status `ready` deltaP `-27.2035` edge `-0.061` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.8202` n `52` status `ready` deltaP `-30.0213` edge `-0.1745` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.752` n `52` status `ready` deltaP `-28.6468` edge `-0.2076` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.087` n `52` status `ready` deltaP `-9.6554` edge `-0.3489` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3227` n `52` status `ready` deltaP `-25.2938` edge `-0.308` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.7387` n `52` status `ready` deltaP `-23.2105` edge `-0.9526` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
