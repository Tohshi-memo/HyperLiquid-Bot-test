# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T08:07:31.375118+00:00`
- Price records: `672`
- Market context records: `8390`
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

- `news_risk_high->unknown_24h` score `6252.4046` n `52` status `ready` deltaP `36.4049` edge `520.8331` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6369` n `52` status `ready` deltaP `27.2866` edge `0.5142` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9699` n `52` status `ready` deltaP `21.4302` edge `0.1355` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7272` n `52` status `ready` deltaP `22.7134` edge `0.0949` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9973` n `52` status `ready` deltaP `9.2167` edge `0.264` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6903` n `52` status `ready` deltaP `13.0585` edge `0.0972` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.629` n `52` status `ready` deltaP `11.4118` edge `0.0994` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4865` n `52` status `ready` deltaP `17.4836` edge `0.2132` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8088` n `52` status `ready` deltaP `7.6337` edge `0.0633` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2912` n `52` status `ready` deltaP `5.0438` edge `0.0195` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1374` n `52` status `ready` deltaP `6.3911` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1641` n `52` status `ready` deltaP `2.7983` edge `0.008` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4255` n `52` status `ready` deltaP `5.265` edge `0.0061` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1394` n `52` status `ready` deltaP `-8.4178` edge `-0.0436` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6849` n `52` status `ready` deltaP `-27.2035` edge `-0.0602` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.7095` n `52` status `ready` deltaP `-29.3269` edge `-0.1699` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7532` n `52` status `ready` deltaP `-28.6468` edge `-0.2077` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9956` n `52` status `ready` deltaP `-9.3082` edge `-0.3436` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3215` n `52` status `ready` deltaP `-25.2938` edge `-0.3079` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.8563` n `52` status `ready` deltaP `-23.2105` edge `-0.9624` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
