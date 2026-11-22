# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T16:37:31.995962+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4036`

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

- `market_context_high->unknown_1h` score `12025.772` n `106` status `ready` deltaP `-0.8418` edge `1002.1731` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7500.1573` n `106` status `ready` deltaP `-2.5742` edge `625.0608` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1405.4098` n `31` status `ready` deltaP `4.0274` edge `117.1082` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1250.2989` n `31` status `ready` deltaP `3.634` edge `104.173` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9732` n `31` status `ready` deltaP `40.2734` edge `0.7775` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.6374` n `31` status `ready` deltaP `23.7116` edge `0.8154` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6144` n `31` status `ready` deltaP `14.644` edge `0.8921` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9894` n `31` status `ready` deltaP `19.8377` edge `0.2189` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4768` n `31` status `ready` deltaP `36.1576` edge `0.0747` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.8428` edge `0.0229` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3816` n `31` status `ready` deltaP `8.6633` edge `0.2937` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.03` n `31` status `ready` deltaP `8.2142` edge `0.2412` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5361` n `31` status `ready` deltaP `20.5891` edge `0.1154` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.48` n `31` status `ready` deltaP `27.936` edge `0.0314` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7032` n `31` status `ready` deltaP `16.1438` edge `0.0223` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0717` n `31` status `ready` deltaP `1.3811` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3635` n `106` status `ready` deltaP `1.8557` edge `0.0075` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3963` n `106` status `ready` deltaP `2.141` edge `0.0014` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.261` n `106` status `ready` deltaP `-9.0753` edge `-0.0016` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5259` n `106` status `ready` deltaP `-0.3164` edge `0.0037` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
