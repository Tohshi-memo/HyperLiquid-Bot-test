# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T23:22:26.320109+00:00`
- Price records: `672`
- Market context records: `6863`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->unknown_24h` score `1.1979` n `176` status `ready` deltaP `-1.8001` edge `0.5408` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2409` n `224` status `ready` deltaP `2.3872` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6501` n `224` status `ready` deltaP `-1.497` edge `-0.0049` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6512` n `224` status `ready` deltaP `1.3126` edge `0.0134` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.688` n `224` status `ready` deltaP `3.0983` edge `0.0124` maxDD `-4.2314`
- `market_context_high->commodity_24h` score `-0.813` n `176` status `ready` deltaP `5.1255` edge `0.0849` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.8507` n `224` status `ready` deltaP `-2.2268` edge `-0.0031` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9461` n `224` status `ready` deltaP `-5.4908` edge `-0.0079` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9914` n `223` status `ready` deltaP `10.976` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3503` n `223` status `ready` deltaP `-2.4803` edge `-0.0076` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6289` n `224` status `ready` deltaP `-3.2613` edge `-0.0239` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9203` n `224` status `ready` deltaP `0.2887` edge `-0.0301` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.052` n `223` status `ready` deltaP `2.909` edge `-0.0245` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4498` n `223` status `ready` deltaP `-0.4737` edge `-0.0126` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-3.1232` n `223` status `ready` deltaP `-9.1215` edge `0.0371` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.1556` n `223` status `ready` deltaP `-1.8961` edge `-0.0592` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2038` n `223` status `ready` deltaP `-0.9747` edge `-0.0459` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5457` n `176` status `ready` deltaP `-9.8816` edge `-0.0093` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5613` n `223` status `ready` deltaP `-0.1809` edge `-0.1737` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0077` n `176` status `ready` deltaP `-18.9332` edge `-0.1801` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
