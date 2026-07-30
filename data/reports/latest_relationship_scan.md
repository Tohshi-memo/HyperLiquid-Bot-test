# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T03:52:30.824508+00:00`
- Price records: `672`
- Market context records: `8371`
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

- `news_risk_high->unknown_24h` score `6252.1334` n `52` status `ready` deltaP `35.1896` edge `520.8186` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2036` n `52` status `ready` deltaP `25.3049` edge `0.4913` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.886` n `52` status `ready` deltaP `20.6817` edge `0.1335` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.623` n `52` status `ready` deltaP `21.9512` edge `0.0913` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8997` n `52` status `ready` deltaP `8.1496` edge `0.2586` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.6458` n `52` status `ready` deltaP `11.5615` edge `0.0998` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.6315` n `52` status `ready` deltaP `12.6094` edge `0.0953` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3832` n `52` status `ready` deltaP `16.1117` edge `0.2091` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8486` n `52` status `ready` deltaP `7.7861` edge `0.0656` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2337` n `52` status `ready` deltaP `4.445` edge `0.0187` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0774` n `52` status `ready` deltaP `5.3432` edge `0.0024` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0934` n `52` status `ready` deltaP `3.3971` edge `0.0099` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.537` n `52` status `ready` deltaP `3.4357` edge `0.004` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.119` n `52` status `ready` deltaP `-8.2681` edge `-0.0429` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.4714` n `52` status `ready` deltaP `-25.1202` edge `-0.0563` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.3311` n `52` status `ready` deltaP `-28.6325` edge `-0.143` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.791` n `52` status `ready` deltaP `-29.1041` edge `-0.2078` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8696` n `52` status `ready` deltaP `-9.3082` edge `-0.3331` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1544` n `52` status `ready` deltaP `-24.5994` edge `-0.2986` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0291` n `52` status `ready` deltaP `-23.2105` edge `-0.9768` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
