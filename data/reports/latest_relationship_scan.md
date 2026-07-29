# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T13:22:28.801405+00:00`
- Price records: `672`
- Market context records: `8306`
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

- `news_risk_high->unknown_24h` score `6098.6518` n `53` status `ready` deltaP `35.3347` edge `508.0275` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.6427` n `53` status `ready` deltaP `25.0144` edge `0.4465` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8584` n `53` status `ready` deltaP `20.7406` edge `0.1308` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.529` n `53` status `ready` deltaP `21.6607` edge `0.0854` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0308` n `53` status `ready` deltaP `9.7101` edge `0.265` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8687` n `53` status `ready` deltaP `14.4193` edge `0.103` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.702` n `53` status `ready` deltaP `11.8744` edge `0.1024` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6146` n `53` status `ready` deltaP `18.0569` edge `0.2258` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2087` n `53` status `ready` deltaP `10.6823` edge `0.0763` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2926` n `53` status `ready` deltaP `5.1661` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1219` n `53` status `ready` deltaP `6.1236` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0734` n `53` status `ready` deltaP `4.8667` edge `0.014` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.479` n `53` status `ready` deltaP `4.1618` edge `0.0066` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.126` n `53` status `ready` deltaP `-8.4906` edge `-0.042` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0228` n `53` status `ready` deltaP `-20.4042` edge `-0.0493` maxDD `-5.326`
- `news_risk_high->metal_24h` score `-5.7557` n `53` status `ready` deltaP `-21.6752` edge `-0.0581` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9114` n `53` status `ready` deltaP `-31.2097` edge `-0.2038` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.2603` n `53` status `ready` deltaP `-7.6028` edge `-0.2937` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.108` n `53` status `ready` deltaP `-24.05` edge `-0.2984` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.8818` n `53` status `ready` deltaP `-14.7537` edge `-1.1893` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
