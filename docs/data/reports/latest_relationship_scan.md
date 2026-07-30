# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T14:37:30.949503+00:00`
- Price records: `672`
- Market context records: `8419`
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

- `news_risk_high->unknown_24h` score `6252.9517` n `52` status `ready` deltaP `40.9188` edge `520.8486` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.1306` n `52` status `ready` deltaP `24.2378` edge `0.409` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3846` n `52` status `ready` deltaP `19.4841` edge `0.0997` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2477` n `52` status `ready` deltaP `19.3598` edge `0.0773` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5752` n `52` status `ready` deltaP `12.31` edge `0.0926` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.4424` n `52` status `ready` deltaP `6.0155` edge `0.2142` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.4336` n `52` status `ready` deltaP `10.3639` edge `0.0901` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1686` n `52` status `ready` deltaP `15.0446` edge `0.1887` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.2531` n `52` status `ready` deltaP `3.8227` edge `0.0424` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1506` n `52` status `ready` deltaP `6.3911` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0683` n `52` status `ready` deltaP `3.0977` edge `0.0139` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3954` n `52` status `ready` deltaP `0.7025` edge `0.0027` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4457` n `52` status `ready` deltaP `4.5028` edge `0.0086` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9273` n `52` status `ready` deltaP `-6.322` edge `-0.0399` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7529` n `52` status `ready` deltaP `-27.7244` edge `-0.0624` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3063` n `52` status `ready` deltaP `-25.4456` edge `-0.1918` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.4834` n `52` status `ready` deltaP `-33.8408` edge `-0.2043` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.4559` n `52` status `ready` deltaP `-11.9124` edge `-0.3646` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.4707` n `52` status `ready` deltaP `-25.9883` edge `-0.3157` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0745` n `52` status `ready` deltaP `-24.0785` edge `-0.9748` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
