# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T13:52:30.158420+00:00`
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

- `market_context_high->unknown_1h` score `12044.6696` n `106` status `ready` deltaP `-0.3927` edge `1003.7449` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7517.1985` n `106` status `ready` deltaP `-2.5742` edge `626.4809` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1424.3073` n `31` status `ready` deltaP `4.4765` edge `118.68` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1267.3401` n `31` status `ready` deltaP `3.634` edge `105.5931` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9406` n `31` status `ready` deltaP `40.121` edge `0.7758` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.7826` n `31` status `ready` deltaP `23.7116` edge `0.8275` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7159` n `31` status `ready` deltaP `14.7964` edge `0.9041` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0229` n `31` status `ready` deltaP `20.1371` edge `0.2197` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4816` n `31` status `ready` deltaP `36.1576` edge `0.0751` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.707` n `31` status `ready` deltaP `31.6931` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5445` n `31` status `ready` deltaP `10.0106` edge `0.3056` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1228` n `31` status `ready` deltaP `8.6633` edge `0.2501` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5416` n `31` status `ready` deltaP `20.7415` edge `0.1151` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5151` n `31` status `ready` deltaP `28.5348` edge `0.0319` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.6415` n `31` status `ready` deltaP `15.0767` edge `0.0215` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.1196` n `31` status `ready` deltaP `0.7823` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3285` n `106` status `ready` deltaP `2.4545` edge `0.008` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4095` n `106` status `ready` deltaP `1.9913` edge `0.0013` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2119` n `106` status `ready` deltaP `-8.4765` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5267` n `106` status `ready` deltaP `-0.3164` edge `0.0036` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
