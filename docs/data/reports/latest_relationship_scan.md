# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T01:10:59.562340+00:00`
- Price records: `672`
- Market context records: `8360`
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

- `news_risk_high->unknown_24h` score `6252.0938` n `52` status `ready` deltaP `35.1896` edge `520.8153` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5094` n `52` status `ready` deltaP `26.0671` edge `0.5117` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9076` n `52` status `ready` deltaP `20.8314` edge `0.1343` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.749` n `52` status `ready` deltaP `22.8659` edge `0.0957` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0843` n `52` status `ready` deltaP `9.674` edge `0.2721` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7922` n `52` status `ready` deltaP `13.5076` edge `0.1027` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7285` n `52` status `ready` deltaP `11.8609` edge `0.1047` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5728` n `52` status `ready` deltaP `17.1787` edge `0.2263` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8328` n `52` status `ready` deltaP `7.6337` edge `0.0653` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.254` n `52` status `ready` deltaP `4.5947` edge `0.0194` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0798` n `52` status `ready` deltaP `5.3432` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1689` n `52` status `ready` deltaP `2.6486` edge `0.0086` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5632` n `52` status `ready` deltaP `2.9784` edge `0.0037` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1909` n `52` status `ready` deltaP `-9.0166` edge `-0.0439` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2886` n `52` status `ready` deltaP `-23.2105` edge `-0.0538` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.9143` n `52` status `ready` deltaP `-26.7227` edge `-0.121` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9731` n `52` status `ready` deltaP `-30.7809` edge `-0.2118` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8948` n `52` status `ready` deltaP `-9.3082` edge `-0.3352` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0203` n `52` status `ready` deltaP `-24.0785` edge `-0.2909` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.9013` n `52` status `ready` deltaP `-16.9871` edge `-1.3427` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
