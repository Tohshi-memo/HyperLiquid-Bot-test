# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T08:37:41.919637+00:00`
- Price records: `672`
- Market context records: `8392`
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

- `news_risk_high->unknown_24h` score `6252.46` n `52` status `ready` deltaP `36.7521` edge `520.8354` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6297` n `52` status `ready` deltaP `27.2866` edge `0.5136` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9711` n `52` status `ready` deltaP `21.4302` edge `0.1356` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7284` n `52` status `ready` deltaP `22.7134` edge `0.095` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0012` n `52` status `ready` deltaP `9.2167` edge `0.2645` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.713` n `52` status `ready` deltaP `13.2082` edge `0.0981` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6494` n `52` status `ready` deltaP `11.5615` edge `0.1001` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4881` n `52` status `ready` deltaP `17.4836` edge `0.2134` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.776` n `52` status `ready` deltaP `7.3288` edge `0.0626` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2888` n `52` status `ready` deltaP `5.0438` edge `0.0193` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1203` n `52` status `ready` deltaP `6.0917` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1833` n `52` status `ready` deltaP `2.6486` edge `0.0074` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4342` n `52` status `ready` deltaP `5.1126` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1358` n `52` status `ready` deltaP `-8.4178` edge `-0.0433` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6897` n `52` status `ready` deltaP `-27.2035` edge `-0.0606` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.7625` n `52` status `ready` deltaP `-29.6741` edge `-0.172` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7556` n `52` status `ready` deltaP `-28.6468` edge `-0.2079` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.057` n `52` status `ready` deltaP `-9.6554` edge `-0.3464` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3227` n `52` status `ready` deltaP `-25.2938` edge `-0.308` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.7963` n `52` status `ready` deltaP `-23.2105` edge `-0.9574` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
