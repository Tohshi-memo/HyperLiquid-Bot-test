# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T13:52:26.852741+00:00`
- Price records: `672`
- Market context records: `1326`
- Flow alert records: `5730`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `15.6888` n `128` status `ready` deltaP `37.934` edge `1.1677` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.4961` n `128` status `ready` deltaP `13.8889` edge `1.1988` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.7296` n `128` status `ready` deltaP `28.3854` edge `0.8232` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.3691` n `128` status `ready` deltaP `28.2986` edge `0.3674` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0858` n `128` status `ready` deltaP `21.1806` edge `0.4871` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3471` n `157` status `ready` deltaP `12.0436` edge `0.1858` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.6397` n `128` status `ready` deltaP `-2.0833` edge `0.4235` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.5326` n `128` status `ready` deltaP `-12.1528` edge `0.3569` maxDD `-6.8535`
- `market_context_high->fx_24h` score `1.1035` n `128` status `ready` deltaP `12.5869` edge `0.0545` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1749` n `157` status `ready` deltaP `13.5253` edge `0.0675` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1673` n `157` status `ready` deltaP `3.218` edge `0.0352` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0943` n `157` status `ready` deltaP `4.8742` edge `0.0885` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0524` n `157` status `ready` deltaP `5.1642` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0067` n `157` status `ready` deltaP `9.3911` edge `0.0058` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5254` n `157` status `ready` deltaP `0.8086` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6121` n `157` status `ready` deltaP `0.5473` edge `0.0324` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.9311` n `157` status `ready` deltaP `-1.5161` edge `-0.0072` maxDD `-5.8323`
- `market_context_high->commodity_1h` score `-0.9425` n `157` status `ready` deltaP `-2.0033` edge `-0.0037` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-0.9701` n `157` status `ready` deltaP `9.992` edge `0.1845` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-0.9871` n `157` status `ready` deltaP `3.7158` edge `0.0758` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
