# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T23:22:37.047809+00:00`
- Price records: `672`
- Market context records: `8351`
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

- `news_risk_high->unknown_24h` score `6252.0362` n `52` status `ready` deltaP `35.1896` edge `520.8105` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6191` n `52` status `ready` deltaP `26.5244` edge `0.5178` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.892` n `52` status `ready` deltaP `20.6817` edge `0.134` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7756` n `52` status `ready` deltaP `23.0183` edge `0.0969` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.224` n `52` status `ready` deltaP `10.7411` edge `0.2829` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7838` n `52` status `ready` deltaP `13.5076` edge `0.102` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.7132` n `52` status `ready` deltaP `18.0934` edge `0.2382` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.7034` n `52` status `ready` deltaP `11.7112` edge `0.1036` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `0.8328` n `52` status `ready` deltaP `7.6337` edge `0.0653` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2337` n `52` status `ready` deltaP `4.445` edge `0.0187` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0549` n `52` status `ready` deltaP `4.8941` edge `0.0025` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2336` n `52` status `ready` deltaP `2.0498` edge `0.0072` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5426` n `52` status `ready` deltaP `3.2833` edge `0.0043` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2603` n `52` status `ready` deltaP `-9.7651` edge `-0.0447` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2374` n `52` status `ready` deltaP `-22.6896` edge `-0.053` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.6659` n `52` status `ready` deltaP `-25.5075` edge `-0.1084` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.0945` n `52` status `ready` deltaP `-31.848` edge `-0.2148` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9128` n `52` status `ready` deltaP `-9.3082` edge `-0.3367` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0731` n `52` status `ready` deltaP `-24.0785` edge `-0.2953` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.6457` n `52` status `ready` deltaP `-16.9871` edge `-1.3214` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
