# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T11:07:26.767981+00:00`
- Price records: `672`
- Market context records: `8403`
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

- `news_risk_high->unknown_24h` score `6252.6601` n `52` status `ready` deltaP `38.4883` edge `520.8405` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1826` n `52` status `ready` deltaP `25.7622` edge `0.4865` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8524` n `52` status `ready` deltaP `20.8314` edge `0.1297` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5623` n `52` status `ready` deltaP `21.3415` edge `0.0903` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.7951` n `52` status `ready` deltaP `7.9972` edge `0.2462` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6855` n `52` status `ready` deltaP `12.9088` edge `0.0978` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.617` n `52` status `ready` deltaP `11.4118` edge `0.0984` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3608` n `52` status `ready` deltaP `16.4165` edge `0.2042` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.5305` n `52` status `ready` deltaP `5.8044` edge `0.0523` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2432` n `52` status `ready` deltaP `4.5947` edge `0.0185` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0899` n `52` status `ready` deltaP `5.4929` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.278` n `52` status `ready` deltaP `1.7504` edge `0.0055` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4841` n `52` status `ready` deltaP `4.1979` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0028` n `52` status `ready` deltaP `-7.0705` edge `-0.0412` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7565` n `52` status `ready` deltaP `-27.7244` edge `-0.0627` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.0585` n `52` status `ready` deltaP `-31.4102` edge `-0.1851` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.5812` n `52` status `ready` deltaP `-27.4273` edge `-0.2015` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.3145` n `52` status `ready` deltaP `-11.0443` edge `-0.3586` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3287` n `52` status `ready` deltaP `-25.2938` edge `-0.3085` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.5647` n `52` status `ready` deltaP `-23.2105` edge `-0.9381` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
