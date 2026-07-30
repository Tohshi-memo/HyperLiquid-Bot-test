# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T18:07:34.759935+00:00`
- Price records: `672`
- Market context records: `8434`
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

- `news_risk_high->unknown_24h` score `6256.2979` n `52` status `ready` deltaP `43.1758` edge `521.1124` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.2051` n `52` status `ready` deltaP `23.0183` edge `0.34` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2516` n `52` status `ready` deltaP `18.7356` edge `0.0936` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1064` n `52` status `ready` deltaP `18.5976` edge `0.0706` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5212` n `52` status `ready` deltaP `12.1603` edge `0.0891` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2034` n `52` status `ready` deltaP `8.7172` edge `0.0819` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1743` n `52` status `ready` deltaP `4.3386` edge `0.191` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9745` n `52` status `ready` deltaP `13.3678` edge `0.175` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.174` n `52` status `ready` deltaP `6.8402` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0166` n `52` status `ready` deltaP `1.841` edge `0.0359` maxDD `-0.7433`
- `news_risk_high->index_1h` score `-0.0024` n `52` status `ready` deltaP `2.3492` edge `0.013` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3131` n `52` status `ready` deltaP `6.3321` edge `0.0134` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4661` n `52` status `ready` deltaP `0.1037` edge `0.0008` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.8758` n `52` status `ready` deltaP `-5.7232` edge `-0.0396` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7001` n `52` status `ready` deltaP `-27.7244` edge `-0.058` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.5064` n `52` status `ready` deltaP `-27.1224` edge `-0.1973` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.7628` n `52` status `ready` deltaP `-34.7088` edge `-0.2218` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.6682` n `52` status `ready` deltaP `-12.7804` edge `-0.3765` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.8763` n `52` status `ready` deltaP `-28.4188` edge `-0.3333` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-37.2922` n `52` status `ready` deltaP `-26.5091` edge `-1.1434` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
