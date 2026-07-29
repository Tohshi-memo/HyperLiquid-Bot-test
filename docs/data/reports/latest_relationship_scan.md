# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T13:37:39.961574+00:00`
- Price records: `672`
- Market context records: `8307`
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

- `news_risk_high->unknown_24h` score `6098.8534` n `53` status `ready` deltaP `35.3347` edge `508.0443` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.6861` n `53` status `ready` deltaP `25.1668` edge `0.4491` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8776` n `53` status `ready` deltaP `20.7406` edge `0.1324` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5338` n `53` status `ready` deltaP `21.6607` edge `0.0858` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0551` n `53` status `ready` deltaP `9.8626` edge `0.2671` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8735` n `53` status `ready` deltaP `14.4193` edge `0.1034` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.708` n `53` status `ready` deltaP `11.8744` edge `0.1029` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6381` n `53` status `ready` deltaP `18.2093` edge `0.2278` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2245` n `53` status `ready` deltaP `10.8347` edge `0.0766` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2938` n `53` status `ready` deltaP `5.1661` edge `0.0189` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1219` n `53` status `ready` deltaP `6.1236` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0758` n `53` status `ready` deltaP `4.8667` edge `0.0142` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4877` n `53` status `ready` deltaP `4.0094` edge `0.0065` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1272` n `53` status `ready` deltaP `-8.4906` edge `-0.0421` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0228` n `53` status `ready` deltaP `-20.4042` edge `-0.0493` maxDD `-5.326`
- `news_risk_high->metal_24h` score `-5.7828` n `53` status `ready` deltaP `-21.8488` edge `-0.0592` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9332` n `53` status `ready` deltaP `-31.3621` edge `-0.2046` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.2507` n `53` status `ready` deltaP `-7.6028` edge `-0.2929` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.108` n `53` status `ready` deltaP `-24.05` edge `-0.2984` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.9329` n `53` status `ready` deltaP `-14.9273` edge `-1.1924` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
