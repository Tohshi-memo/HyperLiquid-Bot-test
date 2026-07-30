# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T14:22:43.275268+00:00`
- Price records: `672`
- Market context records: `8417`
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

- `news_risk_high->unknown_24h` score `6252.9342` n `52` status `ready` deltaP `40.7452` edge `520.8483` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2508` n `52` status `ready` deltaP `24.3902` edge `0.418` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.4578` n `52` status `ready` deltaP `19.6338` edge `0.1048` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2731` n `52` status `ready` deltaP `19.5122` edge `0.0784` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.586` n `52` status `ready` deltaP `12.31` edge `0.0935` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.4667` n `52` status `ready` deltaP `6.1679` edge `0.2163` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.4611` n `52` status `ready` deltaP `10.5136` edge `0.0914` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1882` n `52` status `ready` deltaP `15.197` edge `0.1902` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.2689` n `52` status `ready` deltaP `3.9752` edge `0.0427` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1506` n `52` status `ready` deltaP `6.3911` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0875` n `52` status `ready` deltaP `3.2474` edge `0.0145` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3834` n `52` status `ready` deltaP `0.8522` edge `0.0027` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4488` n `52` status `ready` deltaP `4.5028` edge `0.0082` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9249` n `52` status `ready` deltaP `-6.322` edge `-0.0397` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7565` n `52` status `ready` deltaP `-27.7244` edge `-0.0627` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3099` n `52` status `ready` deltaP `-25.4456` edge `-0.1921` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.4515` n `52` status `ready` deltaP `-33.6672` edge `-0.2028` maxDD `-10.8302`
- `news_risk_high->index_24h` score `-12.4376` n `52` status `ready` deltaP `-25.8146` edge `-0.3141` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4511` n `52` status `ready` deltaP `-11.9124` edge `-0.3642` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.895` n `52` status `ready` deltaP `-23.9049` edge `-0.961` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
