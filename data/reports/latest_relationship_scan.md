# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T03:22:24.842878+00:00`
- Price records: `672`
- Market context records: `8369`
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

- `news_risk_high->unknown_24h` score `6252.125` n `52` status `ready` deltaP `35.1896` edge `520.8179` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1866` n `52` status `ready` deltaP `25.1524` edge `0.4909` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8417` n `52` status `ready` deltaP `20.3823` edge `0.1318` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6242` n `52` status `ready` deltaP `21.9512` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9226` n `52` status `ready` deltaP `8.4545` edge `0.2595` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.6446` n `52` status `ready` deltaP `11.5615` edge `0.0997` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.6363` n `52` status `ready` deltaP `12.6094` edge `0.0957` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3941` n `52` status `ready` deltaP `16.1117` edge `0.2105` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8426` n `52` status `ready` deltaP `7.7861` edge `0.0651` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2061` n `52` status `ready` deltaP `4.1456` edge `0.0184` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0697` n `52` status `ready` deltaP `5.1935` edge `0.0024` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1234` n `52` status `ready` deltaP `3.0977` edge `0.0094` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5544` n `52` status `ready` deltaP `3.1309` edge `0.0038` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1058` n `52` status `ready` deltaP `-8.1184` edge `-0.0428` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.4388` n `52` status `ready` deltaP `-24.773` edge `-0.0559` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.2529` n `52` status `ready` deltaP `-28.2852` edge `-0.1388` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8238` n `52` status `ready` deltaP `-29.409` edge `-0.2085` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8732` n `52` status `ready` deltaP `-9.3082` edge `-0.3334` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1189` n `52` status `ready` deltaP `-24.4258` edge `-0.2968` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0123` n `52` status `ready` deltaP `-23.2105` edge `-0.9754` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
