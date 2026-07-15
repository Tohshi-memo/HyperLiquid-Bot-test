# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T23:36:51.687522+00:00`
- Price records: `672`
- Market context records: `6864`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `market_context_high->unknown_24h` score `1.1971` n `176` status `ready` deltaP `-1.8001` edge `0.5407` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2409` n `224` status `ready` deltaP `2.3872` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6392` n `224` status `ready` deltaP `-1.3473` edge `-0.0045` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6524` n `224` status `ready` deltaP `1.3126` edge `0.0133` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.688` n `224` status `ready` deltaP `3.0983` edge `0.0124` maxDD `-4.2314`
- `market_context_high->commodity_24h` score `-0.8497` n `176` status `ready` deltaP `4.9522` edge `0.083` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.8593` n `224` status `ready` deltaP `-2.3765` edge `-0.0032` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9484` n `224` status `ready` deltaP `-5.4908` edge `-0.0082` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9835` n `223` status `ready` deltaP `11.1282` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3401` n `223` status `ready` deltaP `-2.3281` edge `-0.0073` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6529` n `224` status `ready` deltaP `-3.411` edge `-0.0249` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9305` n `224` status `ready` deltaP `0.139` edge `-0.0304` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.052` n `223` status `ready` deltaP `2.909` edge `-0.0245` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4593` n `223` status `ready` deltaP `-0.6259` edge `-0.0128` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-3.128` n `223` status `ready` deltaP `-9.1215` edge `0.0367` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.1563` n `223` status `ready` deltaP `-1.8961` edge `-0.0593` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2054` n `223` status `ready` deltaP `-0.9747` edge `-0.0461` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5493` n `176` status `ready` deltaP `-9.8816` edge `-0.0096` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5487` n `223` status `ready` deltaP `-0.0287` edge `-0.1731` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0023` n `176` status `ready` deltaP `-18.9332` edge `-0.1794` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
