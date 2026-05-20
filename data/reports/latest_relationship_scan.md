# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T10:07:16.664019+00:00`
- Price records: `672`
- Market context records: `1311`
- Flow alert records: `5684`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8781`

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

- `market_context_high->crypto_major_24h` score `16.6952` n `128` status `ready` deltaP `40.5381` edge `1.2342` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.1899` n `128` status `ready` deltaP `12.3264` edge `1.1837` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6024` n `128` status `ready` deltaP `28.3854` edge `0.8126` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.9374` n `128` status `ready` deltaP `30.9028` edge `0.3974` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.7914` n `128` status `ready` deltaP `23.7847` edge `0.5602` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5597` n `157` status `ready` deltaP `13.1107` edge `0.1964` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1388` n `128` status `ready` deltaP `0.0` edge `0.4512` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.9438` n `128` status `ready` deltaP `-14.7569` edge `0.3252` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.8112` n `128` status `ready` deltaP `9.9827` edge `0.0475` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2068` n `157` status `ready` deltaP `3.6671` edge `0.0355` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1873` n `157` status `ready` deltaP `5.9413` edge `0.0933` maxDD `-3.7119`
- `market_context_high->metal_4h` score `0.1869` n `157` status `ready` deltaP `13.5253` edge `0.0685` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1022` n `157` status `ready` deltaP `6.0624` edge `0.0181` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0847` n `157` status `ready` deltaP `8.7923` edge `0.0033` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.511` n `157` status `ready` deltaP `0.9583` edge `-0.0034` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6301` n `157` status `ready` deltaP `0.5473` edge `0.0309` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8569` n `157` status `ready` deltaP `10.2969` edge `0.1919` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9078` n `157` status `ready` deltaP `-1.3664` edge `-0.0052` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9544` n `157` status `ready` deltaP `3.5634` edge `0.081` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-1.024` n `157` status `ready` deltaP `-2.4524` edge `-0.0075` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
