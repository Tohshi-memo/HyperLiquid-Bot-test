# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T05:52:24.769978+00:00`
- Price records: `672`
- Market context records: `8380`
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

- `news_risk_high->unknown_24h` score `6252.1989` n `52` status `ready` deltaP `35.3633` edge `520.8229` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4086` n `52` status `ready` deltaP `26.0671` edge `0.5033` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9843` n `52` status `ready` deltaP `21.4302` edge `0.1367` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6496` n `52` status `ready` deltaP `22.1037` edge `0.0925` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8879` n `52` status `ready` deltaP `7.9972` edge `0.2581` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7298` n `52` status `ready` deltaP `13.3579` edge `0.0985` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6806` n `52` status `ready` deltaP `11.7112` edge `0.1017` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4054` n `52` status `ready` deltaP `16.569` edge `0.2089` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8402` n `52` status `ready` deltaP `7.7861` edge `0.0649` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2912` n `52` status `ready` deltaP `5.0438` edge `0.0195` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1039` n `52` status `ready` deltaP `5.7923` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0635` n `52` status `ready` deltaP `3.6965` edge `0.0104` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4658` n `52` status `ready` deltaP `4.6553` edge `0.005` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1873` n `52` status `ready` deltaP `-8.8669` edge `-0.0446` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6101` n `52` status `ready` deltaP `-26.5091` edge `-0.0586` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.5679` n `52` status `ready` deltaP `-29.3269` edge `-0.1581` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7376` n `52` status `ready` deltaP `-28.6468` edge `-0.2064` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.89` n `52` status `ready` deltaP `-9.3082` edge `-0.3348` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.2975` n `52` status `ready` deltaP `-25.2938` edge `-0.3059` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0471` n `52` status `ready` deltaP `-23.2105` edge `-0.9783` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
