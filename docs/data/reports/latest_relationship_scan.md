# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T21:52:43.962621+00:00`
- Price records: `672`
- Market context records: `6858`
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

- `market_context_high->unknown_24h` score `1.1588` n `176` status `ready` deltaP `-1.5467` edge `0.5341` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2573` n `224` status `ready` deltaP `2.0878` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6225` n `224` status `ready` deltaP `1.612` edge `0.0138` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.6278` n `176` status `ready` deltaP `6.0606` edge `0.0941` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.6797` n `224` status `ready` deltaP `3.248` edge `0.0121` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6883` n `224` status `ready` deltaP `-2.0958` edge `-0.0058` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8764` n `224` status `ready` deltaP `-2.6759` edge `-0.0034` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9375` n `224` status `ready` deltaP `-5.3411` edge `-0.0078` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0118` n `219` status `ready` deltaP `10.5837` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.413` n `219` status `ready` deltaP `-3.2798` edge `-0.0103` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6794` n `224` status `ready` deltaP `-3.1116` edge `-0.0291` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9733` n `224` status `ready` deltaP `-0.3101` edge `-0.0329` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0525` n `219` status `ready` deltaP `2.961` edge `-0.0249` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4405` n `219` status `ready` deltaP `-0.3703` edge `-0.0121` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1021` n `219` status `ready` deltaP `-1.3031` edge `-0.0563` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1411` n `219` status `ready` deltaP `-9.0447` edge `0.0351` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.197` n `219` status `ready` deltaP `-0.8443` edge `-0.0459` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5164` n `176` status `ready` deltaP `-9.7853` edge `-0.0075` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5903` n `219` status `ready` deltaP `-0.0793` edge `-0.1781` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0359` n `176` status `ready` deltaP `-18.8447` edge `-0.1843` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
