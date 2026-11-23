# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T00:27:35.625949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5270`

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

- `market_context_high->unknown_1h` score `13631.8595` n `96` status `ready` deltaP `0.6549` edge `1136.0001` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8947.9493` n `94` status `ready` deltaP `-0.8886` edge `745.6989` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1363.3486` n `31` status `ready` deltaP `3.5783` edge `113.6061` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1198.5918` n `31` status `ready` deltaP `4.3962` edge `99.859` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0612` n `31` status `ready` deltaP `39.6637` edge `0.7889` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0321` n `31` status `ready` deltaP `25.5409` edge `0.8361` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7111` n `31` status `ready` deltaP `14.644` edge `0.9045` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0781` n `31` status `ready` deltaP `20.1371` edge `0.2243` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.624` n `31` status `ready` deltaP `37.682` edge `0.0768` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7669` n `31` status `ready` deltaP `32.2919` edge `0.0238` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4985` n `31` status `ready` deltaP `9.8609` edge `0.3007` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1111` n `31` status `ready` deltaP `8.6633` edge `0.2486` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6482` n `31` status `ready` deltaP `22.2659` edge `0.1186` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5914` n `31` status `ready` deltaP `29.8821` edge `0.0327` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7637` n `31` status `ready` deltaP `17.6682` edge `0.0199` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0597` n `31` status `ready` deltaP `1.3811` edge `0.012` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.503` n `96` status `ready` deltaP `-1.4783` edge `-0.0058` maxDD `-1.2394`
- `market_context_high->fx_4h` score `-0.7978` n `94` status `ready` deltaP `4.2813` edge `0.0079` maxDD `-1.0983`
- `market_context_high->metal_1h` score `-0.9351` n `96` status `ready` deltaP `-0.5614` edge `-0.0077` maxDD `-2.6517`
- `market_context_high->fx_1h` score `-1.2675` n `96` status `ready` deltaP `-9.3625` edge `-0.0012` maxDD `-0.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
