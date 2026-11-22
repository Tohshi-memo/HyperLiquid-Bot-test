# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T18:22:28.510923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4102`

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

- `market_context_high->unknown_1h` score `12019.1636` n `106` status `ready` deltaP `-0.5424` edge `1001.6204` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7489.4453` n `106` status `ready` deltaP `-2.2694` edge `624.1661` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1398.8013` n `31` status `ready` deltaP `4.3268` edge `116.5555` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1239.5869` n `31` status `ready` deltaP `3.9388` edge `103.2783` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0032` n `31` status `ready` deltaP `40.2734` edge `0.78` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.7218` n `31` status `ready` deltaP `24.0165` edge `0.8204` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6308` n `31` status `ready` deltaP `14.644` edge `0.8942` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9283` n `31` status `ready` deltaP `19.2389` edge `0.2178` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.478` n `31` status `ready` deltaP `36.1576` edge `0.0748` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6699` n `31` status `ready` deltaP `31.244` edge `0.0227` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3933` n `31` status `ready` deltaP `8.813` edge `0.2942` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0199` n `31` status `ready` deltaP `8.0645` edge `0.2409` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5392` n `31` status `ready` deltaP `20.5891` edge `0.1158` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.4964` n `31` status `ready` deltaP `28.2354` edge `0.0315` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7649` n `31` status `ready` deltaP `17.2108` edge `0.0231` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0837` n `31` status `ready` deltaP `1.2314` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3472` n `106` status `ready` deltaP `2.1551` edge `0.0076` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4466` n `106` status `ready` deltaP `1.5422` edge `0.0012` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2598` n `106` status `ready` deltaP `-9.0753` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.522` n `106` status `ready` deltaP `-0.3164` edge `0.0042` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
