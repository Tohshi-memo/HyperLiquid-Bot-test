# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T18:07:27.287269+00:00`
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

- `market_context_high->unknown_1h` score `12019.832` n `106` status `ready` deltaP `-0.5424` edge `1001.6761` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7489.3527` n `106` status `ready` deltaP `-2.4218` edge `624.1594` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1399.4697` n `31` status `ready` deltaP `4.3268` edge `116.6112` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1239.4943` n `31` status `ready` deltaP `3.7864` edge `103.2716` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9984` n `31` status `ready` deltaP `40.2734` edge `0.7796` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.7` n `31` status `ready` deltaP `23.864` edge `0.8196` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.63` n `31` status `ready` deltaP `14.644` edge `0.8941` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9438` n `31` status `ready` deltaP `19.3886` edge `0.2181` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4768` n `31` status `ready` deltaP `36.1576` edge `0.0747` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6699` n `31` status `ready` deltaP `31.244` edge `0.0227` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3933` n `31` status `ready` deltaP `8.813` edge `0.2942` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0167` n `31` status `ready` deltaP `8.0645` edge `0.2405` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5392` n `31` status `ready` deltaP `20.5891` edge `0.1158` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.4886` n `31` status `ready` deltaP `28.0857` edge `0.0315` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7554` n `31` status `ready` deltaP `17.0584` edge `0.0229` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0837` n `31` status `ready` deltaP `1.2314` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.355` n `106` status `ready` deltaP `2.0054` edge `0.0076` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4466` n `106` status `ready` deltaP `1.5422` edge `0.0012` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2598` n `106` status `ready` deltaP `-9.0753` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5228` n `106` status `ready` deltaP `-0.3164` edge `0.0041` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
