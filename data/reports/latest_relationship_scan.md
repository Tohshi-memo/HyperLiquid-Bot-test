# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T21:52:27.998871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5126`

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

- `market_context_high->unknown_1h` score `12060.0932` n `106` status `ready` deltaP `-0.1978` edge `1005.0289` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `8010.5835` n `101` status `ready` deltaP `-2.7364` edge `667.5974` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1383.061` n `31` status `ready` deltaP `3.728` edge `115.2478` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1214.4961` n `31` status `ready` deltaP `3.9388` edge `101.1874` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1928` n `31` status `ready` deltaP `40.2734` edge `0.7958` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0913` n `31` status `ready` deltaP `25.8457` edge `0.839` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.836` n `31` status `ready` deltaP `15.711` edge `0.9134` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9894` n `31` status `ready` deltaP `19.5383` edge `0.2209` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.619` n `31` status `ready` deltaP `37.5295` edge `0.0774` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7358` n `31` status `ready` deltaP `31.9925` edge `0.0232` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4642` n `31` status `ready` deltaP `9.5615` edge `0.2983` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0565` n `31` status `ready` deltaP `8.2142` edge `0.2446` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6882` n `31` status `ready` deltaP `22.5708` edge `0.1217` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5664` n `31` status `ready` deltaP `29.433` edge `0.0325` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7645` n `31` status `ready` deltaP `17.6682` edge `0.02` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0801` n `31` status `ready` deltaP `1.2314` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.4371` n `106` status `ready` deltaP `3.3527` edge `0.0077` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4613` n `106` status `ready` deltaP `1.3473` edge `0.0014` maxDD `-1.2394`
- `market_context_high->fx_1h` score `-1.4083` n `106` status `ready` deltaP `-11.0072` edge `-0.001` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.4105` n `101` status `ready` deltaP `-0.335` edge `0.0049` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
