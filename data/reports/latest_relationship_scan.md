# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T18:37:39.189764+00:00`
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

- `market_context_high->unknown_1h` score `12018.4628` n `106` status `ready` deltaP `-0.5424` edge `1001.562` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7485.1793` n `106` status `ready` deltaP `-2.2694` edge `623.8106` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1398.1005` n `31` status `ready` deltaP `4.3268` edge `116.4971` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1235.3209` n `31` status `ready` deltaP `3.9388` edge `102.9228` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0092` n `31` status `ready` deltaP `40.2734` edge `0.7805` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.752` n `31` status `ready` deltaP `24.1689` edge `0.8219` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.637` n `31` status `ready` deltaP `14.644` edge `0.895` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9151` n `31` status `ready` deltaP `19.0892` edge `0.2177` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.478` n `31` status `ready` deltaP `36.1576` edge `0.0748` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6579` n `31` status `ready` deltaP `31.0943` edge `0.0227` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.405` n `31` status `ready` deltaP `8.9627` edge `0.2947` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0362` n `31` status `ready` deltaP `8.2142` edge `0.242` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.54` n `31` status `ready` deltaP `20.5891` edge `0.1159` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5049` n `31` status `ready` deltaP `28.3851` edge `0.0316` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7736` n `31` status `ready` deltaP `17.3633` edge `0.0232` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0837` n `31` status `ready` deltaP `1.2314` edge `0.011` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3386` n `106` status `ready` deltaP `2.3048` edge `0.0077` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4586` n `106` status `ready` deltaP `1.3925` edge `0.0012` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2598` n `106` status `ready` deltaP `-9.0753` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5212` n `106` status `ready` deltaP `-0.3164` edge `0.0043` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
