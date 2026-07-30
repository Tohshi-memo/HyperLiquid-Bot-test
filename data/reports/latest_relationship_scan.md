# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T17:52:26.388341+00:00`
- Price records: `672`
- Market context records: `8433`
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

- `news_risk_high->unknown_24h` score `6255.996` n `52` status `ready` deltaP `43.0021` edge `521.0884` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.2341` n `52` status `ready` deltaP `23.1707` edge `0.3414` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2719` n `52` status `ready` deltaP `18.8853` edge `0.0943` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1076` n `52` status `ready` deltaP `18.5976` edge `0.0707` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5488` n `52` status `ready` deltaP `12.31` edge `0.0904` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.225` n `52` status `ready` deltaP `8.8669` edge `0.0827` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1939` n `52` status `ready` deltaP `4.4911` edge `0.1925` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9784` n `52` status `ready` deltaP `13.3678` edge `0.1755` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1647` n `52` status `ready` deltaP `6.6905` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0324` n `52` status `ready` deltaP `1.9934` edge `0.0362` maxDD `-0.7433`
- `news_risk_high->index_1h` score `-0.0012` n `52` status `ready` deltaP `2.3492` edge `0.0131` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3218` n `52` status `ready` deltaP `6.1797` edge `0.0133` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4517` n `52` status `ready` deltaP `0.2534` edge `0.001` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.889` n `52` status `ready` deltaP `-5.8729` edge `-0.0397` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7049` n `52` status `ready` deltaP `-27.7244` edge `-0.0584` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4894` n `52` status `ready` deltaP `-26.97` edge `-0.1969` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.7556` n `52` status `ready` deltaP `-34.7088` edge `-0.2212` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.6562` n `52` status `ready` deltaP `-12.7804` edge `-0.3755` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.8516` n `52` status `ready` deltaP `-28.2452` edge `-0.3324` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-37.1535` n `52` status `ready` deltaP `-26.3355` edge `-1.133` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
