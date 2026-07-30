# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T03:37:29.195980+00:00`
- Price records: `672`
- Market context records: `8370`
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

- `news_risk_high->unknown_24h` score `6252.1286` n `52` status `ready` deltaP `35.1896` edge `520.8182` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2036` n `52` status `ready` deltaP `25.3049` edge `0.4913` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8669` n `52` status `ready` deltaP `20.532` edge `0.1329` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6242` n `52` status `ready` deltaP `21.9512` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9116` n `52` status `ready` deltaP `8.3021` edge `0.2591` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.6446` n `52` status `ready` deltaP `11.5615` edge `0.0997` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.6339` n `52` status `ready` deltaP `12.6094` edge `0.0955` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3886` n `52` status `ready` deltaP `16.1117` edge `0.2098` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8474` n `52` status `ready` deltaP `7.7861` edge `0.0655` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2205` n `52` status `ready` deltaP `4.2953` edge `0.0186` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0774` n `52` status `ready` deltaP `5.3432` edge `0.0024` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1078` n `52` status `ready` deltaP `3.2474` edge `0.0097` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5457` n `52` status `ready` deltaP `3.2833` edge `0.0039` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1178` n `52` status `ready` deltaP `-8.2681` edge `-0.0428` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.4551` n `52` status `ready` deltaP `-24.9466` edge `-0.0561` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.2908` n `52` status `ready` deltaP `-28.4588` edge `-0.1408` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8068` n `52` status `ready` deltaP `-29.2566` edge `-0.2081` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.872` n `52` status `ready` deltaP `-9.3082` edge `-0.3333` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1285` n `52` status `ready` deltaP `-24.4258` edge `-0.2976` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0159` n `52` status `ready` deltaP `-23.2105` edge `-0.9757` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
