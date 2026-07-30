# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T22:22:37.569532+00:00`
- Price records: `672`
- Market context records: `8453`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6261.2945` n `52` status `ready` deltaP `44.0438` edge `521.523` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.119` n `53` status `ready` deltaP `22.4229` edge `0.3368` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9866` n `60` status `ready` deltaP `20.9781` edge `0.1399` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.0481` n `53` status `ready` deltaP `18.1546` edge `0.0687` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.7262` n `60` status `ready` deltaP `13.9122` edge `0.0945` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2006` n `60` status `ready` deltaP `8.9521` edge `0.0801` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1027` n `53` status `ready` deltaP `4.2223` edge `0.1826` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.8927` n `53` status `ready` deltaP `12.874` edge `0.1678` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6435` n `60` status `ready` deltaP `11.1776` edge `0.0072` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4829` n `60` status `ready` deltaP `7.3054` edge `0.0204` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.051` n `53` status `ready` deltaP `1.5359` edge `0.0323` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.0722` n `60` status `ready` deltaP `4.1417` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.2907` n `53` status `ready` deltaP `6.6584` edge `0.0141` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.4561` n `60` status `ready` deltaP `-1.7066` edge `-0.0314` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6197` n `52` status `ready` deltaP `-27.7244` edge `-0.0513` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.2662` n `53` status `ready` deltaP `-24.9597` edge `-0.1917` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.0731` n `52` status `ready` deltaP `-36.0977` edge `-0.2384` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8044` n `52` status `ready` deltaP `-12.954` edge `-0.3867` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.5216` n `52` status `ready` deltaP `-31.3702` edge `-0.3674` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.2035` n `52` status `ready` deltaP `-26.7094` edge `-1.6364` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
