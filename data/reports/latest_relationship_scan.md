# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T22:52:28.359782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_1h` score `12653.4248` n `102` status `ready` deltaP `1.2064` edge `1054.4602` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8485.3002` n `97` status `ready` deltaP `-2.6873` edge `707.1568` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1377.0502` n `31` status `ready` deltaP `3.5783` edge `114.7479` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.535` n `31` status `ready` deltaP `4.3962` edge `100.9376` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1832` n `31` status `ready` deltaP `40.2734` edge `0.795` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0661` n `31` status `ready` deltaP `25.8457` edge `0.8369` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.8094` n `31` status `ready` deltaP `15.5586` edge `0.911` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0397` n `31` status `ready` deltaP `19.9874` edge `0.2221` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6336` n `31` status `ready` deltaP `37.682` edge `0.0776` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7489` n `31` status `ready` deltaP `32.1422` edge `0.0233` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5226` n `31` status `ready` deltaP `10.1603` edge `0.3018` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1126` n `31` status `ready` deltaP `8.6633` edge `0.2488` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.7088` n `31` status `ready` deltaP `22.8757` edge `0.1223` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5836` n `31` status `ready` deltaP `29.7324` edge `0.0327` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7536` n `31` status `ready` deltaP `17.6682` edge `0.0186` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0813` n `31` status `ready` deltaP `1.2314` edge `0.0112` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.4506` n `102` status `ready` deltaP `1.497` edge `0.0013` maxDD `-1.2394`
- `market_context_high->metal_1h` score `-0.5071` n `102` status `ready` deltaP `2.5977` edge `0.0069` maxDD `-2.6517`
- `market_context_high->fx_4h` score `-1.2131` n `97` status `ready` deltaP `0.6883` edge `0.0052` maxDD `-1.2255`
- `market_context_high->fx_1h` score `-1.3355` n `102` status `ready` deltaP `-10.2002` edge `-0.0011` maxDD `-0.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
