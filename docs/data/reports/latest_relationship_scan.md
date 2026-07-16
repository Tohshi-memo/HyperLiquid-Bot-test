# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T00:07:28.942237+00:00`
- Price records: `672`
- Market context records: `6866`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `market_context_high->index_1h` score `-0.2491` n `224` status `ready` deltaP `4.3092` edge `-0.0005` maxDD `-0.4799`
- `market_context_high->crypto_alt_1h` score `-0.6584` n `224` status `ready` deltaP `1.3126` edge `0.0128` maxDD `-3.7803`
- `market_context_high->index_4h` score `-0.6866` n `223` status `ready` deltaP `5.0071` edge `-0.0019` maxDD `-1.894`
- `market_context_high->crypto_major_1h` score `-0.6892` n `224` status `ready` deltaP `3.0983` edge `0.0123` maxDD `-4.2314`
- `market_context_high->metal_4h` score `-0.7944` n `223` status `ready` deltaP `5.6849` edge `0.0018` maxDD `-0.9902`
- `market_context_high->metal_1h` score `-0.8` n `224` status `ready` deltaP `-6.0816` edge `-0.0003` maxDD `-0.271`
- `market_context_high->equity_1h` score `-1.0572` n `224` status `ready` deltaP `-4.9107` edge `-0.001` maxDD `-0.4774`
- `market_context_high->equity_4h` score `-1.5811` n `223` status `ready` deltaP `-2.1596` edge `-0.0031` maxDD `-1.8169`
- `market_context_high->unknown_1h` score `-1.7925` n `224` status `ready` deltaP `-5.0417` edge `-0.027` maxDD `-3.1014`
- `market_context_high->unknown_24h` score `-2.4186` n `176` status `ready` deltaP `-6.7975` edge `0.3952` maxDD `-30.7971`
- `market_context_high->crypto_major_4h` score `-3.1548` n `223` status `ready` deltaP `-1.8961` edge `-0.0591` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2023` n `223` status `ready` deltaP `-0.9747` edge `-0.0457` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3366` n `223` status `ready` deltaP `-9.2737` edge `0.0123` maxDD `-9.6155`
- `market_context_high->index_24h` score `-4.7692` n `176` status `ready` deltaP `-12.2006` edge `-0.0295` maxDD `-7.3811`
- `market_context_high->metal_24h` score `-5.3403` n `176` status `ready` deltaP `-6.7532` edge `-0.0254` maxDD `-8.8052`
- `market_context_high->equity_24h` score `-6.6884` n `176` status `ready` deltaP `-18.7313` edge `-0.0434` maxDD `-9.1273`
- `market_context_high->commodity_24h` score `-8.8` n `176` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->fx_24h` score `-8.8` n `176` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->commodity_4h` score `-11.15` n `223` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->fx_4h` score `-11.15` n `223` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
