# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T19:37:26.780815+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4112`

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

- `market_context_high->unknown_1h` score `12012.7604` n `106` status `ready` deltaP `-0.6921` edge `1001.0878` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7474.0529` n `106` status `ready` deltaP `-2.2694` edge `622.8834` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1392.3981` n `31` status `ready` deltaP `4.1771` edge `116.0229` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1224.1945` n `31` status `ready` deltaP `3.9388` edge `101.9956` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0452` n `31` status `ready` deltaP `40.2734` edge `0.7835` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.8691` n `31` status `ready` deltaP `24.7787` edge `0.8276` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7005` n `31` status `ready` deltaP `14.9488` edge `0.9011` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.963` n `31` status `ready` deltaP `19.3886` edge `0.2197` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.506` n `31` status `ready` deltaP `36.4625` edge `0.0751` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6843` n `31` status `ready` deltaP `31.3937` edge `0.0229` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4369` n `31` status `ready` deltaP `9.2621` edge `0.2968` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0573` n `31` status `ready` deltaP `8.3639` edge `0.2437` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5756` n `31` status `ready` deltaP `21.1988` edge `0.1164` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.54` n `31` status `ready` deltaP `28.9839` edge `0.0321` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7895` n `31` status `ready` deltaP `17.6682` edge `0.0232` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0801` n `31` status `ready` deltaP `1.2314` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3036` n `106` status `ready` deltaP `2.9036` edge `0.0082` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4323` n `106` status `ready` deltaP `1.6919` edge `0.0014` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2346` n `106` status `ready` deltaP `-8.7759` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5204` n `106` status `ready` deltaP `-0.3164` edge `0.0044` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
