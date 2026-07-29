# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T10:37:29.535000+00:00`
- Price records: `672`
- Market context records: `8294`
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

- `news_risk_high->unknown_24h` score `5950.1547` n `54` status `ready` deltaP `34.6065` edge `495.6576` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.7723` n `54` status `ready` deltaP `25.1637` edge `0.4563` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9155` n `54` status `ready` deltaP `21.0801` edge `0.1333` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5466` n `54` status `ready` deltaP `21.5052` edge `0.0879` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9581` n `54` status `ready` deltaP `9.1069` edge `0.2597` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8639` n `54` status `ready` deltaP `14.7039` edge `0.1007` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5442` n `54` status `ready` deltaP `10.4569` edge `0.0987` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5319` n `54` status `ready` deltaP `17.2313` edge `0.2207` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0624` n `54` status `ready` deltaP `9.7391` edge `0.0704` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3848` n `54` status `ready` deltaP `6.1544` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1681` n `54` status `ready` deltaP `6.9971` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0545` n `54` status `ready` deltaP `3.554` edge `0.0121` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4619` n `54` status `ready` deltaP `4.4602` edge `0.0068` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.142` n `54` status `ready` deltaP `-8.8102` edge `-0.0412` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0392` n `54` status `ready` deltaP `-20.544` edge `-0.0486` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.7139` n `54` status `ready` deltaP `-21.1227` edge `-0.0583` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7688` n `54` status `ready` deltaP `-30.6572` edge `-0.1956` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.9154` n `54` status `ready` deltaP `-5.9606` edge `-0.2759` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.9596` n `54` status `ready` deltaP `-23.3796` edge `-0.2905` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-31.9654` n `54` status `ready` deltaP `-11.8635` edge `-1.1322` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
