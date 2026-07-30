# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T07:18:05.678100+00:00`
- Price records: `672`
- Market context records: `8386`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5790`

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

- `news_risk_high->unknown_24h` score `6252.3161` n `52` status `ready` deltaP `35.8841` edge `520.8292` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5631` n `52` status `ready` deltaP `26.8293` edge `0.5111` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.934` n `52` status `ready` deltaP `21.1308` edge `0.1345` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6798` n `52` status `ready` deltaP `22.2561` edge `0.094` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9611` n `52` status `ready` deltaP `8.7594` edge `0.2624` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6903` n `52` status `ready` deltaP `13.0585` edge `0.0972` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6518` n `52` status `ready` deltaP `11.5615` edge `0.1003` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4779` n `52` status `ready` deltaP `17.4836` edge `0.2121` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8294` n `52` status `ready` deltaP `7.7861` edge `0.064` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2756` n `52` status `ready` deltaP `4.8941` edge `0.0192` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1374` n `52` status `ready` deltaP `6.3911` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1174` n `52` status `ready` deltaP `3.2474` edge `0.0089` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4263` n `52` status `ready` deltaP `5.265` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1561` n `52` status `ready` deltaP `-8.5675` edge `-0.044` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.665` n `52` status `ready` deltaP `-27.0299` edge `-0.0597` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.6723` n `52` status `ready` deltaP `-29.3269` edge `-0.1668` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7472` n `52` status `ready` deltaP `-28.6468` edge `-0.2072` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9476` n `52` status `ready` deltaP `-9.3082` edge `-0.3396` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3251` n `52` status `ready` deltaP `-25.2938` edge `-0.3082` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.9583` n `52` status `ready` deltaP `-23.2105` edge `-0.9709` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
