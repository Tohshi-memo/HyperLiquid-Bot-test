# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T01:37:30.736842+00:00`
- Price records: `672`
- Market context records: `8362`
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

- `news_risk_high->unknown_24h` score `6252.0962` n `52` status `ready` deltaP `35.1896` edge `520.8155` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.3854` n `52` status `ready` deltaP `25.7622` edge `0.5034` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8656` n `52` status `ready` deltaP `20.6817` edge `0.1318` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7066` n `52` status `ready` deltaP `22.561` edge `0.0942` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0334` n `52` status `ready` deltaP `9.3691` edge `0.2676` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.743` n `52` status `ready` deltaP `13.2082` edge `0.1006` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6962` n `52` status `ready` deltaP `11.7112` edge `0.103` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5172` n `52` status `ready` deltaP `16.8739` edge `0.2212` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.828` n `52` status `ready` deltaP `7.6337` edge `0.0649` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2349` n `52` status `ready` deltaP `4.445` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0619` n `52` status `ready` deltaP `5.0438` edge `0.0024` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1725` n `52` status `ready` deltaP `2.6486` edge `0.0083` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5719` n `52` status `ready` deltaP `2.826` edge `0.0036` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1789` n `52` status `ready` deltaP `-8.8669` edge `-0.0439` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.32` n `52` status `ready` deltaP `-23.5577` edge `-0.0541` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.9889` n `52` status `ready` deltaP `-27.07` edge `-0.1249` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9391` n `52` status `ready` deltaP `-30.4761` edge `-0.211` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8864` n `52` status `ready` deltaP `-9.3082` edge `-0.3345` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0275` n `52` status `ready` deltaP `-24.0785` edge `-0.2915` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.9955` n `52` status `ready` deltaP `-23.2105` edge `-0.974` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
