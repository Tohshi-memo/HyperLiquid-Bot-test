# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T17:52:37.611732+00:00`
- Price records: `672`
- Market context records: `6003`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11142`

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

- `news_risk_high->fx_24h` score `7.5803` n `30` status `ready` deltaP `68.9236` edge `0.1722` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1701` n `30` status `ready` deltaP `43.2012` edge `0.0641` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9351` n `30` status `ready` deltaP `31.2848` edge `0.1399` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.219` n `30` status `ready` deltaP `26.6267` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2188` n `221` status `ready` deltaP `7.7564` edge `0.1593` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7514` n `30` status `ready` deltaP `9.8902` edge `0.0771` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.4718` n `194` status `ready` deltaP `24.2698` edge `0.3986` maxDD `-30.0202`
- `news_risk_high->crypto_alt_1h` score `0.1522` n `30` status `ready` deltaP `5.1697` edge `0.0312` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1218` n `30` status `ready` deltaP `9.2361` edge `0.0412` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.404` n `30` status `ready` deltaP `1.6866` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5055` n `221` status `ready` deltaP `2.1995` edge `0.0004` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5724` n `221` status `ready` deltaP `-0.5256` edge `0.0022` maxDD `-0.7117`
- `market_context_high->equity_1h` score `-0.582` n `221` status `ready` deltaP `2.0599` edge `0.0245` maxDD `-4.3608`
- `market_context_high->fx_1h` score `-0.6707` n `221` status `ready` deltaP `-0.5528` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0399` n `30` status `ready` deltaP `-9.4012` edge `-0.0192` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0971` n `221` status `ready` deltaP `-0.9401` edge `-0.0048` maxDD `-3.0339`
- `market_context_high->index_4h` score `-1.1503` n `221` status `ready` deltaP `0.5214` edge `0.0162` maxDD `-3.0392`
- `market_context_high->crypto_major_1h` score `-1.2201` n `221` status `ready` deltaP `1.7605` edge `0.0086` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2577` n `221` status `ready` deltaP `0.9917` edge `0.0074` maxDD `-9.3536`
- `market_context_high->index_1h` score `-1.338` n `221` status `ready` deltaP `-3.2474` edge `0.0015` maxDD `-1.3078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
