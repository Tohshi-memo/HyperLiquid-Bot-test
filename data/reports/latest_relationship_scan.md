# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T22:37:26.490429+00:00`
- Price records: `672`
- Market context records: `8241`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `news_risk_high->unknown_24h` score `7957.3589` n `43` status `ready` deltaP `38.5417` edge `662.8563` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.382` n `54` status `ready` deltaP `27.1454` edge `0.4939` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1049` n `54` status `ready` deltaP `22.128` edge `0.1421` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7383` n `54` status `ready` deltaP `23.182` edge `0.0927` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3196` n `54` status `ready` deltaP `11.3934` edge `0.2908` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7548` n `54` status `ready` deltaP `14.2548` edge `0.0946` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6677` n `54` status `ready` deltaP `11.2054` edge `0.104` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3293` n `54` status `ready` deltaP `16.6215` edge `0.1988` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0094` n `54` status `ready` deltaP `9.5867` edge `0.067` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4794` n `54` status `ready` deltaP `7.2023` edge `0.0208` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.151` n `54` status `ready` deltaP `6.6977` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1371` n `54` status `ready` deltaP `2.8055` edge `0.0102` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5086` n `54` status `ready` deltaP `3.698` edge `0.0059` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1516` n `54` status `ready` deltaP `-8.8102` edge `-0.042` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.09` n `43` status `ready` deltaP `-18.6491` edge `-0.0449` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.8559` n `43` status `ready` deltaP `-21.4672` edge `-0.0934` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.9035` n `54` status `ready` deltaP `-32.7913` edge `-0.1926` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6719` n `43` status `ready` deltaP `-23.9624` edge `-0.3551` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.3628` n `43` status `ready` deltaP `-20.1752` edge `-0.4793` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.3024` n `43` status `ready` deltaP `-23.4415` edge `-1.2233` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
