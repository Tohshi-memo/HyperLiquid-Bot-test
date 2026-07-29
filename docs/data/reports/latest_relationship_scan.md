# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T19:22:34.039906+00:00`
- Price records: `672`
- Market context records: `8332`
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

- `news_risk_high->unknown_24h` score `6250.9267` n `52` status `ready` deltaP `35.016` edge `520.7192` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.933` n `52` status `ready` deltaP `24.8476` edge `0.4718` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6893` n `52` status `ready` deltaP `20.2326` edge `0.1201` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5287` n `52` status `ready` deltaP `21.3415` edge `0.0875` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0184` n `52` status `ready` deltaP `9.2167` edge `0.2667` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7394` n `52` status `ready` deltaP `13.5076` edge `0.0983` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.611` n `52` status `ready` deltaP `11.1124` edge `0.0999` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5533` n `52` status `ready` deltaP `17.1787` edge `0.2238` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9382` n `52` status `ready` deltaP `8.3959` edge `0.069` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.218` n `52` status `ready` deltaP `4.5947` edge `0.0164` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1452` n `52` status `ready` deltaP `6.5408` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1809` n `52` status `ready` deltaP `2.6486` edge `0.0076` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4011` n `52` status `ready` deltaP `5.5699` edge `0.0072` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2616` n `52` status `ready` deltaP `-9.6154` edge `-0.0458` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0105` n `52` status `ready` deltaP `-20.2591` edge `-0.0503` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.1077` n `52` status `ready` deltaP `-22.7297` edge `-0.0804` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2108` n `52` status `ready` deltaP `-32.7626` edge `-0.2184` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8252` n `52` status `ready` deltaP `-9.3082` edge `-0.3294` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1943` n `52` status `ready` deltaP `-24.0785` edge `-0.3054` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.2051` n `52` status `ready` deltaP `-16.6399` edge `-1.287` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
