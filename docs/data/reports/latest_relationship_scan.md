# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T09:07:32.607803+00:00`
- Price records: `672`
- Market context records: `6903`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `0.3508` n `188` status `ready` deltaP `-4.2461` edge `0.4679` maxDD `-13.903`
- `market_context_high->fx_1h` score `-0.195` n `224` status `ready` deltaP `3.1357` edge `0.0026` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.342` n `224` status `ready` deltaP `3.4084` edge `0.0252` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4207` n `224` status `ready` deltaP `4.8947` edge `0.0227` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6058` n `224` status `ready` deltaP `-0.7485` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7671` n `224` status `ready` deltaP `14.7649` edge `0.0096` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7744` n `224` status `ready` deltaP `-0.8795` edge `-0.0023` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8409` n `224` status `ready` deltaP `-3.8441` edge `-0.0054` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3357` n `224` status `ready` deltaP `-1.8838` edge `-0.0097` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5774` n `224` status `ready` deltaP `-3.1116` edge `-0.0206` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7528` n `224` status `ready` deltaP `2.0851` edge `-0.0206` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9235` n `224` status `ready` deltaP `4.8563` edge `-0.021` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1843` n `224` status `ready` deltaP `2.4717` edge `0.0018` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.2017` n `188` status `ready` deltaP `0.5476` edge `-0.0003` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.7692` n `224` status `ready` deltaP `2.0579` edge `-0.0104` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8556` n `224` status `ready` deltaP `-0.0871` edge `-0.0328` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0193` n `224` status `ready` deltaP `-8.1228` edge `0.0391` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1875` n `188` status `ready` deltaP `-5.8842` edge `-0.0061` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1765` n `224` status `ready` deltaP `2.2539` edge `-0.1406` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3727` n `188` status `ready` deltaP `-13.6657` edge `-0.1237` maxDD `-28.3558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
