# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T15:37:28.811593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4026`

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

- `market_context_high->unknown_1h` score `12031.5332` n `106` status `ready` deltaP `-0.5424` edge `1002.6512` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7505.8513` n `106` status `ready` deltaP `-2.5742` edge `625.5353` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1411.1709` n `31` status `ready` deltaP `4.3268` edge `117.5863` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1255.9929` n `31` status `ready` deltaP `3.634` edge `104.6475` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9066` n `31` status `ready` deltaP `39.8161` edge `0.775` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.636` n `31` status `ready` deltaP `23.5592` edge `0.8163` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6325` n `31` status `ready` deltaP `14.7964` edge `0.8934` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9271` n `31` status `ready` deltaP `19.2389` edge `0.2177` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4768` n `31` status `ready` deltaP `36.1576` edge `0.0747` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6819` n `31` status `ready` deltaP `31.3937` edge `0.0227` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4213` n `31` status `ready` deltaP `9.1124` edge `0.2958` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0495` n `31` status `ready` deltaP `8.3639` edge `0.2427` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5337` n `31` status `ready` deltaP `20.5891` edge `0.1151` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.4878` n `31` status `ready` deltaP `28.0857` edge `0.0314` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.6668` n `31` status `ready` deltaP `15.534` edge `0.0217` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0849` n `31` status `ready` deltaP `1.2314` edge `0.0109` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3558` n `106` status `ready` deltaP `2.0054` edge `0.0075` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4347` n `106` status `ready` deltaP `1.6919` edge `0.0012` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2478` n `106` status `ready` deltaP `-8.9256` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5267` n `106` status `ready` deltaP `-0.3164` edge `0.0036` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
