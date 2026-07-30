# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T23:22:28.121778+00:00`
- Price records: `672`
- Market context records: `8458`
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

- `news_risk_high->unknown_24h` score `6262.4525` n `52` status `ready` deltaP `44.0438` edge `521.6195` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9664` n `57` status `ready` deltaP `23.5345` edge `0.4` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9944` n `61` status `ready` deltaP `21.2109` edge `0.139` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1958` n `57` status `ready` deltaP `19.2662` edge `0.0736` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5937` n `61` status `ready` deltaP `12.6018` edge `0.0922` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.2498` n `57` status `ready` deltaP `6.5255` edge `0.1861` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2255` n `61` status `ready` deltaP `9.3084` edge `0.0798` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.0627` n `57` status `ready` deltaP `15.0647` edge `0.175` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.5658` n `61` status `ready` deltaP `10.2213` edge `0.0071` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.5378` n `61` status `ready` deltaP `7.9611` edge `0.0206` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0079` n `57` status `ready` deltaP `2.1047` edge `0.0321` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.0392` n `61` status `ready` deltaP `4.5254` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.0901` n `57` status `ready` deltaP `10.0208` edge `0.0174` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.4983` n `61` status `ready` deltaP `-2.2946` edge `-0.031` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5993` n `52` status `ready` deltaP `-27.7244` edge `-0.0496` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.5675` n `57` status `ready` deltaP `-19.3463` edge `-0.1709` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.1429` n `52` status `ready` deltaP `-36.445` edge `-0.2419` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8248` n `52` status `ready` deltaP `-12.954` edge `-0.3884` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.6888` n `52` status `ready` deltaP `-32.0646` edge `-0.3767` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.5098` n `52` status `ready` deltaP `-27.4038` edge `-1.6573` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
