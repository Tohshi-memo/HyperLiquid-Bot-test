# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T05:52:24.277966+00:00`
- Price records: `672`
- Market context records: `6890`
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

- `market_context_high->unknown_24h` score `0.4518` n `185` status `ready` deltaP `-5.3417` edge `0.4809` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2222` n `224` status `ready` deltaP `2.6866` edge `0.0021` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5865` n `224` status `ready` deltaP `1.9114` edge `0.0148` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.5941` n `224` status `ready` deltaP `-0.5988` edge `-0.0037` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6653` n `224` status `ready` deltaP `3.3977` edge `0.0123` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.811` n `224` status `ready` deltaP `-1.4783` edge `-0.003` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8825` n `224` status `ready` deltaP `12.9356` edge `0.007` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8853` n `224` status `ready` deltaP `-4.4429` edge `-0.0071` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3146` n `224` status `ready` deltaP `-1.8838` edge `-0.007` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6697` n `224` status `ready` deltaP `-3.411` edge `-0.0263` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8362` n `224` status `ready` deltaP `1.3366` edge `-0.0263` maxDD `-13.1084`
- `market_context_high->commodity_24h` score `-1.8724` n `185` status `ready` deltaP `1.1981` edge `0.0228` maxDD `-5.2791`
- `market_context_high->index_4h` score `-2.0277` n `224` status `ready` deltaP `3.3319` edge `-0.0242` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.351` n `224` status `ready` deltaP `0.9473` edge `-0.0094` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.0782` n `224` status `ready` deltaP `0.0762` edge `-0.0368` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-3.0797` n `224` status `ready` deltaP `-1.3066` edge `-0.0534` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1869` n `224` status `ready` deltaP `-9.6472` edge `0.0353` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2415` n `185` status `ready` deltaP `-6.5296` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4258` n `224` status `ready` deltaP `0.7295` edge `-0.1624` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.6052` n `185` status `ready` deltaP `-15.0546` edge `-0.1443` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
