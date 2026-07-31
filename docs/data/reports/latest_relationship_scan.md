# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T01:52:25.024238+00:00`
- Price records: `672`
- Market context records: `8469`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6265.3505` n `52` status `ready` deltaP `44.0438` edge `521.861` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.3196` n `60` status `ready` deltaP `23.1504` edge `0.432` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8205` n `61` status `ready` deltaP `20.3127` edge `0.1305` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2443` n `60` status `ready` deltaP `18.8821` edge `0.0802` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5781` n `61` status `ready` deltaP `12.6018` edge `0.0909` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.29` n `60` status `ready` deltaP `17.124` edge `0.1904` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.2888` n `60` status `ready` deltaP `7.246` edge `0.1863` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2399` n `61` status `ready` deltaP `9.4581` edge `0.08` maxDD `-1.1783`
- `news_risk_high->index_1h` score `0.4311` n `61` status `ready` deltaP `7.0629` edge `0.0177` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.4244` n `61` status `ready` deltaP `8.7243` edge `0.0053` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.008` n `60` status `ready` deltaP `11.128` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0176` n `61` status `ready` deltaP `4.6751` edge `0.0077` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.3557` n `60` status `ready` deltaP `-1.1179` edge `0.0246` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.4899` n `61` status `ready` deltaP `-2.2946` edge `-0.0303` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5753` n `52` status `ready` deltaP `-27.7244` edge `-0.0476` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4144` n `60` status `ready` deltaP `-18.5569` edge `-0.1634` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2372` n `52` status `ready` deltaP `-36.6186` edge `-0.2486` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.909` n `52` status `ready` deltaP `-13.3013` edge `-0.3931` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.1253` n `52` status `ready` deltaP `-33.8008` edge `-0.4015` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.1239` n `52` status `ready` deltaP `-29.1399` edge `-1.6969` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
