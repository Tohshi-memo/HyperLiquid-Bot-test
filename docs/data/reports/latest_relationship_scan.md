# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T05:07:25.950854+00:00`
- Price records: `672`
- Market context records: `6887`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `0.4526` n `185` status `ready` deltaP `-5.3417` edge `0.481` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.223` n `224` status `ready` deltaP `2.6866` edge `0.002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5242` n `224` status `ready` deltaP `2.3605` edge `0.017` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5838` n `224` status `ready` deltaP `3.8468` edge `0.0161` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.612` n `224` status `ready` deltaP `-0.8982` edge `-0.004` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7915` n `224` status `ready` deltaP `-1.1789` edge `-0.0025` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8919` n `224` status `ready` deltaP `12.7831` edge `0.0068` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.9032` n `224` status `ready` deltaP `-4.7423` edge `-0.0074` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3138` n `224` status `ready` deltaP `-1.8838` edge `-0.0069` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.593` n `224` status `ready` deltaP `-2.9619` edge `-0.0229` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7934` n `224` status `ready` deltaP `1.7857` edge `-0.0238` maxDD `-13.1084`
- `market_context_high->commodity_24h` score `-1.8124` n `185` status `ready` deltaP `1.1981` edge `0.0278` maxDD `-5.2791`
- `market_context_high->index_4h` score `-2.0048` n `224` status `ready` deltaP `3.6368` edge `-0.0233` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3612` n `224` status `ready` deltaP `0.7948` edge `-0.0097` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0639` n `224` status `ready` deltaP `-1.1542` edge `-0.0524` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.079` n `224` status `ready` deltaP `0.0762` edge `-0.0369` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1857` n `224` status `ready` deltaP `-9.6472` edge `0.0354` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2367` n `185` status `ready` deltaP `-6.5296` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.37` n `224` status `ready` deltaP `1.1869` edge `-0.1583` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.6325` n `185` status `ready` deltaP `-15.0546` edge `-0.1478` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
