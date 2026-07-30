# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T18:37:38.388329+00:00`
- Price records: `672`
- Market context records: `8436`
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

- `news_risk_high->unknown_24h` score `6256.9149` n `52` status `ready` deltaP `43.523` edge `521.1615` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.2063` n `52` status `ready` deltaP `23.0183` edge `0.3401` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2456` n `52` status `ready` deltaP `18.7356` edge `0.0931` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.121` n `52` status `ready` deltaP `18.75` edge `0.0708` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5008` n `52` status `ready` deltaP `12.0106` edge `0.0884` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.1879` n `52` status `ready` deltaP `8.5675` edge `0.0816` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1475` n `52` status `ready` deltaP `4.0338` edge `0.1896` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9753` n `52` status `ready` deltaP `13.3678` edge `0.1751` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1911` n `52` status `ready` deltaP `7.1396` edge `0.005` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0094` n `52` status `ready` deltaP `1.841` edge `0.0353` maxDD `-0.7433`
- `news_risk_high->index_1h` score `-0.0276` n `52` status `ready` deltaP `2.0498` edge `0.0129` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.321` n `52` status `ready` deltaP `6.1797` edge `0.0134` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4912` n `52` status `ready` deltaP `-0.1957` edge `0.0007` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.8782` n `52` status `ready` deltaP `-5.7232` edge `-0.0398` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6917` n `52` status `ready` deltaP `-27.7244` edge `-0.0573` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.5234` n `52` status `ready` deltaP `-27.2748` edge `-0.1977` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.7784` n `52` status `ready` deltaP `-34.7088` edge `-0.2231` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.6934` n `52` status `ready` deltaP `-12.7804` edge `-0.3786` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.9281` n `52` status `ready` deltaP `-28.766` edge `-0.3353` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-37.5815` n `52` status `ready` deltaP `-26.8563` edge `-1.1652` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
