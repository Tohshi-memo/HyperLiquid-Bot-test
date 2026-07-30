# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T17:22:31.623587+00:00`
- Price records: `672`
- Market context records: `8431`
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

- `news_risk_high->unknown_24h` score `6255.3958` n `52` status `ready` deltaP `42.6549` edge `521.0407` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.2917` n `52` status `ready` deltaP `23.1707` edge `0.3462` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3103` n `52` status `ready` deltaP `19.1847` edge `0.0955` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1112` n `52` status `ready` deltaP `18.5976` edge `0.071` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5871` n `52` status `ready` deltaP `12.6094` edge `0.0916` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2598` n `52` status `ready` deltaP `9.1663` edge `0.0836` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.219` n `52` status `ready` deltaP `4.6435` edge `0.1947` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.991` n `52` status `ready` deltaP `13.5202` edge `0.1761` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1483` n `52` status `ready` deltaP `6.3911` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.064` n `52` status `ready` deltaP `2.2983` edge `0.0368` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.012` n `52` status `ready` deltaP `2.4989` edge `0.0132` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3392` n `52` status `ready` deltaP `5.8748` edge `0.0131` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4254` n `52` status `ready` deltaP `0.5528` edge `0.0012` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.9189` n `52` status `ready` deltaP `-6.1723` edge `-0.0402` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7145` n `52` status `ready` deltaP `-27.7244` edge `-0.0592` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4554` n `52` status `ready` deltaP `-26.6651` edge `-0.1961` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.7268` n `52` status `ready` deltaP `-34.7088` edge `-0.2188` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.6135` n `52` status `ready` deltaP `-12.6068` edge `-0.3731` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.795` n `52` status `ready` deltaP `-27.898` edge `-0.33` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-36.8353` n `52` status `ready` deltaP `-25.9883` edge `-1.1088` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
