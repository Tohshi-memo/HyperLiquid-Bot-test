# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T04:22:30.095969+00:00`
- Price records: `672`
- Market context records: `8373`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6252.1406` n `52` status `ready` deltaP `35.1896` edge `520.8192` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2192` n `52` status `ready` deltaP `25.3049` edge `0.4926` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9256` n `52` status `ready` deltaP `20.9811` edge `0.1348` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6364` n `52` status `ready` deltaP `22.1037` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8958` n `52` status `ready` deltaP `8.1496` edge `0.2581` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.6829` n `52` status `ready` deltaP `11.8609` edge `0.1009` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.6723` n `52` status `ready` deltaP `12.9088` edge `0.0967` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3785` n `52` status `ready` deltaP `16.1117` edge `0.2085` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8438` n `52` status `ready` deltaP `7.7861` edge `0.0652` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2492` n `52` status `ready` deltaP `4.5947` edge `0.019` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0782` n `52` status `ready` deltaP `5.3432` edge `0.0025` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.079` n `52` status `ready` deltaP `3.5468` edge `0.0101` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5283` n `52` status `ready` deltaP `3.5882` edge `0.0041` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1477` n `52` status `ready` deltaP `-8.5675` edge `-0.0433` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5064` n `52` status `ready` deltaP `-25.4674` edge `-0.0569` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.4105` n `52` status `ready` deltaP `-28.9797` edge `-0.1473` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7716` n `52` status `ready` deltaP `-28.9517` edge `-0.2072` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.866` n `52` status `ready` deltaP `-9.3082` edge `-0.3328` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.2061` n `52` status `ready` deltaP `-24.9466` edge `-0.3006` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0591` n `52` status `ready` deltaP `-23.2105` edge `-0.9793` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
