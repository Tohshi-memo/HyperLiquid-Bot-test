# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T09:22:31.977638+00:00`
- Price records: `672`
- Market context records: `8288`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5948.8265` n `54` status `ready` deltaP `33.7384` edge `495.5527` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.9277` n `54` status `ready` deltaP `25.621` edge `0.4662` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9551` n `54` status `ready` deltaP `21.2298` edge `0.1356` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6143` n `54` status `ready` deltaP `21.9625` edge `0.0905` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9903` n `54` status `ready` deltaP `9.4117` edge `0.2618` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8315` n `54` status `ready` deltaP `14.4045` edge `0.1` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5418` n `54` status `ready` deltaP `10.4569` edge `0.0985` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.535` n `54` status `ready` deltaP `17.2313` edge `0.2211` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9993` n `54` status `ready` deltaP `9.1294` edge `0.0692` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4124` n `54` status `ready` deltaP `6.4538` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1518` n `54` status `ready` deltaP `6.6977` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0964` n `54` status `ready` deltaP `3.1049` edge `0.0116` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4445` n `54` status `ready` deltaP `4.7651` edge `0.007` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0928` n `54` status `ready` deltaP `-8.3611` edge `-0.0401` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0392` n `54` status `ready` deltaP `-20.544` edge `-0.0486` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.6025` n `54` status `ready` deltaP `-20.2547` edge `-0.0548` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7068` n `54` status `ready` deltaP `-30.0474` edge `-0.1945` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.967` n `54` status `ready` deltaP `-5.9606` edge `-0.2802` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0355` n `54` status `ready` deltaP `-24.074` edge `-0.2922` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-31.8418` n `54` status `ready` deltaP `-11.8635` edge `-1.1219` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
