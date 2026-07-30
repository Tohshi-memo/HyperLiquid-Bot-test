# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T15:07:30.663007+00:00`
- Price records: `672`
- Market context records: `8421`
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

- `news_risk_high->unknown_24h` score `6252.9867` n `52` status `ready` deltaP `41.266` edge `520.8492` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9214` n `52` status `ready` deltaP `23.9329` edge `0.3936` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2983` n `52` status `ready` deltaP `19.1847` edge `0.0945` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2041` n `52` status `ready` deltaP `19.0549` edge `0.0757` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.562` n `52` status `ready` deltaP `12.31` edge `0.0915` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.3923` n `52` status `ready` deltaP `5.7106` edge `0.2098` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.3856` n `52` status `ready` deltaP `10.0645` edge `0.0881` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1176` n `52` status `ready` deltaP `14.7397` edge `0.1842` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.2203` n `52` status `ready` deltaP `3.5178` edge `0.0417` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1421` n `52` status `ready` deltaP `6.2414` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0371` n `52` status `ready` deltaP `2.7983` edge `0.0133` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3834` n `52` status `ready` deltaP `0.8522` edge `0.0027` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4394` n `52` status `ready` deltaP `4.5028` edge `0.0094` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9321` n `52` status `ready` deltaP `-6.322` edge `-0.0403` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7457` n `52` status `ready` deltaP `-27.7244` edge `-0.0618` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3063` n `52` status `ready` deltaP `-25.4456` edge `-0.1918` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.546` n `52` status `ready` deltaP `-34.188` edge `-0.2072` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.4806` n `52` status `ready` deltaP `-12.086` edge `-0.3655` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.5344` n `52` status `ready` deltaP `-26.3355` edge `-0.3187` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.4059` n `52` status `ready` deltaP `-24.4258` edge `-1.0001` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
