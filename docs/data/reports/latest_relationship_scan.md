# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T13:37:38.346959+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4008`

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

- `market_context_high->unknown_1h` score `12041.8172` n `106` status `ready` deltaP `-0.3927` edge `1003.5072` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7515.7993` n `106` status `ready` deltaP `-2.5742` edge `626.3643` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1421.4549` n `31` status `ready` deltaP `4.4765` edge `118.4423` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1391.9959` n `30` status `ready` deltaP `3.5265` edge `115.9818` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0044` n `30` status `ready` deltaP `39.5833` edge `0.7847` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.9117` n `30` status `ready` deltaP `22.8963` edge `0.8437` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `7.0897` n `30` status `ready` deltaP `16.8394` edge `0.9384` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0109` n `31` status `ready` deltaP `19.9874` edge `0.2197` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4278` n `30` status `ready` deltaP `35.6199` edge `0.0742` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7082` n `31` status `ready` deltaP `31.6931` edge `0.0229` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5328` n `31` status `ready` deltaP `9.8609` edge `0.3051` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1235` n `31` status `ready` deltaP `8.6633` edge `0.2502` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6611` n `30` status `ready` deltaP `22.7845` edge `0.1168` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5151` n `31` status `ready` deltaP `28.5348` edge `0.0319` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7515` n `30` status `ready` deltaP `17.0122` edge `0.0227` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.1184` n `31` status `ready` deltaP `0.7823` edge `0.0111` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3285` n `106` status `ready` deltaP `2.4545` edge `0.008` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4083` n `106` status `ready` deltaP `1.9913` edge `0.0014` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2119` n `106` status `ready` deltaP `-8.4765` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5267` n `106` status `ready` deltaP `-0.3164` edge `0.0036` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
